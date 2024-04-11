import os
import time
import shutil
import random
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
 
to_dir = "C:/Users/Shinj_28/OneDrive/Desktop/files"
from_dir = "C:/Users/Shinj_28/Downloads"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMomentHandler(FileSystemEventHandler):
        def on_created(self, event):
            name,ext = os.path.splitext(event.src_path)
            time.sleep(1)
           #path2=""
            for key , value in dir_tree.items():
                time.sleep(1)
                if ext in value:
                    file_name =os.path.basename(event.src_path)
                    print("downloaded..."+ file_name)
                    path1 = from_dir+'/'+file_name
                    path2 = to_dir +'/'+key
                    path3 = to_dir +'/'+key + '/' + file_name

                    time.sleep(1)
                    
                    if os.path.exists(path2):
                        print("Directory exists..")
                        time.sleep(1)
                        if os.path.exists(path3):
                            print("File already exists in " + key +"...")
                            print("Renaming file"+ file_name+"...")
                            new_file_name = os.path.splitext(file_name)[0]+str(random.randint(0,999))+os.path.splitext(file_name)[1]
                            path4 = to_dir +'/'+key + '/' + new_file_name
                            print("Moving" + new_file_name+"...")
                            shutil.move(path1,path4)
                            time.sleep(1)
                    else :
                        print("Moving" + file_name+"...")
                        shutil.move(path1,path3)
                        time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving"+file_name+"...")
                    shutil.move(path1,path3)
                    time.sleep(1)
            
event_handler= FileMomentHandler()
observer = Observer()
observer.schedule(event_handler, from_dir , recursive = True)
observer.start()

try : 
    while True :
        time.sleep(2)
        print("Running...")
except KeyboardInterrupt:
    print("Stopped...")
    observer.stop()
    