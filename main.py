from requests_html import HTMLSession
from bs4 import BeautifulSoup

    # Define type of session being used for requests lib
session = HTMLSession()

    # Send an HTTP request to the URL
response = session.get('https://www.toyota.com/all-vehicles/')

response.html.render()

#print(response.text)

a = response.html.find('vehicles-grid')
print(a)

about = response.html.find('vehicles-grid', first=False)
print(.text)