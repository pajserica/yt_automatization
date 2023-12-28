from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
from selenium.webdriver.common.by import By

save_path = "D:\\pyTikTube\\tiktoks\\football"
tk_page = "https://www.tiktok.com/search?q=football%20messi&t=1673280131736"

def downloadVideo(link, id):
    print(f"downloading video {id} ......")
    cookies = {
        '_ga': 'GA1.2.844603655.1672961386',
        '_gid': 'GA1.2.1045683313.1672961386',
        '_gat_UA-3524196-6': '1',
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': '_ga=GA1.2.844603655.1672961386; _gid=GA1.2.1045683313.1672961386; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'NDZuMTU2',
    }

    response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
    downloadSoup = BeautifulSoup(response.text, "html.parser")

    
    #print(downloadSoup.a["href"])
    if downloadSoup.a is not None:
        downloadLink = downloadSoup.a["href"]
    

        mp4File = urlopen(downloadLink)
        # Feel free to change the download directory
        with open(f"{save_path}/{id}.mp4", "wb") as output:
            while True:
                data = mp4File.read(4096)
                if data:
                    output.write(data)
                else:
                    break

driver = webdriver.Chrome()
# Change the tiktok link
driver.get(tk_page)

time.sleep(15)

scroll_pause_time = 1
screen_height = driver.execute_script("return window.screen.height;")
i = 1
j = 0
while j<5:
    #driver.find_element(By.XPATH,   f'//*[@id="app"]/div[3]/div[2]/div[2]/div[2]/button').click() 
    i += 1
    time.sleep(scroll_pause_time)
    driver.execute_script("window.scrollBy(0, 1000);")
    j += 1
    #if (screen_height) * i > scroll_height:
        #break 

soup = BeautifulSoup(driver.page_source, "html.parser")
# this class may change, so make sure to inspect the page and find the correct class
videos = soup.find_all("div", {"class": "tiktok-yz6ijl-DivWrapper"})

print(len(videos))
for index, video in enumerate(videos):
    if(index > 0):
        downloadVideo(video.a["href"], index)
        time.sleep(5)
        