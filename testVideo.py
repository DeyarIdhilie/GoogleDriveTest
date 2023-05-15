import random
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
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
    time.sleep(5)
    sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
    time.sleep(5)
    sign_in.click()
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
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#\:5 > div > c-wiz > div:nth-child(3) > c-wiz > div > div.zCNSJd')))
    # driver.execute_script("arguments[0].classList.add('highlighted');", element)

    # double click to perview video
    video = driver.find_element(By.CSS_SELECTOR,".Ccie2c:nth-child(1) .l-u-Ab-zb-ma-za")
    action = ActionChains(driver)

   
    action.perform()
    time.sleep(30)
    iframe = driver.find_element(By.CSS_SELECTOR, "#drive-viewer-video-player-object-0")
    driver.switch_to.frame(iframe)
    video = driver.find_element(By.TAG_NAME, "video")
    video_current_time = 0
    is_stopped = False
    video_current_time = video.get_property('currentTime')
    if video_current_time == 0:
        print("video hasn't started yet, check your internet connection")
    elif video_current_time > 0:
        print("video has started playing")
    for i in range(60):
        print("i= ",i)
        time.sleep(1)
        video_current_time = video.get_property('currentTime')
        if video_current_time == 0:
            print("video hasn't started yet, check your internet connection")
        elif video_current_time >= 60:
            # turn the video off
            driver.execute_script("arguments[0].pause();", video)
            print("video was stopped at: ", video_current_time)
            is_stopped = True
            break
    if is_stopped == False:
        print("video forced to stop at: ", video_current_time)

    # go back to previous page
    driver.switch_to.default_content()
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Yk-hj-S"))
    )
    ActionChains(driver).move_to_element(element).perform()
    back_arrow = driver.find_element(By.CSS_SELECTOR, 'div[data-tooltip="Close"]')
    back_arrow.click()

    time.sleep(5)

    quit_chrome(driver)


def quit_chrome(driver):
    driver.quit()


if __name__ == '__main__':

    start_chrom()
