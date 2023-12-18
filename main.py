from requests_html import HTMLSession
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
toyotaQty = 49

# create a dynamic list to write car data to
toyotaDataList = []

def getCarData():
    for i in range(toyotaQty):
        # msrp stores dollar amount in reverse correlation to the correct model & year, making an index for it and making it a func of i allows us to get around this
        msrpIndex = toyotaQty - i
        carData = {
            'Model': model[i].text,
            'Year' : modelYear[i].text,
            'MSRP' : msrp[msrpIndex].text
        } 
        toyotaDataList.append(carData) # append scraped data to list

getCarData() #Call function to fill the list

# Write the list contents into the json file
filename = "toyota.json"
with open(filename, "w") as file_object:
    json.dump(toyotaDataList, file_object, indent = 2)

