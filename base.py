from tiktok_uploader.upload import upload_video

from datetime import datetime

from tiktok_uploader.tiktok_video_crawler import main

import os 


from datetime import datetime

import toml

from os.path import abspath, join, dirname

import time


print('''
▓█████▄  ▒█████   █    ██▓██   ██▓ ▄▄▄       ███▄    █    ▓█████▄  ▒█████   █    ██▓██   ██▓ ██▓ ███▄    █ 
▒██▀ ██▌▒██▒  ██▒ ██  ▓██▒▒██  ██▒▒████▄     ██ ▀█   █    ▒██▀ ██▌▒██▒  ██▒ ██  ▓██▒▒██  ██▒▓██▒ ██ ▀█   █ 
░██   █▌▒██░  ██▒▓██  ▒██░ ▒██ ██░▒██  ▀█▄  ▓██  ▀█ ██▒   ░██   █▌▒██░  ██▒▓██  ▒██░ ▒██ ██░▒██▒▓██  ▀█ ██▒
░▓█▄   ▌▒██   ██░▓▓█  ░██░ ░ ▐██▓░░██▄▄▄▄██ ▓██▒  ▐▌██▒   ░▓█▄   ▌▒██   ██░▓▓█  ░██░ ░ ▐██▓░░██░▓██▒  ▐▌██▒
░▒████▓ ░ ████▓▒░▒▒█████▓  ░ ██▒▓░ ▓█   ▓██▒▒██░   ▓██░   ░▒████▓ ░ ████▓▒░▒▒█████▓  ░ ██▒▓░░██░▒██░   ▓██░
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ██▒▒▒  ▒▒   ▓▒█░░ ▒░   ▒ ▒     ▒▒▓  ▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒   ██▒▒▒ ░▓  ░ ▒░   ▒ ▒ 
 ░ ▒  ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ▓██ ░▒░   ▒   ▒▒ ░░ ░░   ░ ▒░    ░ ▒  ▒   ░ ▒ ▒░ ░░▒░ ░ ░ ▓██ ░▒░  ▒ ░░ ░░   ░ ▒░
 ░ ░  ░ ░ ░ ░ ▒   ░░░ ░ ░ ▒ ▒ ░░    ░   ▒      ░   ░ ░     ░ ░  ░ ░ ░ ░ ▒   ░░░ ░ ░ ▒ ▒ ░░   ▒ ░   ░   ░ ░ 
   ░        ░ ░     ░     ░ ░           ░  ░         ░       ░        ░ ░     ░     ░ ░      ░           ░ 
 ░                        ░ ░                              ░                        ░ ░                    
                    
''')


directory_path = os.path.join(os.getcwd(), "stok_video")

if len(os.listdir(directory_path)) == 0:
    main()

src_dir = abspath(dirname(__file__))
print(src_dir)
path = os.path.join(os.path.join(src_dir,'tiktok_uploader'),'config.toml') 
print(path)

with open(path, 'r') as f:
    config = toml.load(f)

def single_upload():

    directory_path = ".\\stok_video"
    print(os.getcwd() + "\\cookies.txt")

    for i in range(len(os.listdir(".\\cookies"))):
        if len(os.listdir(directory_path)) <= len(os.listdir(".\\cookies")):
            main()
        list_of_videos = os.listdir(directory_path)
        video = list_of_videos[i]
        full_path = os.path.join(directory_path,video)
        upload_video(full_path,
                    description="",
                    cookies=os.getcwd() + f".\\cookies\\cookie{i+1}.txt")

        if os.path.exists(full_path): 
            os.remove(full_path)  

while True:
    print("PLS select a function")

    print("[1] Upload Video \t\t [3] Monitor Account")
    print("[2] Remove Video Stock \n")
    print("[4] exit\n")

    menu_option = int(input())

    match menu_option:
        case 1:
            while True:
                if len(os.listdir(directory_path)) == 0:
                    main()
                c = datetime.now()

                current_hour = int(c.strftime('%H'))
                current_minute = int(c.strftime('%M'))
                if current_hour+1 in config['schedule']['upload_time'] and current_minute in range(40,60) or current_hour in config['schedule']['upload_time'] or current_minute in range(0,20):
                    print("it works yall")
                    single_upload()
                    time.sleep(3600)
            pass
        case 2:
            for i in os.listdir(directory_path):
                os.remove(i)
        case 3:
            pass
        case 4:
            break
        case _:
            pass