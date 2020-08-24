from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import requests
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(r"C:\chromedriver")
x=0
driver.get("https://www.flipkart.com")

content = driver.page_source
soup =BeautifulSoup(content,features="html.parser")
for a in soup.findAll('a',href=True):
        if a.img:
            try :
                url =a.img['src']
                r = requests.get(url)
                x+=1
                f=open("%s.jpg"%x,'wb')
                f.write(r.content)


            except Exception:
                continue
print(x)
