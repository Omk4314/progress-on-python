import re
ip_re = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*(\[\d{2}/[a-z^hikwxz]{3}/\d{4}:\d{2}:\d{2}:\d{2} [+-]{1}\d{4}\])"
with open("access.log") as log_file:
    contents = log_file.read()
match = re.findall(ip_re, contents, re.IGNORECASE)
for required_value in match:
    print(f"IP address: {required_value[0]} | Timestamp: {required_value[1]}")