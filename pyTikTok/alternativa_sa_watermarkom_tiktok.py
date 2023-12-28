import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests

# Set the minimum number of views
min_views = 15000000
i = 0
# Set the URL for the TikTok trending page
url = "https://www.tiktok.com/search?q=trending&t=1672962424606"

# Use Selenium to load the page
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Get the HTML source
html = driver.page_source

# Close the browser
driver.close()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the video elements
videos = soup.find_all("div", class_="tiktok-yz6ijl-DivWrapper")

print(f'haloooooooooOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO {videos}')

def downloadTT(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)

    time.sleep(2)

    html = driver.page_source

    # Close the browser
    driver.close()

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    
    # Find the video element
    video = soup.find("video")

    # Download the video

    video_data = requests.get(video["src"], stream=True).content

    return video_data

def convert_string_to_int(string):
    # Strip off any leading or trailing whitespace
    string = string.strip()

    # Check if the string ends with 'K'
    if string.endswith("K"):
        # If it does, remove the 'K' and multiply by 1000
        value = int(float(string[:-1]) * 1000)
    elif string.endswith("M"):
        value = int(float(string[:-1]) * 1000000)
    else:
        # If it does not, try to convert it directly to an integer
        value = int(string)

    return value

# Download each video
for video in videos:
    """    # Check the number of viewsx
    soupp = BeautifulSoup(str(video), "html.parser")
    strong_element = soupp.find("strong")
    text = str(strong_element)
    #print(f'viewCount: {text}')
    view_count = convert_string_to_int(text)
    if view_count < min_views:
        continue
    """
    # Get the video URL
    url = video.a["href"]
    
    video_data = downloadTT(url)

    # Save the video to a file
    filename = f"{i}.mp4"
    save_path = r"D:\\pyTikTube\\tiktoks\\shortFails"
    with open(os.path.join(save_path, filename), "wb") as f:
        f.write(video_data)
    print(f"Downloaded {filename} to {save_path}")

    i = i + 1

print("All videos downloaded!")
