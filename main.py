from requests_html import HTMLSession
import json

def getCarData(session, url, qty):
    # Send an HTTP request to the URL
    response = session.get('https://www.toyota.com/all-vehicles/')
    response.html.render()

    carDataList = []

    #retrieve data elements
    msrp = response.html.find('.header' '.body-01', containing="$")
    model = response.html.find('.title' '.heading-04')
    modelYear = response.html.find('.model-year')
    
    if len(msrp) == len(model) == len(modelYear) == qty:
        for i in range(qty):
            # msrp stores dollar amount in reverse correlation to the correct model & year, making an index for it and making it a func of i allows us to get around this
            msrpIndex = qty - i - 1
            carData = {
            'Model': model[i].text,
            'Year' : modelYear[i].text,
            'MSRP' : msrp[msrpIndex].text
            } 
            carDataList.append(carData)
        return carDataList

    else:
        print("Inconsistent Data Lengths. Printing length of lists: MSRP, Model, Model Year \n") 
        print(len(msrp))
        print(len(model))
        print(len(modelYear))

def writeToJson(dataList, filename):
    with open(filename, "w") as file_object:
        json.dump(dataList, file_object, indent = 2)

def main():
    # Define type of session being used for requests lib
    session = HTMLSession()

    url = 'https://www.toyota.com/all-vehicles/'
    toyotaQty = 50
    toyotaDataList = getCarData(session, url, toyotaQty)

    if toyotaDataList:
        # Call function to write the list contents into the json file
        filename = "toyota.json"
        writeToJson(toyotaDataList, filename)
        print(f"Data written to {filename}")

if __name__ == "__main__":
    main()

