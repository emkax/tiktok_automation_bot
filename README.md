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
