locals {
  ecs_task_definition_arn = aws_ecs_task_definition.task_definition.arn
}

data "external" "sidecarinjector" {
  program = [
    "${path.module}/sidecar-injector.py",
  ]
  query = {
    container_definition_json = var.container_definition_json
    lacework_access_token = var.lacework_access_token
  }
}

resource "aws_ecs_task_definition" "task_definition" {
  family = var.family
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = var.cpu
  memory                   = var.memory
  container_definitions    = data.external.sidecarinjector.result.container_definition_json
}
