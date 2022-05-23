variable "cpu" {
  type        = string
  description = "(Required) Number of cpu units used by the task."
}
variable "memory" {
  type        = string
  description = "(Required) Amount (in MiB) of memory used by the task."
}
variable "family" {
  type        = string
  description = "(Required) A unique name for your task definition."
}
variable "container_definition_json" {
  type        = string
  description = "(Required) The container definition one would pass to aws_ecs_task_definition"
}
variable "lacework_access_token" {
  type        = string
  description = "(Required) A valid Lacework Access Token"
}
variable "execution_role_arn" {
  type        = string
  description = "(Optional) ARN of the task execution role that the Amazon ECS container agent and the Docker daemon can assume."
  default     = ""
}
variable "tags" {
  type        = map(string)
  description = "A map/dictionary of Tags to be assigned to created resources"
  default     = {}
}