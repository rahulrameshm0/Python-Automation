from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time


website = "https://www.thesun.co.uk/sport/football/"
path = "/Users/rahul/Downloads/chromedriver-mac-arm64/chromedriver"

#Headless Mode
options = Options()
options.add_argument("--headless")

service = Service(executable_path=path)
drive = webdriver.Chrome(service=service, options=options)

drive.get(website)
time.sleep(5)  # wait 5 seconds for the page to fully load

containers = drive.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    try:
        title = container.find_element(by="xpath", value='./a/h3').text
        subtitle = container.find_element(by="xpath", value='./a/p').text
        link = container.find_element(by="xpath", value='./a').get_attribute('href')

#     Append each item
        titles.append(title)
        subtitles.append(subtitle)
        links.append(link)
    except:
        continue
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}

headlines = pd.DataFrame(my_dict)
headlines.to_csv('headless.csv', index=False)
drive.quit()



# //div[@class="teaser__copy-container"]/a/h3
