from requests_html import HTMLSession
from bs4 import BeautifulSoup

    # Define type of session being used for requests lib
session = HTMLSession()

    # Send an HTTP request to the URL
response = session.get('https://www.toyota.com/all-vehicles/')

response.html.render()

#print(response.text)

msrp = response.html.find('.header' '.body-01', containing="$")
for i in range(50):
    if msrp:
        print(msrp[i].text)
    else:
        print("No MSRP")

model = response.html.find('.title' '.heading-04')
for i in range(50):
    if model:
        print(model[i].text)
    else:
        print("No Model")

modelYear = response.html.find('.model-year')
for i in range(50):
    if modelYear:
        print(modelYear[i].text)
    else:
        print("No Model Year")