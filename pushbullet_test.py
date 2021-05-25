from pushbullet import Pushbullet
from os import path
api_key = 'o.KQ4eSi8fZz6ym65RT16UyeVRaKq1rslv'
pb = Pushbullet(api_key)
# Pushing notification to user's phone:
pb.push_note("WARNING: FIRE WAS DETECTED","")
# Pushing link to user's phone:
# pb.push_link("Cool site", "https://github.com/yassinechaouch/S4G4")
# Pushing file to user's phone:
with open("assets/logs_example.txt", "rb") as log:
    file_data = pb.upload_file(log, "logs.txt")
push = pb.push_file(**file_data)
# To delete pushes (all information sent) from user's phone:
# pb.delete_pushes()
# Or if file is already uploaded, then directly use pb.push.file(file url, file name, file type)
# push = pb.push_file(file_url="https://i.imgur.com/IAYZ20i.jpg", file_name="cat.jpg", file_type="image/jpeg")