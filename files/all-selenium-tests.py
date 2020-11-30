#! /usr/bin/env python
import jinja2
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

ip0 = sys.argv[1]
ip1 = sys.argv[2]
ip2 = sys.argv[3]
ip3 = sys.argv[4]
zc_ip = sys.argv[5]

# login
def login():
    driver.get("https://"+zc_ip+"/login.html")
    driver.set_window_size(1440, 877)
    driver.find_element(By.ID, "login").click()

# assign syslog server
def syslog_config():
    driver.get("https://"+zc_ip+"/diagnostics/event_log.html")
    element = driver.find_element(By.NAME, "syslog_host0")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.NAME, "enable_syslog").click()
#     driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) input:nth-child(2)").click()
    driver.find_element(By.NAME, "syslog_host0").click()
    driver.find_element(By.NAME, "syslog_host0").send_keys(ip0)
    driver.find_element(By.NAME, "syslog_host1").click()
    driver.find_element(By.NAME, "syslog_host1").send_keys(ip1)
    driver.find_element(By.NAME, "syslog_host2").click()
    driver.find_element(By.NAME, "syslog_host2").send_keys(ip2)
    driver.find_element(By.NAME, "syslog_host3").click()
    driver.find_element(By.NAME, "syslog_host3").send_keys(ip3)
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) input:nth-child(2)").click()
    driver.find_element(By.NAME, "continue_button").click()

# disable syslog - used for initial testing of script only
def syslog_disable():
    driver.get("https://"+zc_ip+"/diagnostics/event_log.html")
    element = driver.find_element(By.NAME, "syslog_host0")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.NAME, "enable_syslog").click()
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) input:nth-child(2)").click()
    driver.find_element(By.NAME, "continue_button").click()

# enable and configure ntp
def ntp_enable():
    driver.get("https://"+zc_ip+"/configuration/time.html")
    driver.find_element(By.NAME, "enable_ntp").click()
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) input:nth-child(2)").click()
    driver.find_element(By.NAME, "ntp_dns_name").click()
    driver.find_element(By.NAME, "ntp_dns_name").send_keys("pool.ntp.org")
    driver.find_element(By.ID, "time_zone_offset").click()
    dropdown = driver.find_element(By.ID, "time_zone_offset")
    dropdown.find_element(By.XPATH, "//option[. = '(UTC-8:00) America/Vancouver']").click()
    driver.find_element(By.CSS_SELECTOR, "tr:nth-child(14) input:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, "#continue_button > table").click()
    driver.find_element(By.CSS_SELECTOR, "#continue_button > table").click()
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
    syslog_config()
    ntp_enable()
    ntp_disable()
#     syslog_disable()
    logout()

main()