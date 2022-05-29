import requests
import json

EAOT_BASE = "https://catalogs.mast.stsci.edu/api/v0.1/eaot/search"
METADATA = EAOT_BASE + "/metadata.json"
JSON_DECORATOR = '.json'

COLUMNS = {
            "Planet_Name": "Planet name", 
            "SNR_Emission_15_micron": "1.5 micron Emission SNR relative to HD 209458 b",
            "SNR_Emission_5_micron": "5 micron Emission SNR relative to HD 209458 b",
            "SNR_Emission_K_mag": "K-band Transmission SNR relative to HD 209458 b",
            "Rp": "Planet radius (Jupiter radii)",
            "Mp": "Planet mass (Jupiter masses)",
            "Tday": "Dayside Temperature (Kelvin)",
            "Teq": "Planet equilibrium temperature (K)",
            "log10g_p": "Planet surface gravity",
            "Period": "Planet orbital period (d)",
            "Transit_Duration": "Planet transit duration (hr)",
            "K_mag": "K-band magnitude",
            "Distance": "Distance to planet host star (pc)",
            "Teff": "Stellar effective temperature (K)",
            "log10g_s": "Stellar surface gravity",
            "Transit_Flag": " Planet transit flag (0- no transit, 1- transit)",
            "Catalog_Name": "Planet source catalog name"
        }

class EAOTException(Exception):
    """Class for EAOT Exceptions"""

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

def jdict(text) -> dict:
    dict = json.loads(text)
    return dict

def query_columns(columns, sort=None, sort_on_col=None) -> dict:
    """ Query columns name, and return dictionary of column
    columns (dict) - Dictionary of column names and bounds
        e.g.
        columns = {
                    'col_name': {'upper': None, 'lower': foo}, 
                    'col_name2' : {'upper': bar, 'lower': foo}
                    }
    sort (string) -  'asc' or 'desc'
    sort_on_col (string) - column to sort on
    return:
        results - json dictionary of column values 
    """
    query = EAOT_BASE + JSON_DECORATOR
    for column in columns.keys():
        if column in COLUMNS.keys():
            query += "?columns=" + column
            if columns[column]['upper']:
                query += ".gte=" + str(column[upper])
            if columns[column]['lower']:
                query += ".lte=" + str(column[lower])
            if len(columns) > 1 and column != column[-1]:
                query += "&"
        else:
            raise(EAOTException("Invalid column {}".format(column)))
    if sort:
        if sort_on_col in COLUMNS.keys() and (sort == '.asc' or sort == 'desc'):
            query += "sort_by=" + sort_on_col + "." + sort
        else:
            raise(EAOTException("Invalid sorting on column: {} sorting: {}".format(sort_on_col, sort)))
    
    print(query)

    return make_request(query)

query_input = {"Planet_Name": {'upper': None, 'lower': None}}

output_planet_name = query_columns(query_input)
print(output_planet_name)