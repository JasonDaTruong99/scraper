from requests_html import AsyncHTMLSession, HTML
import json

async def getToyotaData(session, qty):
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
            print("Enter Kelly Blue Book URL for " + modelYear[i].text + " " + model[i].text)
            url = input()
            averagePrice = await getKellyPrices(url, session)
            carData = {
            'Make' : "Toyota",
            'Model': model[i].text,
            'Year' : modelYear[i].text,
            'MSRP' : msrp[msrpIndex].text,
            'Average Price': averagePrice
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

async def get_toyota(session):
    try:
        response = await session.get('https://www.toyota.com/all-vehicles/')
        await response.html.arender()
        return response
    except Exception as e:
        print(f"Error fetching Toyota data: {e}")
        return None

async def getKellyPrices(url, session):
    try:
        selector ='.item-card .positioned-overlay-base .margin-left-auto.col-xs-4.text-right.pull-right > div > span.first-price.text-ultra-bold'
        kResponse = await session.get(url)
        await kResponse.html.arender()
        prices = kResponse.html.find(selector)
        sumPrices = sum(float(price.text.replace('$', '').replace(',', '')) for price in prices)
        print(len(prices))
        for price in prices:
            print(" These are the prices of the car" + prices.text)
        avg = sumPrices/len(prices)
        return avg
    except Exception as e:
        print(f"Error fetching prices from KBB: {e}")
        return None 

async def main():
    session = AsyncHTMLSession()
    #ToyotaQty is 50
    toyotaQty = 50
    toyotaDataList = await getToyotaData(session, toyotaQty)

    if toyotaDataList:
        # Call function to write the list contents into the json file
        filename = "json_files/toyota.json"
        writeToJson(toyotaDataList, filename)
        print(f"Data written to {filename}")

    await session.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())