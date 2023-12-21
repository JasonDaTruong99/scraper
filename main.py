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

'''async def getLexusData(session, qty):
    # Send an HTTP request to the URL
    response = await get_lexus(session)

    carDataList = []

    #retrieve data elements
    msrpStrings = response.html.find('.modelCard a p:nth-child(3)')
    modelsYears = response.html.find('.h3' '.margin-vert-x')
    #for some reason there is an extra first element that have the classes for the modelYears stuff so im just manually getting rid of it
    modelsYears.pop(0)

    #Check to see if amount of data matches what's expected and create a list if so, if not print for troubleshooting
    if len(msrpStrings) == len(modelsYears) == qty:
        for i in range(qty):
            #Splitting the modelsyears strings into the specific models and years for each one
            splittempa = modelsYears[i].text.split(' ', 1)
            modelYear = splittempa[0]
            splittempb = splittempa[1].split(' ', 1)
            model = splittempb[1]

            #Splitting the msrp strings to only grab the actual price
            splittempc = msrpStrings[i].text.split(' ')
            msrp = splittempc[2]

            #msrp works normally for this one for some reason no need to invert
            carData = {
            'Make' : "Lexus",
            'Model': model,
            'Year' : modelYear,
            'MSRP' : msrp
            } 
            carDataList.append(carData)
        return carDataList

    else:
        print("Inconsistent Data Lengths. Printing length of lists: MSRP Strings, Model/Year Strings, qty")
        print(len(msrpStrings))
        print(len(modelsYears))
        print(qty)
        return False'''

async def getAcuraData(session, qty):
    # Send an HTTP request to the URL
    response = await get_acura(session)

    carDataList = []

    #retrieve data elements
    modelsYears = response.html.find('.col-sm-6 > h1')
    msrpStrings = response.html.find('.col-sm-6 > p strong')

    #Check to see if amount of data matches what's expected and create a list if so, if not print for troubleshooting
    if len(msrpStrings) == len(modelsYears) == qty:
        for i in range(qty):
            #Splitting the modelsyears strings into the specific models and years for each one
            splittempa = modelsYears[i].text.split(None, 1)
            modelYear = splittempa[0]
            model = splittempa[1]

            #Splitting the msrp strings to only grab the actual price
            if 'Starting at ' in msrpStrings[i].text and ' MSRP*' in msrpStrings[i].text:
                msrp = msrpStrings[i].text.split('Starting at ')[1].split(' MSRP*')[0]
            else:
                msrp = msrpStrings[i].text

            #msrp works normally for this one for some reason no need to invert
            carData = {
            'Make' : "Acura",
            'Model': model,
            'Year' : modelYear,
            'MSRP' : msrp
            } 
            carDataList.append(carData)
        return carDataList

    else:
        print("Inconsistent Data Lengths. Printing length of lists: MSRP Strings, Model/Year Strings, qty")
        print(len(msrpStrings))
        print(len(modelsYears))
        print(qty)
        return False
    
def writeToJson(dataList, filename):
    with open(filename, "w") as file_object:
        json.dump(dataList, file_object, indent = 2)

#Functions to open html sessions and render them into html from javascript
'''async def get_toyota(session):
    try:
        response = await session.get('https://www.toyota.com/all-vehicles/')
        await response.html.arender()
        return response
    except Exception as e:
        print(f"Error fetching Toyota data: {e}")
        return None'''

'''async def get_lexus(session):
    try:
        response = await session.get('https://www.metrolexus.com/showroom.html')
        await response.html.arender()
        return response
    except Exception as e:
        print(f"Error fetching Lexus data: {e}")
        return None'''

async def get_acura(session):
    try:
        response = await session.get('https://www.rizzaacura.com/acura-models-orland-park-il')
        await response.html.arender()
        return response
    except Exception as e:
        print(f"Error fetching Acura data: {e}")
        return None
    
async def main():
    session = AsyncHTMLSession()

    #Giving quantity of models on each site and calling functions to get data
    '''toyotaQty = 50
    toyotaDataList = await getToyotaData(session, toyotaQty)'''

    '''lexusQty = 29
    lexusDataList = await getLexusData(session, lexusQty)'''

    acuraOty = 7
    acuraDataList = await getAcuraData(session, acuraOty)

    #making sure datalists came back correctly before writing to json
    '''if toyotaDataList:
        # Call function to write the list contents into the json file
        filename = "json_files/toyota.json"
        writeToJson(toyotaDataList, filename)
        print(f"Data written to {filename}")'''
    
    '''if lexusDataList:
        # Call function to write the list contents into the json file
        filename = "json_files/lexus.json"
        writeToJson(lexusDataList, filename)
        print(f"Data written to {filename}")'''
    
    if acuraDataList:
        # Call function to write the list contents into the json file
        filename = "json_files/acura.json"
        writeToJson(acuraDataList, filename)
        print(f"Data written to {filename}")

    #Need to close session to avoid loop exceptions
    await session.close()

if __name__ == "__main__":
    #Also some weird stuff to avoid loop exceptions with async sessions
    import asyncio
    asyncio.run(main())