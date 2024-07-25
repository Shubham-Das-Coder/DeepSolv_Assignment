import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text

if __name__ == "__main__":
    url = "https://www.apple.com/apple-vision-pro/"
    website_text = scrape_website(url)
    with open("E:/DeepSolv_Assignment/data/extracted_website_text.txt", "w", encoding="utf-8") as f:
        f.write(website_text)
