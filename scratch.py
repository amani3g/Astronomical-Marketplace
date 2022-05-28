import requests
import json

eaot_base = "https://catalogs.mast.stsci.edu/api/v0.1/eaot/search/"
metadata = eaot_base + "metadata.json"

COLUMNS = {
            'Planet_Name': 'Planet name', 
            'SNR_Emission_15_micron': '1.5 micron Emission SNR relative to HD 209458 b',
            'SNR_Emission_5_micron': '5 micron Emission SNR relative to HD 209458 b',
            'SNR_Emission_K_mag': 'K-band Transmission SNR relative to HD 209458 b',
            'Rp': 'Planet radius (Jupiter radii)',
            'Mp': 'Planet mass (Jupiter masses)',
            'Tday': 'Dayside Temperature (Kelvin)'',
            'Teq': 'Planet equilibrium temperature (K)',
            'log10g_p': 'Planet surface gravity',
            'Period': 'Planet orbital period (d)',
            'Transit_Duration': 'Planet transit duration (hr)',
            'K_mag': 'K-band magnitude',
            'Distance': 'Distance to planet host star (pc)',
            'Teff': 'Stellar effective temperature (K)',
            'log10g_s': 'Stellar surface gravity',
            'Transit_Flag': ' Planet transit flag (0- no transit, 1- transit)',
            'Catalog_Name': 'Planet source catalog name'
        }

def make_request(string):
    try:
        request = requests.get(string)
        return request
    except Exception:
        print("Request did not update. Returned {}".format(request))

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def jtext(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

def jdict(text):
    dict = json.loads(text)
    return dict