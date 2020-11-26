#! /usr/bin/env python
import pytest
import time
import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.options import Options

#global vars for all functions

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(chrome_options=chrome_options)

# login
def login():
    driver.get("https://192.168.0.108/login.html")
    driver.set_window_size(1440, 877)
    driver.find_element(By.ID, "login").click()

# disable syslog - used for initial testing of script only
def syslog_disable():
    driver.get("https://192.168.0.108/diagnostics/event_log.html")
    element = driver.find_element(By.NAME, "syslog_host0")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.NAME, "enable_syslog").click()
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) input:nth-child(2)").click()
    driver.find_element(By.NAME, "continue_button").click()

# disable ntp
def ntp_disable():
    driver.find_element(By.NAME, "enable_ntp").click()
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(14) input:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#continue_button > table").click()
    driver.find_element(By.CSS_SELECTOR, "#continue_button > table").click()
    driver.find_element(By.NAME, "continue_button").click()

# logout
def logout():
    driver.find_element(By.LINK_TEXT, "Log Out").click()
    driver.close()

def main():
    login()
#     ntp_disable()
    syslog_disable()
    logout()

main()