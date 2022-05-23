#!/usr/bin/env python3
import os, subprocess
import sys, json;

def eprint(*args, **kwargs):
  print(*args, file=sys.stderr, **kwargs)

input = json.load(sys.stdin)
container_definition = json.loads(input['container_definition_json'])
lacework_access_token = input['lacework_access_token']

datacollector_json = {
  "name": "datacollector-sidecar",
  "image": "lacework/datacollector:latest-sidecar",
  "cpu": 0,
  "portMappings": [],
  "essential": False,
  "environment": [],
  "mountPoints": [],
  "volumesFrom": []
}

container_definition.append(datacollector_json)

container_definition[0]['essential'] = True

lw_access_token_env = {
  "name": "LaceworkAccessToken",
  "value": lacework_access_token
}
container_definition[0].setdefault('environment', []).append(lw_access_token_env)

entrypoint = None
command = None
if 'entrypoint' in container_definition[0].keys():
  if container_definition[0]['entrypoint'] == '':
    entrypoint = []
  entrypoint = container_definition[0]['entrypoint']
if 'command' in container_definition[0].keys():
  if container_definition[0]['command'] == '':
    command = []
  command = container_definition[0]['command']

injector_input = {
  "entrypoint": entrypoint,
  "cmd": command,
  "container": container_definition[0]['image']
}
injected_data = json.loads(subprocess.check_output([os.path.dirname(os.path.abspath(__file__)) + '/entrypoint-cmd-injector.py'],text=True,input=json.dumps(injector_input)))
container_definition[0]['entrypoint'] = injected_data['entrypoint']
container_definition[0]['command'] = injected_data['cmd']

lw_volume = {
  "sourceContainer": "datacollector-sidecar",
  "readOnly": True
}
container_definition[0].setdefault('volumesFrom', []).append(lw_volume)

lw_depends = {
  "containerName": "datacollector-sidecar",
  "condition": "SUCCESS"
}
container_definition[0].setdefault('dependsOn', []).append(lw_depends)
output = {"container_definition_json": json.dumps(container_definition)}
print(json.dumps(output))