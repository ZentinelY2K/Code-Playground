logs = [
    "[12:00:01] INFO user=Axel ip=192.168.1.2",
    "[12:01:14] ERROR user=Chris ip=192.168.1.4",
    "[12:01:30] WARNING user=Axel ip=192.168.1.2",
    "[12:02:10] ERROR user=Axel ip=192.168.1.2",
    "[12:03:45] ERROR user=Axel ip=192.168.1.2",
    "[12:04:00] INFO user=Chris ip=10.0.0.5"
]
Info_counter = 0
Error_counter = 0
Warning_counter = 0
user = ""
most_errors_counter_Chris = 0
most_errors_counter_AXEL = 0
ips = []
ip = ""
for log in logs: #iterate through every item of list
    ip = log.split("ip=")[1].split(" ")[0]
    ips.append(ip)
    if "INFO" in log:
        Info_counter += 1
    elif "ERROR" in log:
        user = log.split("user=")[1].split(" ")[0]
        Error_counter += 1
        if user == "Chris":
            most_errors_counter_Chris += 1
        elif user == "Axel":
            most_errors_counter_AXEL += 1
    elif "WARNING" in log:
        Warning_counter += 1
    else: #no need for this but just to be sure
        continue
print("Log Levels:")
print(f"Info: {Info_counter}")
print(f"Error: {Error_counter}")
print(f"Warning: {Warning_counter}")
if most_errors_counter_Chris > most_errors_counter_AXEL:
    print(f"most errors is Chris, with a total of {most_errors_counter_Chris}")
elif  most_errors_counter_AXEL > most_errors_counter_Chris:
    print(f"most errors is Axel, with a total of {most_errors_counter_AXEL}")
