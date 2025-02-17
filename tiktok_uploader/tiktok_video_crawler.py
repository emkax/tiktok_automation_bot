from selenium import webdriver
import urllib
import toml
from bs4 import BeautifulSoup
from os.path import abspath, join, dirname

import os
import random
import time


src_dir = abspath(dirname(__file__))
print(src_dir)
path = os.path.join(src_dir,'config.toml') 
print(path)
with open(path, 'r') as f:
        config = toml.load(f)

def main():
    if config['platform'] == 'tiktok':
        crawler_tiktok()
    elif config['platform'] == 'douyin':
        crawler_douyin()
    else:
        print("pls configure a valid platform")

def get_cookies(path: str = None, cookies_str: str = None) -> dict:
    """
    Gets cookies from the passed file using the netscape standard
    """
    if path:
        with open(path, "r", encoding="utf-8") as file:
            lines = file.read().split("\n")
    else:
        lines = cookies_str.split("\n")

    return_cookies = []
    for line in lines:
        split = line.split('\t')
        if len(split) < 6:
            continue

        split = [x.strip() for x in split]

        try:
            split[4] = int(split[4])
        except ValueError:
            split[4] = None

        return_cookies.append({
            'name': split[5],
            'value': split[6],
            'domain': split[0],
            'path': split[2],
        })

        if split[4]:
            return_cookies[-1]['expiry'] = split[4]
    return return_cookies


def crawler_douyin():
    driver = webdriver.Chrome()


    print(config['crawler']['direct_douyin_link'])

    while 1:
        try:
            driver.get(config['crawler']['direct_douyin_link'])
            print('done')
            break
        except Exception as e:
            print(e)
            print("not succesful retying to connect to douyin's server") 

    time.sleep(5)

    video_links = []
    for i in range(config['crawler']['jumlah_stok_video']):
        while 1:
            try:
                next_element = driver.find_element('xpath',config['crawler']['next_video_douyin'])
                next_element.click()
                elem = driver.find_element('xpath',config['crawler']['direct_douyin_path'])
                inter_element = elem.get_attribute('innerHTML')
                soup = BeautifulSoup(inter_element, 'html.parser')
                
                sources = soup.find_all('source')

                video_urls = [source['src'] for source in sources if 'src' in source.attrs]

                video_links.append(video_urls[len(video_urls)-1])
                print(video_urls)
                print("------------------------------------------")
                time.sleep(5)
                break
            except Exception as e:
                print(e)
                xbutton = driver.find_element('xpath',config['crawler']['xbutton']) 
                xbutton.click()

    lower_bound = 10**(config['file_management']['video_name_length']-1)
    upper_bound = 10**config['file_management']['video_name_length'] - 1
    for video_link in video_links:
        randomed = random.randint(lower_bound, upper_bound)
        URL = 'https:' + video_link
        FILENAME = os.path.join("stok_video", f"{randomed}.mp4")

        print(FILENAME)
        request_url = urllib.request.urlretrieve(URL,FILENAME)
        print(request_url)
    current_url = driver.current_url
    config['crawler']['direct_douyin_link'] = current_url
    with open(path, 'w') as f:
        toml.dump(config, f)
    print(f"next chain = {current_url}")
    time.sleep(5)
    driver.quit()


###BETA
def crawler_tiktok():
    driver = webdriver.Chrome()


    print(config['crawler']['direct_tiktok_link'])
    cookies = get_cookies(path=".\\cookies\\cookie1.txt") 
    while 1:
        try:
            driver.get(config['crawler']['direct_tiktok_link'])
            for cookie in cookies:
                try:
                    print("adding cookie")
                    driver.add_cookie(cookie)
                except Exception as _:
                    print('Failed to add cookie')
            driver.get(config['crawler']['direct_tiktok_link'])
            print('done')
            break
        except Exception as e:
            print(e)
            print("not succesful retying to connect to tiktok's server") 

    time.sleep(10)


    video_links = []
    for i in range(config['crawler']['jumlah_stok_video']):
        while 1:
            try:
                next_element = driver.find_element('xpath',config['crawler']['next_video_tiktok'])
                next_element.click()
                time.sleep(10)
                elem = driver.find_element('xpath',config['crawler']['direct_tiktok_path'])
                inter_element = elem.get_attribute('innerHTML')
                soup = BeautifulSoup(inter_element, 'html.parser')

                sources = soup.find_all('source')

                video_urls = [source['src'] for source in sources if 'src' in source.attrs]

                video_links.append(video_urls[len(video_urls)-1])
                print(video_urls)
                print("------------------------------------------")
                time.sleep(5)
                break
            except Exception as e:
                print(e)
                xbutton = driver.find_element('xpath',config['crawler']['close_captcha']) 
                xbutton.click()

    lower_bound = 10**(config['file_management']['video_name_length']-1)
    upper_bound = 10**config['file_management']['video_name_length'] - 1
    for video_link in video_links:
        randomed = random.randint(lower_bound, upper_bound)
        URL = 'https:' + video_link
        FILENAME = os.path.join("stok_video", f"{randomed}.mp4")

        print(FILENAME)
        request_url = urllib.request.urlretrieve(URL,FILENAME)
        print(request_url)
    current_url = driver.current_url
    config['crawler']['direct_tiktok_link'] = current_url
    with open(path, 'w') as f:
        toml.dump(config, f)
    print(f"next chain = {current_url}")
    time.sleep(5)
    driver.quit()
