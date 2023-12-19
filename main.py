from requests_html import AsyncHTMLSession, HTML
import json

'''async def getToyotaData(session, qty):
    # Send an HTTP request to the URL
    response = await get_toyota(session)

    carDataList = []

    #retrieve data elements
    msrp = response.html.find('.header' '.body-01', containing="$")
    model = response.html.find('.title' '.heading-04')
    modelYear = response.html.find('.model-year')

    #Check to see if amount of data matches what's expected and create a list if so, if not print for troubleshooting
    if len(msrp) == len(model) == len(modelYear) == qty:
        for i in range(qty):
            # msrp stores dollar amount in reverse correlation to the correct model & year, making an index for it and making it a func of i allows us to get around this
            msrpIndex = qty - i - 1
            carData = {
            'Make' : "Toyota",
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
        print(qty)
        return False'''

async def getLexusData(session, qty):
    # Send an HTTP request to the URL
    response = await get_lexus(session)

    carDataList = []

    #retrieve data elements
    msrpStrings = response.html.find('.modelCard > p:nth-child(2)')
    modelsYears = response.html.find('.h3' '.margin-vert-x')

    #Check to see if amount of data matches what's expected and create a list if so, if not print for troubleshooting
    if len(msrpStrings) == len(modelsYears) == qty:
        for i in range(qty):
            #Splitting the modelsyears strings into the specific models and years for each one
            splittempa = modelsYears[i].split(' ', 1)
            modelYear = splittempa[1]
            splittempb = splittempa[2].split(' ')
            model = splittempb[2]

            #Splitting the msrp strings to only grab the actual price
            splittempc = msrpStrings[i].split(' ')
            msrp = splittempc[2]

            # msrp stores dollar amount in reverse correlation to the correct model & year, making an index for it and making it a func of i allows us to get around this
            # msrpIndex = qty - i - 1
            # i havent had a chance to run it so i have no idea if the msrp thing is still gonna be backwards i feel like it shouldnt but who knows
            carData = {
            'Make' : "Lexus",
            'Model': model.text,
            'Year' : modelYear.text,
            'MSRP' : msrp.text
            } 
            carDataList.append(carData)
        return carDataList

    else:
        print("Inconsistent Data Lengths. Printing length of lists: MSRP, Model, Model Year \n") 
        print(len(msrp))
        print(len(model))
        print(len(modelYear))
        print(qty)
        return False

def writeToJson(dataList, filename):
    with open(filename, "w") as file_object:
        json.dump(dataList, file_object, indent = 2)

'''async def get_toyota(session):
    try:
        response = await session.get('https://www.toyota.com/all-vehicles/')
        await response.html.arender()
        return response
    except Exception as e:
        print(f"Error fetching Toyota data: {e}")
        return None'''

async def get_lexus(session):
    try:
        response = await session.get('https://www.metrolexus.com/showroom.html')
        await response.html.arender()
        return response
    except Exception as e:
        print(f"Error fetching Lexus data: {e}")
        return None

async def main():
    session = AsyncHTMLSession()

    #toyotaQty = 50
    #toyotaDataList = await getToyotaData(session, toyotaQty)

    lexusQty = 29
    lexusDataList = await getLexusData(session, lexusQty)

    '''if toyotaDataList:
        # Call function to write the list contents into the json file
        filename = "json_files/toyota.json"
        writeToJson(toyotaDataList, filename)
        print(f"Data written to {filename}")'''
    
    if lexusDataList:
        # Call function to write the list contents into the json file
        filename = "json_files/lexus.json"
        writeToJson(lexusDataList, filename)
        print(f"Data written to {filename}")

    await session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())