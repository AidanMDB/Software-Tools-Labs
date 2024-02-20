# ######################################################
# Author :  Aidan Dannhausen-Brun
# email : adannhau@purdue.edu
# ID : ee364a10
# Date : 02/10/2024
# ######################################################

import os  # List of module import statements
import sys  # Each one on a line
import re
import glob
import string
import math

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################

def getProviderDict(provider : str):
    provider_dict = dict()
    with open(f"providers/{provider}.dat", 'r') as file:
        next(file)
        next(file)
        next(file)
        for line in file:
            SBC, price = line.replace(" ", "").split(',')
            provider_dict[SBC] = float(price[1:-1])

    return provider_dict





def getDifference(SBC : str, provider1 : str, provider2 : str):
    prov1_dict = getProviderDict(provider1)
    prov2_dict = getProviderDict(provider2)
    SBC = SBC.replace(" ", "")
    dif = round(abs(prov2_dict[SBC] - prov1_dict[SBC]), 2)
    return dif

def getLowestInModel(sbc_model, provider):
    min = dict()

    sbc_model = sbc_model.replace(" ", "")[:-1]
    prov_dict = getProviderDict(provider)
    min_price = 0

    for model, price in prov_dict.items():
        if re.match(sbc_model+'[A-Z0-9]+', model):
            min_price = price
            break

    for model, price in prov_dict.items():
        
        if price < min_price and re.match(sbc_model+'[A-Z0-9]+', model):
            min.clear()
            min[model[:5]+' '+model[5:]] = price
            min_price = price
        elif price == min_price and re.match(sbc_model+'[A-Z0-9]+', model):
            min[model[:5]+' '+model[5:]] = (price)
            min_price = price

    return min

def checkAllPrices(sbcset : set):
    sbc_dict = dict()
    for sbc in sbcset:
        sbc = sbc.replace(" ", "")
        min_price = sys.maxsize
        provider = ""
        for prov in os.scandir("providers"):
            prov_dict = getProviderDict(os.path.basename(prov)[:-4])
            if prov_dict.get(sbc) != None and prov_dict.get(sbc) < min_price:
                min_price = prov_dict[sbc]
                provider = os.path.basename(prov)[:-4]
        sbc_dict[sbc[:5]+' '+sbc[5:]] = (provider, min_price)
    return sbc_dict


def getYearlyVolumeAndClose():
    yearly_dict = dict()
    with open("stocks.dat", 'r') as file:
        next(file)
        next(file)
        for line in file:
            values = line.split(',')
            year = values[0].split("\\")[0]
            if year != yearly_dict.keys():
                yearly_dict[year] = (values[2],values[1])
            
    return 0


# ######################################################
# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################
if __name__ == "__main__":

    #print(getProviderDict("provider1"))
    print(getDifference("Rasp. Pi-4800MQ", "provider2", "provider4"))
    
    print(getLowestInModel("Rasp. Pi-5*", "provider2"))

    print(checkAllPrices({"Rasp. Pi-4800MQ", "Rasp. Pi-6600U", "Rasp. Pi-4950HQ", "Rasp. Pi-5750HQ"}))