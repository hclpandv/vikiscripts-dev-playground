#--------------------
# Sample TF template
#--------------------
variable "autostopstart_timezone" {
   default = "Pacific/Auckland"
}

locals {
  current_time              = timestamp()
  today                     = formatdate("YYYY-MM-DD", local.current_time) # 2022-10-04 19:00
  tomorrow                  = formatdate("YYYY-MM-DD", timeadd(local.current_time, "24h")) # 2022-10-05 19:00
  timeout_mins              = "30m"
}


output "locals" {
  value = {
    "current_time"           = local.current_time, # 2021-04-20T04:12:00Z,
    "today"                  = local.today
    "tomorrow"               = local.tomorrow, # 21/04/2021,
    "timeout_mins"           = local.timeout_mins
    "autostopstart_timezone" = var.autostopstart_timezone
    }
}
