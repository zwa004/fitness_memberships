from cgitb import html
import requests 
from bs4 import BeautifulSoup
import config
import selenium 

PATH = 'C:\Program Files (x86)\chromedriver.exe'

loginurl = ('https://www.clubready.com/Security/Login')
dash_url = ('https://app.clubready.com/Dashboard/MainDashboard')

payload = {
    'uid': config.uid,
    'pw': config.pw,
    'Submit': 'Login',
    'inst': 1,
    'subdom': '',
    'loginTo': '',
    'storeID': '',
    'chainId': 773,
    'lostemail': ''
}

with requests.session() as s:
    s.post(loginurl, data=payload)
    r = s.get(dash_url)
    soup = BeautifulSoup(r.content, 'html.parser')
    tags = soup.find_all("a")
    print(tags)
