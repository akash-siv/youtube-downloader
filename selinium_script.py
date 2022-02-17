from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


chrome_options = Options()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--lang=en-us")
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:8282")
s = Service('C:/Users/akash/PycharmProjects/youtube_downloader/chromedriver.exe')
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://www.youtube.com/playlist?list=WL")
time.sleep(2)
link_list = []

def video_list():
    link_object = driver.find_elements_by_tag_name('a')
    old_list= [page.get_attribute('href') for page in link_object]
    for a in old_list:
        try:
            if "watch" in a:
                link_list.append(a)
        except:
            pass
    return set(link_list)


def download(link):
    driver = webdriver.Chrome(service=s, options=chrome_options)
    driver.get("https://savef.net/en48/?ts=1645019911253&url=https%3A%2F%2Fm.youtube.com%2F")
    current_tab = driver.current_window_handle
    url = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".main-form-input")))
    url.clear()
    url.send_keys(link)
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".main-form-submit"))).click()
    try:
        time.sleep(1)
        chwd = driver.window_handles
        for new_window in chwd:
            # switch focus to child window
            if (new_window != current_tab):
                driver.close()

        driver.switch_to.window(current_tab)
        time.sleep(1)
        a = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "tr:nth-child(3) td:nth-child(1) .download-link-popup-js")))
    except:
        pass
    else:
        if a.text == "720":
            a.click()
        elif WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "tr:nth-child(2) td:nth-child(1) .download-link-popup-js"))).text == "720":
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "tr:nth-child(2) td:nth-child(1) .download-link-popup-js"))).click()
            time.sleep(15)





