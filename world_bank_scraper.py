import requests
from bs4 import BeautifulSoup
import csv


class WorldBankScraper:
    def __init__(self):
        self.base_url = 'https://ieg.worldbankgroup.org/data'

    def scrape(self):
        # Send an HTTP GET request to the website
        response = requests.get(self.base_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            data = []
            for tender in soup.find_all('div', class_='tender'):
                tender_details = tender.text.strip()
                data.append(tender_details)

            self.save_to_csv(data)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    def save_to_csv(self, data):
        with open('world_bank_tenders.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Tender Details'])  # Add headers
            writer.writerows(data)


if __name__ == "__main__":
    scraper = WorldBankScraper()
    scraper.scrape()
