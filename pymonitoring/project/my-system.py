import psutil
import re

# monitoring cpu
def monitor_cpu():
    return psutil.cpu_percent(interval=1)


# Function to query and filter logs
def query_logs(log_file, pattern):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    filtered_logs = [log for log in logs if re.search(pattern, log)]
    return filtered_logs


# Function to calculate average from logs
def calculate_average(logs):
    try:  
        values = [float(log.split()[-1]) for log in logs]
        return sum(values) / len(values)
    except ZeroDivisionError as err:
        print("Cannot divide by Zero...")


# Example usage
cpu_usage = monitor_cpu()
print(f"CPU Usage: {cpu_usage}%")

logs = query_logs('system.log', 'ERROR')
average = calculate_average(logs)
print(f"Average Log Value: {average}")

