# import psutil
# import re
# import time


# def monitor_cpu():
#     return psutil.cpu_percent(interval=1)

# # Function to query and filter logs
# def query_logs(log_file, pattern):
#     with open(log_file, 'r') as file:
#         logs = file.readlines()
#     filtered_logs = [log for log in logs if re.search(pattern, log)]
#     return filtered_logs

# # Function to calculate average from logs
# def calculate_average(logs):
#     try:
#         values = [float(log.split()[-1]) for log in logs]
#         return sum(values) / len(values)
#     except ZeroDivisionError:
#         print("Cannot divide by Zero...")
#         return 0  # Return 0 in case of division by zero

# # Main function
# def main():
#     cpu_usages = [] 
#     log_values = []

#     try:
#         while True:
#             cpu_usage = monitor_cpu()
#             cpu_usages.append(cpu_usage)
#             print(f"CPU Usage: {cpu_usage}%")

#             logs = query_logs('system.log', 'ERROR')
#             log_value = calculate_average(logs) 
#             log_values.append(log_value)
#             print(f"Average Log Value: {log_value}")

#             time.sleep(1)  # Sleep for 1 second

#     except KeyboardInterrupt:
#         print("\nMonitoring stopped by user.")

#         # Calculate and print average CPU usage
#         average_cpu = sum(cpu_usages) / len(cpu_usages)
#         print(f"Average CPU Usage: {average_cpu}%")

#         # Save CPU usage data (optional)
#         with open("cpu_usage.txt", "r") as f:
#             for usage in cpu_usages:
#                 f.write(str(usage) + "\n")

#         # Save log values (optional)
#         with open("log_values.txt", "r") as f:
#             for value in log_values:
#                 f.write(str(value) + "\n")

# if __name__ == "__main__":
#     main()


# import psutil
# import re
# import time

# def monitor_cpu():
#     return psutil.cpu_percent(interval=1)

# # Function to query and filter logs
# def query_logs(log_file, pattern):
#     with open(log_file, 'r') as file:
#         logs = file.readlines()
#     filtered_logs = [log for log in logs if re.search(pattern, log)]
#     return filtered_logs

# # Function to calculate average from logs
# def calculate_average(logs):
#     try:
#         values = [float(log.split()[-1]) for log in logs]
#         return sum(values) / len(values)
#     except ZeroDivisionError:
#         return 0  # Return 0 in case of division by zero

# # Main function
# def main():
#     cpu_usages = [] 
#     error_values = []
#     warning_values = []
#     info_values = []

#     try:
#         while True:
#             cpu_usage = monitor_cpu()
#             cpu_usages.append(cpu_usage)
#             print(f"CPU Usage: {cpu_usage}%")

#             error_logs = query_logs('system.log', 'ERROR')
#             error_avg = calculate_average(error_logs)
#             error_values.append(error_avg)
#             print(f"Average Error Value: {error_avg}")

#             warning_logs = query_logs('system.log', 'WARNING')
#             warning_avg = calculate_average(warning_logs)
#             warning_values.append(warning_avg)
#             print(f"Average Warning Value: {warning_avg}")

#             info_logs = query_logs('system.log', 'INFO')
#             info_avg = calculate_average(info_logs)
#             info_values.append(info_avg)
#             print(f"Average Info Value: {info_avg}")

#             time.sleep(1)  # Sleep for 1 second

#     except KeyboardInterrupt:
#         print("\nMonitoring stopped by user.")

#         # Calculate and print average CPU usage
#         average_cpu = sum(cpu_usages) / len(cpu_usages)
#         print(f"Average CPU Usage: {average_cpu}%")

#         # Save CPU usage data
#         with open("cpu_usage.txt", "w") as f:
#             for usage in cpu_usages:
#                 f.write(str(usage) + "\n")

#         # Save error values
#         with open("error_values.txt", "w") as f:
#             for value in error_values:
#                 f.write(str(value) + "\n")

#         # Save warning values
#         with open("warning_values.txt", "w") as f:
#             for value in warning_values:
#                 f.write(str(value) + "\n")

#         # Save info values
#         with open("info_values.txt", "w") as f:
#             for value in info_values:
#                 f.write(str(value) + "\n")

# if __name__ == "__main__":
#     main()



import psutil
import re
import time

def monitor_cpu():
    return psutil.cpu_percent(interval=1)

def query_logs(log_file, pattern):
    """Query logs to find lines matching a given pattern."""
    with open(log_file, 'r') as file:
        logs = file.readlines()
    return [log for log in logs if re.search(pattern, log)]

def calculate_average(logs):
    """Calculate the average from log entries."""
    try:
        values = [float(log.split()[-1]) for log in logs]
        return sum(values) / len(values)
    except ZeroDivisionError:
        return 0  # Return 0 in case of division by zero

def log_errors(log_file):
    """Query and calculate average for ERROR logs."""
    logs = query_logs(log_file, 'ERROR')
    return calculate_average(logs)

def log_warnings(log_file):
    """Query and calculate average for WARNING logs."""
    logs = query_logs(log_file, 'WARNING')
    return calculate_average(logs)

def log_info(log_file):
    """Query and calculate average for INFO logs."""
    logs = query_logs(log_file, 'INFO')
    return calculate_average(logs)

def save_to_file(filename, data):
    """Save data to a specified file."""
    with open(filename, "w") as f:
        for value in data:
            f.write(str(value) + "\n")

def main():
    cpu_usages = []
    error_values = []
    warning_values = []
    info_values = []

    try:
        while True:
            cpu_usage = monitor_cpu()
            cpu_usages.append(cpu_usage)
            print(f"CPU Usage: {cpu_usage}%")

            error_avg = log_errors('system.log')
            error_values.append(error_avg)
            print(f"Average Error Value: {error_avg}")

            warning_avg = log_warnings('system.log')
            warning_values.append(warning_avg)
            print(f"Average Warning Value: {warning_avg}")

            info_avg = log_info('system.log')
            info_values.append(info_avg)
            print(f"Average Info Value: {info_avg}")

            time.sleep(1)  # Sleep for 1 second

    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

        average_cpu = sum(cpu_usages) / len(cpu_usages)
        print(f"Average CPU Usage: {average_cpu}%")

        # Save data to files
        save_to_file("cpu_usage.txt", cpu_usages)
        save_to_file("error_values.txt", error_values)
        save_to_file("warning_values.txt", warning_values)
        save_to_file("info_values.txt", info_values)

if __name__ == "__main__":
    main()
