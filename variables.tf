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