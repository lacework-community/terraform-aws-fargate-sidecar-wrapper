<a href="https://lacework.com"><img src="https://techally-content.s3-us-west-1.amazonaws.com/public-content/lacework_logo_full.png" width="600"></a>

# terraform-aws-fargate-sidecar-wrapper

<!--[![GitHub release](https://img.shields.io/github/release/lacework/terraform-aws-cloudtrail.svg)](https://github.com/lacework/terraform-aws-cloudtrail/releases/)
[![Codefresh build status]( https://g.codefresh.io/api/badges/pipeline/lacework/terraform-modules%2Ftest-compatibility?type=cf-1&key=eyJhbGciOiJIUzI1NiJ9.NWVmNTAxOGU4Y2FjOGQzYTkxYjg3ZDEx.RJ3DEzWmBXrJX7m38iExJ_ntGv4_Ip8VTa-an8gBwBo)]( https://g.codefresh.io/pipelines/edit/new/builds?id=607e25e6728f5a6fba30431b&pipeline=test-compatibility&projects=terraform-modules&projectId=607db54b728f5a5f8930405d)
-->
Terraform module for configuring an ECS Fargate Task Definition with attempt to automatically add the Lacework sidecar @ apply.

Use of this module does require `docker pull` access to the first container in the container definition.

If you wish to use this module without access to docker, you may specify the `CMD` and/or `ENTRYPOINT` in the container defininition JSON to skip the `docker pull` stage.

## How it works

When you provide this module a complete container definition JSON block, the following steps are performed 100% automatically:

1. A script runs which adds the Lacework sidecar container definition to the end of the container definition
1. The correct depends / volume parameters are added to the first container definition in the JSON
1. The `ENTRYPOINT` and/or `CMD` from the first container definition in the `container_definition_json` is retrieved using `docker`
1. The Lacework sidecar script gets prepended to the `ENTRYPOINT` field of the first container definition

## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 0.12.31 |
| <a name="requirement_docker"></a> [docker](#requirement\_docker) | ~> 20.0 |
| <a name="requirement_python"></a> [python](#requirement\_docker) | ~> 3.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 4.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | ~> 4.0 |

## Resources

| Name | Type |
|------|------|
| [aws_ecs_task_definition.task_definition](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/aws_ecs_task_definition) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="cpu"></a> [cpu](#cpu) | Number of cpu units used by the task. | `string` | `""` | yes |
| <a name="memory"></a> [memory](#memory) | Amount (in MiB) of memory used by the task. | `string` | `""` | yes |
| <a name="family"></a> [family](#family) | A unique name for your task definition. | `string` | `""` | yes |
| <a name="container_definition_json"></a> [container\_definition\_json](#container\_definition\_json) | The container definition one would pass to aws_ecs_task_definition. | `string` | `""` | yes |
| <a name="lacework_access_token"></a> [lacework\_access\_token](#lacework\_access\_token) | A valid Lacework Access Token. | `string` | `""` | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="ecs_task_definition_arn"></a> [ecs\_task\_definition\_arn](#ecs\_task\_definition\_arn) | ECS Task Definition ARN |
