from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(r"C:\Development\\chromedriver.exe")


def get_spotify_url():
    requested_year = input(
        "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
    spotify_url = f"https://www.billboard.com/charts/hot-100/{requested_year}"
    return spotify_url


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option(
        "excludeSwitches", ["enable-logging"])   # Remove error message from adding below option"
    options.add_experimental_option("detach", True)   # Keep browswer open
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get(get_spotify_url())
    return driver


def get_songList():
    driver = get_driver()

    songs = driver.find_elements(
        By.CSS_SELECTOR, ".o-chart-results-list__item .c-title")
    songList = [song.text for song in songs]
    return songList


print(get_songList())
