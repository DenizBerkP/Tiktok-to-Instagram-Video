from instagrapi import Client
import datetime, time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import os
import glob


# txt File containing the links you want to share on Instagram Reels
with open('links.txt', 'r') as file:
    links = [line.strip() for line in file]

# Login Instagram
client = Client() 
client.login("InstagramUserName", "InstagramPassword")

i = 0
shared = 0

share_Hours = [12, 14, 16, 18] # Hours you want to share
now = datetime.datetime.now()
while True:
    if now.hour in share_Hours and shared == 0:
        driver = webdriver.Chrome()
        shared = 1
        downloadsPath = "C:/Users/Administrator/Downloads" # Downloads folder path on your computer
        mp4Files = glob.glob(os.path.join(downloadsPath, "*.mp4"))
        for file in mp4Files:
            try:
                os.remove(file)
            except Exception as e:
                pass
                
        pyperclip.copy(links[i])
        driver.get("https://ssstik.io/tr")
        
        linkPaste = driver.find_element(By.XPATH, '//*[@id="main_page_text"]')
        linkPaste.send_keys(pyperclip.paste())
        
        driver.find_element(By.XPATH, '//*[@id="submit"]').click()
        
        time.sleep(10)
        
        if driver.find_element(By.XPATH, '//*[@id="hd_download"]'):
            driver.find_element(By.XPATH, '//*[@id="hd_download"]').click()
        
        elif driver.find_element(By.XPATH, '//*[@id="dl_btns"]/a[1]'):
            driver.find_element(By.XPATH, '//*[@id="dl_btns"]/a[1]').click()
        
        time.sleep(60)
        
        try:
            videoPath = mp4Files[0]
        except:
            videoPath = mp4Files

        cover_path = 'Cover.jpg'  # Thumbnail (Optional)
        caption = 'Credit: .....' # Caption
        client.clip_upload(video_path, caption, cover_path)
        
        print(now, "Shared.")
        driver.exit()
    elif not now.hour in share_Hours:
        shared = 0
        time.sleep(900)
