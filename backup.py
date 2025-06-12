import os
import shutil
import datetime
import schedule
import time

source_dir = "/Users/rahul/Desktop/Screenshots"
destination_dir = "/Users/rahul/Desktop/Projects/python/backup"

def creating_backup(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source,dest_dir)
        print(f"Folder copied to {dest_dir}")
    except FileExistsError:
        print(f"File already exists in {dest}")

schedule.every().day.at("23:21").do(lambda: creating_backup(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(5)