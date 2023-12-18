from requests_html import HTMLSession
from bs4 import BeautifulSoup
import json

# Define type of session being used for requests lib
session = HTMLSession()

# Send an HTTP request to the URL
response = session.get('https://www.toyota.com/all-vehicles/')

response.html.render()

# init variables
msrp = response.html.find('.header' '.body-01', containing="$")
model = response.html.find('.title' '.heading-04')
modelYear = response.html.find('.model-year')

# create a dynamic list to write car data to
carDataList = []

def getCarData():
    for i in range(50):
        # msrp stores dollar amount in reverse correlation to the correct model & year, making an index for it and making it a func of i allows us to get around this
        msrpIndex = 49 - i
        carData = {
            'Model': model[i].text,
            'Year' : modelYear[i].text,
            'MSRP' : msrp[msrpIndex].text
        } 
        carDataList.append(carData) # append scraped data to list

getCarData() #Call function to fill the list

# Write the list contents into the json file
filename = "toyota.json"
with open(filename, "w") as file_object:
    json.dump(carDataList, file_object, indent = 2)

