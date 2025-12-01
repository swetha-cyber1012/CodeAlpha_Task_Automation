import os
import requests
from bs4 import BeautifulSoup

def scrape_title():
    url = "https://example.com"
    output_file = "sample_files/output/title.txt"

    # Create directories if missing
    os.makedirs("sample_files/output", exist_ok=True)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string if soup.title else "No title found"

    with open(output_file, "w") as file:
        file.write(f"Page Title: {title}")

    print(f"Title saved to {output_file}")

scrape_title()
