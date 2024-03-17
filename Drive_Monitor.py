import psutil # Requires psutil 'pip install psutil'
import time

def monitor_disk_performance(interval=1):
    last_read_count = psutil.disk_io_counters().read_bytes
    last_write_count = psutil.disk_io_counters().write_bytes
    
    while True:
        current_read_count = psutil.disk_io_counters().read_bytes
        current_write_count = psutil.disk_io_counters().write_bytes
        
        read_speed = (current_read_count - last_read_count) / (1024 * 1024 * interval)  # Convert bytes to MB/s
        write_speed = (current_write_count - last_write_count) / (1024 * 1024 * interval)  # Convert bytes to MB/s

        print(f"Read Speed: {read_speed:.2f} MB/s\t Write Speed: {write_speed:.2f} MB/s")

        last_read_count = current_read_count
        last_write_count = current_write_count

        time.sleep(interval)

if __name__ == "__main__":
    monitor_disk_performance()