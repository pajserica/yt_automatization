import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

req_array = []

#read from requests.txt
with open(r"C:\Users\PAJSER-PC\Desktop\Test Programi\TOP_10\requests.txt", "r") as f:
    for line in f:
        req_array.append(line.split(".")[-1].strip())

request = req_array[0]
topic = req_array[1]
del req_array[0:2]

# Set the path to the Chrome driver executable
ser = Service(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

# Create Chrome options
chrome_options = webdriver.ChromeOptions()

# Add the argument to use the specified user data folder
chrome_options.add_argument(r"user-data-dir=C:\Users\PAJSER-PC\AppData\Local\Google\Chrome\User Data\Default")

# Create the Chrome driver
driver = webdriver.Chrome(service=ser, options=chrome_options)

j = 0
for req in req_array:
    # Find the search box element and enter the search text 
    driver.get("https://www.google.com/search?q=" + f"{req}+{topic}" + "&start=" + str(1))


    # Navigate to the Images tab
    driver.find_element(By.XPATH, '//*[contains(text(), "Images")]').click()
    #sleep(300)
    # Find the first image on the page
    driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[1]/a[1]').click()

    #sleep(300)
    # Get the source URL of the image
    
    for k in range(2, 22):
        image = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')
        try:
            sleep(1)
            # Download the image
            r = requests.get(image.get_attribute("src"))
            if r.status_code == 200:
                with open(f"TOP_10\\{j}. {str(req).strip()}.jpg", 'wb') as outfile: outfile.write(r.content)
                j+=1
            else:
                #sleep(100)
                print("else xpath!")
                driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{k}]/a[1]/div[1]/img').click()
                #image = driver.find_element(By.XPATH, '//*[@id="Sva75c"]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/a/img')
                continue
            break
        except:
            if k == 21:
                print("image yet not loaded")
                break
# Close the browser
driver.quit()
with open(r"C:\Users\PAJSER-PC\Desktop\Test Programi\TOP_10\requests.txt", "w") as f:
    f.write(f"{request}" + "\n")

