# Movie Ranking Web Scraper

This Python script is designed to scrape movie ranking data from the Filmweb website (https://www.filmweb.pl/ranking/film) and save it to a CSV file. It uses the Selenium web automation library to navigate the website and retrieve data, and the BeautifulSoup library to parse HTML content.

## Requirements

- Python 3.x
- Selenium (Install using `pip install selenium`)
- BeautifulSoup (Install using `pip install beautifulsoup4`)

## How to Use

1. **Install Python:** Make sure you have Python 3.x installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

2. **Install Required Libraries:** Open a command prompt or terminal and install the required libraries using the following commands:

3. **WebDriver:** This script uses the Edge WebDriver. You need to download the appropriate Microsoft Edge WebDriver for your browser version from: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
Make sure the WebDriver executable is in your system's PATH.

4. **Download the Script:** Download the `movie_ranking_scraper.py` script to your computer.

5. **Run the Script:** Open a command prompt or terminal and navigate to the directory where you downloaded the script. Run the script using the following command:

6. **CSV Output:** The script will start scraping movie data from the Filmweb ranking pages. It will create a CSV file named `movie_ranking.csv` in the same directory as the script. The CSV file will contain columns for Polish Title, Original Title, Rating, Votes, and Genre of each movie.

7. **Adjust Number of Pages (Optional):** By default, the script is set to scrape data from the first 25 pages (approximately 500 movies). You can adjust the `max_pages` variable in the script to scrape more or fewer pages based on your preferences.

8. **Completion:** The script will automatically close the web browser and save the CSV file when it finishes scraping the data.

**Note:** Please be respectful of the website's terms of use and scraping policies. Excessive or aggressive scraping can put strain on the website's servers and may be in violation of their terms.

For any issues or questions, please contact 

