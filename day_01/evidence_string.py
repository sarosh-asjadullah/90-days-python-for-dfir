protocol = "HTTPS"
port = 443
status = "Malicious"

alert_message = f"ALERT : {protocol} traffic on port {port} is {status}"
print(alert_message)
