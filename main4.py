from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(r"C:\Development\\chromedriver.exe")


def get_driver():
    """Create selenium driver"""
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

    driver.get(
        "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
    return driver


def get_movies():
    """Scrape movie titles from website"""
    driver = get_driver()

    movies = driver.find_elements(
        By.CSS_SELECTOR, ".article-title-description__text h3")

    # movie_list = []
    # for movie in movies:
    #     movie = movie.text
    #     movie_list.append(movie)

    movie_list = [movie.text for movie in movies]
    sorted_movies = movie_list[::-1]   # Reverse movie list

    return sorted_movies


def movieList_to_txt():
    """Convert movie list to text"""
    movies = get_movies()

    with open("movies.txt", mode="w") as file:
        for movie in movies:
            file.write(f"{movie}\n")

    return


movieList_to_txt()
