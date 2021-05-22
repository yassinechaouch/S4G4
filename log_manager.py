from os import path


def add_line_to_file(current_time,duration):
    if path.exists("assets/fire_logs.txt"):
        # now = datetime.now()
        # current_time = now.strftime("%H:%M:%S")
        logs = open("assets/fire_logs.txt", "a+")
        logs.write("Current Time =" + current_time + "  |  Location: Medtech  |  " + "Duration = " + duration)
    else:
        logs = open("assets/fire_logs.txt", "w+")
        logs.write("Current Time =" + current_time + "  |  Location: Medtech  |  " + "Duration = " + duration)

