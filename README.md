# TikTok Automation Bot

## Overview
The **TikTok Automation Bot** is a Python-based tool that automatically downloads videos from a specified category from Douyin / Tiktok by a starting category link and uploads them to multiple TikTok account. This bot helps maintain a consistent posting schedule with minimal effort.

## Features
- ✅ **Automated Video Download**: Fetches videos from sources like YouTube, Instagram, or direct URLs.
- 🚀 **Auto Upload to TikTok**: Uses Selenium to log in and post videos automatically via given cookie.
- 👥 **Multi Account Support**: Utilizes given cookies to switch between accounts.
- ⏳ **Scheduled Posting**: Supports scheduling future uploads.
- 🕶 **Headless Mode**: Runs in the background without a visible browser window.
- 📋 **Logging & Error Handling**: Keeps track of successes and failures.

## Requirements
Ensure you have the following installed:

```sh
curl -O https://raw.githubusercontent.com/emkax/tiktok_automation_bot/requirements.txt

pip install -r ./requirements.txt
```
## How To Use
# 🏃 Run
```
python base.py
```
# 📅 Schedule Upload
set the time to upload e.g {1..24}
```
[schedule]
upload_time = [ 9, 15, 19, 12,22]
```

# ✍️ Set Description
set the description parameter
```
upload_video(full_path,
            description="",
            cookies=cookie)
```
# 📂 Set Video Supply
```
jumlah_stok_video = 6
```

# 🍪 Add Account/Cookie
to add more account add the netscape cookie format and put it in a new file with the next number of the previous cookie in the cookies directory e.g. cookie1,cookie2,cookie3,..

# Adding Video category
you can access these settings in the config.toml file
```
#douyin platform
direct_douyin_link = "video-link-goes-here"

#tiktok platform
direct_tiktok_link = "video-link-goes-here"
```
example

```
direct_douyin_link = "https://www.douyin.com/video/7470498918543936804"
```
the setting above has a video about cosplayer so the program automaticly downloads videos of that kind by utilizing the douyin recommendation system 

```
direct_tiktok = "https://www.tiktok.com/@malgbaisi_/video/7460533837437619464?q=techtok&t=1739799180710"
```
the setting above has a video about techtok so the program automaticly downloads videos of that kind by utilizing tiktok recommendation system
