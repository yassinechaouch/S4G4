from datetime import datetime
from os import path
import ip_locator
from pushbullet import Pushbullet


def add_line_to_file(current_time, duration):
    ip = ip_locator.find_ip()
    location = ip_locator.my_ip_location(ip)
    if path.exists("assets/fire_logs.txt"):
        logs = open("assets/fire_logs.txt", "a+")
        logs.write(location + "  |  " + "Current Time =" + current_time + "  |  " + "Duration = " + str(duration) + "\n")
    else:
        logs = open("assets/fire_logs.txt", "w+")
        logs.write(location + "  |  " + "Current Time =" + current_time + "  |  " + "Duration = " + str(duration) + "\n")

def send_file(pb):
    with open("assets/fire_logs.txt", "rb") as log:
        file_data = pb.upload_file(log, "fire_logs.txt")
        pb.push_file(**file_data)


# begin = time.time()
# end = time.time()
# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
duration = 12
add_line_to_file(dt_string,duration)