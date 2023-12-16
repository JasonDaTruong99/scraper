import requests
from bs4 import BeautifulSoup

def scrape_website():
    url = "https://www.toyota.com/search-inventory/"
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract data using BeautifulSoup methods
        # Example: Print all the text content of <p> tags
        for paragraph in soup.find_all('p'):
            print(paragraph.get_text())

    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the website you want to scrape
    website_url = 'https://example.com'
    scrape_website(website_url)