import requests
from selenium import webdriver
from lxml import html
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service
import os 

save_path = r"D:\pyTikTube\aliExpress"

ali_link = r'https://www.aliexpress.com/af/gadgets-technology-men.html?spm=a2g0o.productlist.1000002.0&initiative_id=AS_20230111005448&dida=y&origin=n'

# Set the path to the Chrome driver executable
ser = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

# Create Chrome options
chrome_options = webdriver.ChromeOptions()

# Add the argument to use the specified user data folder
chrome_options.add_argument(r"user-data-dir=C:\Users\PAJSER-PC\AppData\Local\Google\Chrome\User Data\Default")

# Create the Chrome driver
driver = webdriver.Chrome(service=ser, options=chrome_options)
print("getting...")
driver.get(ali_link)
sleep(2)
for k in range(0, 10):
    # Scroll down by 1000 pixels
    driver.execute_script("window.scrollBy(0, 1000);")
    sleep(1)


i = 1

for i in range(1, 500):
    try:
        driver.find_element(By.XPATH,   f'//*[@id="root"]/div/div/div[2]/div/div[2]/div[3]/a[{i}]').click()
        print(i)
        i += 1
    except:
        print("break")
        break

num = 1

while num<=10 and i > 0:
    #print(i)
    sleep(2)
    driver.switch_to.window(driver.window_handles[i-1])
    try:
        video = driver.find_element(By.XPATH,   f'//*[@id="item-video"]') 
        product_name = driver.find_element(By.XPATH, f"//h1[1]").get_attribute("innerHTML")
        video_link = video.get_attribute("src")
        print(f'video link: {video_link}')
        video_data = requests.get(video_link, stream=True).content

        filename = f"{product_name}.mp4"
        with open(os.path.join(save_path, filename), "wb") as f:
            f.write(video_data)
            print(f"Downloaded {filename} to {save_path}")
        num+=1
        
    except:
        print("there is no video")
        #driver.close()
    i -= 1


driver.quit()