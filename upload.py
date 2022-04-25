import gspread
from opensea import OpenseaAPI
import time


####################################################################################################################
##                                            Setup    //    API Keys                                             ##
####################################################################################################################
                                                                                                                  ##
                                                                                                                  ##
os = OpenseaAPI(apikey='your OpenSea API Key goes here')                                                          ##
gc = gspread.service_account(filename='the name or location of your Google API .json goes here')                  ##
sheet = gc.open('the name of your google sheet goes here')                                                        ##
worksheet_floor = sheet.worksheet('floor prices')                                                                 ##
worksheet_volume = sheet.worksheet('volume')                                                                      ##
worksheet_sales = sheet.worksheet('sales')                                                                        ##
worksheet_owners = sheet.worksheet('holders')                                                                     ##
worksheet_avgholder = sheet.worksheet('avg. holder')                                                              ##
                                                                                                                  ##
                                                                                                                  ##
# Change this variable to reflect the list of collections you wish to track                                       ##
collections = []                                                                                                  ##
                                                                                                                  ##
####################################################################################################################
####################################################################################################################


# function to grab and upload the data
def postData(slugs):
    date = str(datetime.date.today())
    floors = [date]
    volumes = [date]
    saless = [date]
    ownerss = [date]
    per_holder = [date]
    
    # Iterate over the list of collections and grab the specified data
    for slug in slugs:
        data = os.collection_stats(slug)
        floor = round(data['stats']['floor_price'], ndigits=2)
        floors.append(floor)
        volume = round(data['stats']['one_day_volume'], ndigits=2)
        volumes.append(volume)
        sales = round(data['stats']['one_day_sales'], ndigits=2)
        saless.append(sales)
        owners = round(data['stats']['num_owners'], ndigits=2)
        ownerss.append(owners)
        supply = round(data['stats']['total_supply'], ndigits=2)
        per_holder.append(round(supply/owners, ndigits=2))
        
        # Line to prevent being rate-limited
        time.sleep(.25)

    # Append the data to the spreadsheet
    worksheet_floor.append_row(floors)
    worksheet_volume.append_row(volumes)
    worksheet_sales.append_row(saless)
    worksheet_owners.append_row(ownerss)
    worksheet_avgholder.append_row(per_holder)
    
