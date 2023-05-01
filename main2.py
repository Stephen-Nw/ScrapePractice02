from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(r"C:\Development\\chromedriver.exe")


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

    driver.get("https://www.python.org/")
    return driver


def get_events():
    driver = get_driver()
    event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
    event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

    events = {}

    for n in range(len(event_times)):
        events[n] = {
            "time": event_times[n].text,
            "name": event_names[n].text,
        }
    return events


print(get_events())
