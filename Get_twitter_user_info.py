# import libraries
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from getpass import getpass

url = 'https://twitter.com/sachin_rt/likes'
driver = webdriver.Chrome('./chromedriver_win32103/chromedriver')

SampleOP={}
def Twitterscraper(url):
    driver.get(url)
    time.sleep(2)
    #gather user information
    username=driver.find_elements("xpath","//*[@data-testid='UserName']/div/div//span")
    utaddress=driver.find_elements("xpath","//*[@data-testid='UserName']/div/div/div[2]//span")
    bio=driver.find_elements("xpath","//*[@data-testid='UserDescription']//span")
    following=driver.find_elements("xpath","//*[@data-testid='primaryColumn']/div/div[2]/div/div/div/div/div[5]//span/span")
    followers=driver.find_elements("xpath","//*[@data-testid='primaryColumn']/div/div[2]/div/div/div/div/div[5]/div[2]//span/span")
    likes=driver.find_elements("xpath","//*[@data-testid='primaryColumn']/div/div/div/div/div/div/div/div[2]/div/div")
    #add in Dictionary 
    SampleOP["User Name"]=username[0].text
    SampleOP["Biography"]=bio[0].text
    SampleOP["Twiter Handler"]=utaddress[0].text
    SampleOP["Following"]=following[0].text
    SampleOP["Followers"]=followers[0].text
    SampleOP["Likes"]=likes[0].text
    print(SampleOP)
    return SampleOP

#user login this login part is for only retriving the likes of users other than no use

loginurl="https://twitter.com/i/flow/login"

# application variables
#for automatic login
##user='username'
##my_password='password'
#Manual Login
user = input('\nusername:')
my_password = getpass('Password:')

# navigate to login screen
driver.get(loginurl)
driver.maximize_window()
time.sleep(5)
#send username
username = driver.find_element("xpath",'//input[@name="text"]')
username.send_keys(user)
username.send_keys(Keys.RETURN)
time.sleep(3)
#send password
password = driver.find_element("xpath","//input[@type='password']")
password.send_keys(my_password)
password.send_keys(Keys.RETURN)

time.sleep(2)
#now goto fuction and fetch user data and 
Twitterscraper(url)
