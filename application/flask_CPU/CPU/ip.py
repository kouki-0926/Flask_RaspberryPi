import requests

def get_location(ip_address):
    Data=[]

    url = "https://ipapi.co/"+ip_address+"/json/"
    data = requests.get(url).json()

    Data.append("ip: {}".format(data["ip"]))
    Data.append("version: {}".format(data["version"]))
    Data.append("city: {}".format(data["city"]))
    Data.append("region: {}".format(data["region"]))
    Data.append("region_code: {}".format(data["region_code"]))
    Data.append("country: {}".format(data["country"]))
    Data.append("country_name: {}".format(data["country_name"]))
    Data.append("country_code: {}".format(data["country_code"]))
    Data.append("country_code_iso3: {}".format(data["country_code_iso3"]))
    Data.append("country_capital: {}".format(data["country_capital"]))
    Data.append("country_tld: {}".format(data["country_code"]))
    Data.append("continent_code: {}".format(data["continent_code"]))
    Data.append("in_EU: {}".format(data["in_eu"]))
    Data.append("postal: {}".format(data["postal"]))
    Data.append("latitude: {}".format(data["latitude"]))
    Data.append("longitude: {}".format(data["longitude"]))
    Data.append("timezone: {}".format(data["timezone"]))
    Data.append("utc_offset: {}".format(data["utc_offset"]))
    Data.append("country_calling_code: {}".format(data["country_calling_code"]))
    Data.append("currency: {}".format(data["currency"]))
    Data.append("currency_name: {}".format(data["currency_name"]))
    Data.append("languages: {}".format(data["languages"]))
    Data.append("country_area: {}".format(data["country_area"]))
    Data.append("country_population: {}".format(data["country_population"]))
    Data.append("asn: {}".format(data["asn"]))
    Data.append("org: {}".format(data["org"]))

    return Data

if __name__=="__main__":
    Data=get_location('8.8.8.8')
    for i in range(Data):
        print(Data[i])
