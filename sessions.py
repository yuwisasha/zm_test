import random
import time
import urls, db
import json

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


try:
    urls = urls.get_news_urls()
except Exception as ex:
    print(ex)

def scroll_page(driver):
    time.sleep(random.randint(2, 5))
    try:
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    except Exception as ex:
        print(ex)
        return
    time.sleep(random.randint(2, 5))

def session(profile_id, cookies):
    try:
        driver = webdriver.Chrome()
        driver.get(random.choice(urls))

        if cookies:
                cookies_json = json.loads(cookies)
                for cookie in cookies_json:
                     driver.add_cookie({'name': cookie['name'], 'value': cookie['value']})

        scroll_page(driver)
        new_cookies = driver.get_cookies()
        db.update_cookie(profile_id, new_cookies)
        print('Cookie updated')

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
