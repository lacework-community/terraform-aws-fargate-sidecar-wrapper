#!/usr/bin/env python3
import os, subprocess
import sys, json;

def forcearray(input):
  if isinstance(input, str):
    return [input]
  if input is None:
    return []
  return input

input = json.load(sys.stdin)
def is_not_blank(s):
  return bool(s and not s.isspace())

if isinstance(input['entrypoint'], list) or isinstance(input['cmd'], list) or is_not_blank(input['entrypoint']) or is_not_blank(input['cmd']):
  cmd = input['cmd']
  entrypoint = input['entrypoint']
else:
  try:
    subprocess.check_call(['docker','pull', input['container']], stdout=open(os.devnull, 'wb'))
  except subprocess.CalledProcessError:
    print(f"{os.path.basename(__file__)}: Error pulling container")
    sys.exit(1)
  try:
    cmd = json.loads(subprocess.check_output(['docker', 'inspect', "--format={{json .Config.Cmd}}", input['container']], text=True))
    entrypoint = json.loads(subprocess.check_output(['docker', 'inspect', "--format={{json .Config.Entrypoint}}", input['container']], text=True))
  except subprocess.CalledProcessError:
    print(f"{os.path.basename(__file__)}: Error getting CMD / ENTRYPOINT")
    sys.exit(1)


cmd = forcearray(cmd)
entrypoint = forcearray(entrypoint)

entrypoint.insert(0,'/var/lib/lacework-backup/lacework-sidecar.sh')

print(json.dumps({'entrypoint': entrypoint, 'cmd': cmd}))

# docker inspect  nginx:latest
# null or []

# docker inspect --format='{{json .Config.Entrypoint}}' nginx:latest
# null or []

