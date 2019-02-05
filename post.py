#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os, time, getpass

#driver = webdriver.Firefox(options=options) #headless
driver = webdriver.Firefox()

# Acessa a página de login do Facebook
driver.get('https://mbasic.facebook.com')

# Encontrar elemento do campo de e-mail pelo atributo
email = driver.find_element_by_name("email")

# Digita o e-mail no campo de e-mail pelo atributo
email.send_keys('CHANGEEMAIL')

# Encontrar elemento do campo de senha pelo atributo
senha = driver.find_element_by_name("pass")

# Digita a senha no campo de senha pelo atributo
senha.send_keys('CHANGEPASSWORD')

# Simular que o enter seja precisonado
senha = driver.find_element_by_name("pass").send_keys(Keys.ENTER)

# Espera 5 segundos
time.sleep(5)

driver.get("https://www.facebook.com/CHANGEPAGE/?ref=dbl")

#wait page loads, maybe more time
time.sleep(10)

#select element
#inputText = driver.find_element_by_xpath("//div[@class='_1mf _1mj']")

inputText = driver.find_element_by_xpath("//html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/span/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div")

#click to enter text
inputText.click()

#select div to say goodbye
divToRemove = driver.find_element_by_xpath("//html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/span/div/div[2]/div/div/div/div/div/div/div[1]")

#bye div
driver.execute_script("arguments[0].remove()", divToRemove)

#select span
inputText = driver.find_element_by_xpath("//html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/span/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/span")


#set text
driver.execute_script("arguments[0].innerHTML = '<span data-text="'true'">teste</span>'", inputText)


publish = driver.find_element_by_xpath("//html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div/div[2]/div/span[3]/div/button")

driver.execute_script("console.log(arguments[0].classList)", publish)


#_42fr need to remove this class from button - @todo


#inputText = driver.find_element_by_xpath("//div[@class='_1mf _1mj']/span")


#driver.execute_script("document.getElementsByClassName('_1mf _1mj').innerText = 'test'", element)


