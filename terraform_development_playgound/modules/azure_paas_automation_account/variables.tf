variable "applicationname" { description = "name of the application. Will be used for naming conventions" }
variable "region_abbreviation" { description = "name of the regional abbreviation. Will be used for naming conventions" }
variable "environment" { description = "name of the environment which is equal to the TF workspace. Will be used for naming conventions" }
variable "automation_account_name" { description = "name of the automation account" }
variable "automation_account_location" { description = "azure region of the automation account" }
variable "automation_account_resource_group_name" { description = "resource group name of the automation account" }
variable "automation_account_sku_name" { 
  description = "sku_name of the automation account" 
  type        = string
  default = "Basic"
}
variable "automation_account_tags" { description = "sku_name of the automation account" }

variable "local_authentication_enabled" {
  description = "Should local authentication be enabled for this Automation account?"
  type        = bool
  default     = false
}

variable "public_network_access_enabled" {
  description = "Should public network access be enabled for this Automation account?"
  type        = bool
  default     = true
}

variable "system_assigned_identity_enabled" {
  description = "Should the system-assigned identity be enabled for this automation account?"
  type        = bool
  default     = false
}

variable "identity_ids" {
  description = "A list of IDs of managed identities to be assigned to this automation account."
  type        = list(string)
  default     = []
}

variable "python3_shared_packages" {
    description = "Shared python3 packages to be installed on this automation account"
    type = map
    default = {
      azure_identity = {
        content_uri = "https://files.pythonhosted.org/packages/49/83/a777861351e7b99e7c84ff3b36bab35e87b6e5d36e50b6905e148c696515/azure_identity-1.17.1-py3-none-any.whl"
        content_version = "1.17.1"
      }
      azure_common = {
        content_uri = "https://files.pythonhosted.org/packages/62/55/7f118b9c1b23ec15ca05d15a578d8207aa1706bc6f7c87218efffbbf875d/azure_common-1.1.28-py2.py3-none-any.whl"
        content_version = "1.1.28"
      }
    }
}