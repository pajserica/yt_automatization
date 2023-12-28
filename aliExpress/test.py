import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys


# Prompt user for folder name
folder_name = r"D:\pyTikTube\finalVideos\affiliate\aliExpress"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\PAJSER-PC\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Open Chrome browser
bot = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
# Navigate to YouTube Studio page
bot.get("https://studio.youtube.com")
time.sleep(3)

# Get a list of all the videos in the specified folder
video_files = os.listdir(folder_name)

# Iterate through the list of videos
for video_file in video_files:
    # Check if the file is a video
    if video_file.endswith('.mp4'):
        nameofvid = os.path.join(folder_name, video_file)

        # Click the upload button
        try:
            upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
            upload_button.click()
            time.sleep(1)
        except NoSuchElementException:
            print("Unable to locate upload button. Make sure page has fully loaded.")

        # Select the video file
        try:
            file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
            file_input.send_keys(nameofvid)
        except NoSuchElementException:
            print("Unable to locate file input. Make sure page has fully loaded.")

        # Click through subsequent screens
        time.sleep(7)
        try:
            bot.find_element(By.ID, "textbox").send_keys(f"{video_file[:-4]}")
            next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
            for i in range(3):
                next_button.click()
                time.sleep(1)
        except NoSuchElementException:
            print("Unable to locate next button. Make sure page has fully loaded.")

        # Click the "done" button to complete the upload process
        try:
            done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
            done_button.click()
            time.sleep(7)
            #os.remove(nameofvid)
        except NoSuchElementException:
            print("Unable to locate done button. Make sure page has fully loaded.")
        
         # Click the "cancel" button to complete the upload process
        try:
            time.sleep(1)
            close_btn = bot.find_element(By.XPATH, '/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/ytcp-button/div')
            time.sleep(1)
            close_btn.click()
            #close_btn.click()
            time.sleep(1)
            #os.remove(nameofvid)
        except NoSuchElementException:
            print("Unable to locate done button. Make sure page has fully loaded.")
# Close the browser"""
bot.quit()
