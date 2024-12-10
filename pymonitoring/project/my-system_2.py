import psutil
import re
import time
import logging

# Logging configs
logging.basicConfig(filename='system_2.log', 
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s')

# Monitoring CPU and memory usage
def monitor_resources(cpu_threshold=80, memory_threshold=80):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    
    if cpu_usage > cpu_threshold:
        logging.warning(f"High CPU usage detected: {cpu_usage}% b \
            \n please check system.")
    if memory_usage > memory_threshold: 
        logging.warning(f"High Memory usage detected: {memory_usage}% \
                        \n please check system.")
    return cpu_usage, memory_usage


# Function to calculate average from logs
def calculate_average(logs):
    try:
        values = [float(log.split()[-1]) for log in logs]
        return sum(values) / len(values)
    except (ZeroDivisionError, ValueError, IndexError) as err:
        print("Cannot divide by Zero.")
        return None
    
    
# Function to query and filter logs
def query_logs(log_file, pattern):
    with open(log_file, 'r') as file:
        logs = file.readlines()
    filtered_logs = [log for log in logs if re.search(pattern, log)]
    return filtered_logs

# Main to run the program
def main():
    try:
        while True:
            cpu_usage, memory_usage = monitor_resources()
            print(f"CPU Usage: {cpu_usage}%, \nMemory Usage: {memory_usage}%")
            
            # Check logs for warnings and errors
            warning_logs = query_logs('system_2.log', 'WARNING')
            error_logs = query_logs('system_2.log', 'ERROR')
            
            if warning_logs:
                avg_warning = calculate_average(warning_logs)
                print(f"Average Warning Log Value: {avg_warning}")
                
            if error_logs:
                avg_error = calculate_average(error_logs)
                print(f"Average Error Log Value: {avg_error}")
            
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program terminated gracefully...")
            
if __name__ == "__main__":
    main()