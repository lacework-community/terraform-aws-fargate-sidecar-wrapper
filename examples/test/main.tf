module "lacework_aws_ecs_task_definition" {
  source = "../../"
  container_definition_json = file("sample-container-definition.json")
  cpu = "256"
  memory = "512"
  family = "test"
  lacework_access_token = "12345abcde12345abcde12345abcde12345abcde12345abcde12345a"
}