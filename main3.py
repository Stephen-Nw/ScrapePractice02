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

    driver.get("https://news.ycombinator.com/")
    return driver


def get_news():
    driver = get_driver()

    highlights = driver.find_elements(
        By.CLASS_NAME, "titleline")    # Get the topics

    links = driver.find_elements(
        By.CSS_SELECTOR, ".titleline a")   # Get the links to the topics

    # Get the votes for the topics
    upvotes = driver.find_elements(By.CSS_SELECTOR, ".score")

    article_topics = []
    article_links = []
    article_upvotes = []

    for highlight in highlights:
        article_heading = highlight.text
        article_topics.append(article_heading)

    for item in links:
        link = item.get_attribute('href')
        article_links.append(link)

    for vote in upvotes:
        points = vote.text
        article_upvotes.append(points)

    # Values in 'article links' have both number and text. Split number from text and convert number to int
    updated_votes = [int(upvote.split()[0]) for upvote in article_upvotes]

    # Links have heading links and submitter links. Remove submitter links
    updated_links = [
        link for link in article_links if article_links.index(link) % 2 == 0]

    # Find the highest vote number and then the index of that number
    largest_number = max(updated_votes)
    largest_index = updated_votes.index(largest_number)

    most_upvoted_article = article_topics[largest_index]
    most_upvoted_link = updated_links[largest_index]

    most_read_article = {most_upvoted_article: most_upvoted_link}

    return most_read_article


print(get_news())
