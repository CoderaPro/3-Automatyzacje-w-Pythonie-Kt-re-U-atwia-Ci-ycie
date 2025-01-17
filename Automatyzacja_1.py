import os
import time
import shutil


def move_files_by_date(folder_path):

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            ctime = os.path.getctime(file_path)
            ctime_gmt = time.gmtime(ctime)

            year = ctime_gmt.tm_year
            month = ctime_gmt.tm_mon
            dest_folder = os.path.join(folder_path, str(year), str(month))

            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, file))


folder_path = "C:/automations_video"

if os.path.exists(folder_path):
    move_files_by_date(folder_path)
else:
    print(f"The folder path {folder_path} does not exist.")
