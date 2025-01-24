terraform {
  required_version = ">1.3.1"
  required_providers {
    azurerm = ">= 3.33.0"
  }
}

locals {
  # If system_assigned_identity_enabled is true, value is "SystemAssigned".
  # If identity_ids is non-empty, value is "UserAssigned".
  # If system_assigned_identity_enabled is true and identity_ids is non-empty, value is "SystemAssigned, UserAssigned".
  identity_type = join(", ", compact([var.system_assigned_identity_enabled ? "SystemAssigned" : "", length(var.identity_ids) > 0 ? "UserAssigned" : ""]))
}

#---------------------------------------
# Azure automation account
#---------------------------------------
resource "azurerm_automation_account" "instance" {
  name                = "${var.environment}-${var.applicationname}-${var.region_abbreviation}-${var.automation_account_name}"
  resource_group_name = var.automation_account_resource_group_name
  location            = var.automation_account_location
  sku_name            = var.automation_account_sku_name

  local_authentication_enabled  = var.local_authentication_enabled
  public_network_access_enabled = var.public_network_access_enabled

  dynamic "identity" {
    for_each = local.identity_type != "" ? [1] : []

    content {
      type         = local.identity_type
      identity_ids = var.identity_ids
    }
  }
  
  tags = var.automation_account_tags
}

# default set of python3 packages
resource "azurerm_automation_python3_package" "packages" {
  for_each = var.python3_shared_packages

  name                    = each.key
  resource_group_name     = var.automation_account_resource_group_name
  automation_account_name = azurerm_automation_account.instance.name
  content_uri             = each.value.content_uri
  content_version         = each.value.content_version
  tags                    = var.automation_account_tags
}