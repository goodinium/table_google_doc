# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
def main():
    url = 'https://confluence.hflabs.ru/pages/viewpage.action?pageId=1181220999'
    page = requests.get(url)
    page1=requests.get(url).content
    filtered = []
    tdd = []
    soup = BeautifulSoup(page.text, "html.parser")
    tdd = soup.findAll('td', class_='confluenceTd')
    for data in tdd:
        filtered.append(data.text)
        d=data.text
        print(data.text)
    doc(d,filtered)
def doc(d,filtered):
    url2="https://docs.google.com/document/d/1krhe-1NR4zLwQaFDZ-sRPARNNEHQwdB41TlllTmjDuc/edit"
    brow=webdriver.Firefox()
    brow.get(url=url2)
    zz=brow.find_element(By.XPATH, "//body")
    zz.send_keys(Keys.CONTROL + 'a')
    zz.send_keys(Keys.DELETE)
    vv=brow.find_element(By.XPATH, "/html/body/div[2]/div[4]/div[1]/div[1]/div[4]")
    vv.click()
    sleep(1)
    vv=brow.find_element(By.XPATH, "/html/body/div[12]/div[2]/div/span[1]")
    vv.click()
    vv=brow.find_element(By.XPATH, "/html/body/div[53]/div[3]/div[1]/div[3]")
    vv.click()
    sleep(1)
    go(d,zz,filtered)
def go(d,zz,filtered):
    i=0
    for d in filtered:
        print(d)
        sleep(1)
        # zz.clear()
        sleep(1)
        if i!=0:
            zz.send_keys(Keys.TAB)
        zz.send_keys(d + Keys.RETURN)
        i=i+1
main()