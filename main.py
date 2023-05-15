import random
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from selenium.webdriver.support.wait import WebDriverWait
# import pyrobot

def start_chrom():
    chrome_option = webdriver.ChromeOptions()
    # chrome_option.add_argument('--incognito')
    chrome_option.add_experimental_option("detach", True)
    driver_path = "C:\Drivers\chromedriver.exe"
    service = Service(executable_path=driver_path)
    service.start()

    driver = webdriver.Chrome(service=service, options=chrome_option)
    driver.get("https://www.google.com/drive/")
    time.sleep(5)
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT, "Sign in").click()
    new_window = driver.window_handles[-1]
    driver.switch_to.window(new_window)
    driver.find_element(By.ID, "identifierId").click()
    driver.find_element(By.ID, "identifierId").send_keys("idhilied@gmail.com")
    time.sleep(5)
    driver.find_element(By.ID, "identifierNext").click()
    time.sleep(5)

    time.sleep(5)
    driver.find_element(By.ID, "initialView").click()

    driver.find_element(By.NAME, "Passwd").send_keys("test2023")

    time.sleep(5)
    driver.find_element(By.ID, "passwordNext").click()


    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[guidedhelpid="new_menu_button"]')))
    element.click()
    #NOTE: TO INSPEACT A DISAPPEARING ELEMENT, KEEP PRESSING ON CTRL+SHIFT+C AND TRIGGER THIS ELEMENT TO SHOW THEN MOVE YOUR MOUSE TO THE ELEMENT U WANT TO INSPECT
    element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div[data-tooltip="File upload"]')))
    element.click()
    #upload a file randomly
    fileinput = driver.find_element(By.XPATH, "/html/body/input[2]")
    video_names = ['automation-deyar.mp4', 'testim-deyar.mp4', 'video1241937557.mp4',
                   'video1263108396.mp4','video1733716221.mp4','video1741500942.mp4',
                   'video1776593192.mp4','video2692176599.mp4']
    video_path = "C:/Users/dell/Documents/Zoom/videos"
    name = random.choice(video_names)
    video_file = os.path.join(video_path, name)
    print(video_file)
    fileinput.send_keys(video_file)
    time.sleep(5)
    # either the file is already uploaded or it's the first time
    try:
        #element is the popup that asks to replace the old with the new one, to keep both, or to cancel
        #if element is dispalyed then it's not the first time to upload this file
        #what will happen? : replace then upload
        element = driver.find_element(By.CSS_SELECTOR,
                                      "body > div.ZACE2c.vMI2nb.dif24c.vhoiae.KkxPLb.eO2Zfd > div.xmQMab > div > div > div")
        if element.is_displayed():
            print("replace")
            driver.find_element(By.CSS_SELECTOR,
                                "body > div.ZACE2c.vMI2nb.dif24c.vhoiae.KkxPLb.eO2Zfd > div.xmQMab > div > div > div > div > div.OsLnq.IRlIld > div:nth-child(2) > button").click()
        else:
            print("new file")

    except NoSuchElementException:
           print("The file is new")

    quit_chrome(driver)


def quit_chrome(driver):
    driver.quit()


if __name__ == '__main__':

    start_chrom()
