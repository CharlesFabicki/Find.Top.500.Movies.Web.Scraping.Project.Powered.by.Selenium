from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv
import codecs
import locale

# Set the locale for formatting numbers and handling Polish characters
locale.setlocale(locale.LC_ALL, 'pl_PL.UTF-8')

# Create a WebDriver instance
driver = webdriver.Edge()

# Open the URL
url = 'https://www.filmweb.pl/ranking/film'
driver.get(url)

# Open the CSV file for writing with proper encoding
csv_file = codecs.open('movie_ranking.csv', 'w', 'utf-8-sig')
csv_writer = csv.writer(csv_file, dialect='excel')

# Write the header row
csv_writer.writerow(['Polish Title', 'Original Title', 'Rating', 'Votes', 'Genre'])

try:
    # Wait for the ranking cards to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='rankingType__card']")))

    max_pages = 25  # Adjust this value to load up to 500 movies (assuming 20 movies per page)
    page = 1

    while page <= max_pages:
        # Get the page source and parse it with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all ranking cards
        ranking_cards = soup.select(".rankingType__card")

        for card in ranking_cards:
            title = card.select_one(".rankingType__originalTitle")
            rate = card.select_one(".rankingType__rateWrapper")
            genre = card.select_one(".rankingType__genres")
            votes_count = card.select_one("span.rankingType__rate--count")

            # Extract and write the desired <h2> element (Polish title)
            h2_element = card.select_one("h2.rankingType__title[itemprop='name']")
            h2_text = h2_element.get_text(strip=True) if h2_element else "No title found"

            title_text = title.get_text(strip=True) if title else " "
            rate_text = rate.get_text(strip=True) if rate else " "
            genre_text = genre.get_text(strip=True) if genre else " "
            votes_text = votes_count.get_text(strip=True) if votes_count else " "

            # Extract the numeric portion of the rate text
            rate_parts = rate_text.split()
            if len(rate_parts) >= 2:
                rate_number = round(float(rate_parts[0].replace(',', '.')), 2)
                votes_numeric = ''.join(filter(str.isdigit, votes_text))
            else:
                rate_number = None
                votes_numeric = None

            # Write the data to the CSV file
            csv_writer.writerow([h2_text, title_text, rate_number, votes_numeric, genre_text])

        # Move to the next page by going to the URL of the next page
        next_url = f'https://www.filmweb.pl/ranking/film?page={page + 1}'
        driver.get(next_url)

        # Wait for the ranking cards to load on the next page
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='rankingType__card']")))

        page += 1

finally:
    # Check if the browser window is still available before closing
    if driver.window_handles:
        driver.quit()

    # Close the CSV file
    csv_file.close()
