import requests
import logging
import json


class item:
    logger = logging.getLogger("logging_api")
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s; %(levelname)s; %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    apiKey = "35c8de34d5f1fd4cbd609cd6b22c9d64d1109b6f"
    storeId = '1375'


    def is_string(value):
      try:
        str(value)
        return True
      except:
        return False

    def productDetailsFromBarcode(barcode):

        if item.is_string(barcode):
            productName = barcode
        else :
            productName = getProductNameFromBarcode(barcode)

        url = "https://redsky.target.com/v1/plp/search?keyword=" + str(productName) + "&count=2&offset=0"
        response = requests.get(url, verify=False)

        try:
            if response is not None:
                return json.loads(response.text)['search_response']['items']['Item'][0]['description']
            else:
                item.logger.error("productDetailsFromBarcode failed!")
                item.logger.error("response invalid in redsky API")
        except Exception as e:
            item.logger.error("productDetailsFromBarcode failed!")
            item.logger.error(e)

    def getProductNameFromBarcode(barcode):
        barcode = str("20") + str(barcode) + str("000008")
        url = "https://api-internal.target.com/core_items/v1/?barcode=" + str(
            barcode) + "&launchDate=ALL&itemState=ALL&itemStatus=ALL&key=" + str(item.apiKey)

        url = "https://api.target.com/digital_items/v1/full?barcode="+ str(barcode) + "&key=" + + str(item.apiKey)
        try:
            response = requests.get(url, verify=False)
            if response is not None:
                product = json.loads(response.text)['tcin']
                print(product)
                return product
            else:
                item.logger.error("getProductName failed!")
                item.logger.error("response invalid for barcode " + str(barcode))

        except Exception as e:
            item.logger.error("getProductName failed!")
            item.logger.error(e)

    def getDpciFromProductName(productName):
        url = "https://redsky.target.com/v1/plp/search?keyword=" + productName + "&count=2&offset=0"

        try:
            response = requests.get(url, verify=False)
            if response is not None:
                for item in json.loads(response.text)['search_response']['items']['Item']:
                    if ('tcin' in item):
                        return item['tcin']
                item.logger.error("tcin not found for product " + str(productName))
                return None
            else:
                item.logger.error("getLocationForProduct failed!")
                item.logger.error("invalid response!")
        except Exception as e:
            item.logger.error("getLocationForProduct failed!")
            item.logger.error(e)

    def getLocationFromProductName(brand, product):

        if brand is not None and product is not None:
            productName = str(brand) + str(" ") + str(product)
        if brand is None:
            productName = str(product)
        if product is None:
            productName = str(brand)

        dpci = item.getDpciFromProductName(productName)
        if (dpci is not None):
            # dpci = "080-02-0551"

            #url = "https://api-internal.target.com/store_item_placements/v1/?dpci=" + str(dpci) + "&location_id=" + str(item.storeId) + "&key=" + str(item.apiKey)
            url = "https://redsky.target.com/v1/location_details/" + str(dpci) + "?storeId=" + str(item.storeId)

            try:
                response = requests.get(url, verify=False)
                response = json.loads(response.text)['product']['in_store_location']
                if response is not None:
                    responseString = productName + str(" is located on floor ") + str(response['floor']) + str(" block ") + str(response['block']) + str(", block aisle ") + str(response['block_aisle']) + str(" section ") + str(response['section'])
                    return responseString
                else:
                    item.logger.error("getLocationFromProductName failed!")
                    item.logger.error("response invalid for productName " + productName)

            except Exception as e:
                item.logger.error("getLocationFromProductName failed!")
                item.logger.error(e)
        else:
            item.logger.error("getLocationFromProductName failed!")
            item.logger.error("dpci not found!")
