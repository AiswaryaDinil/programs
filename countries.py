# print total no of country details
import json

with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)
print(len(data))

def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]
# print lang of Ukraine

lang_country=[lang["languages"] for lang in data if lang["name"]=="India"]
languages=[lang["name"] for lang in lang_country[0]]
print(languages)

# print currency in china

currency_country=[cur["currencies"] for cur in data if cur["name"]=="Western Sahara"]
currency=[cur["name"] for cur in currency_country[0]]
print(currency)

# print population of india

india_popu=[p["population"] for p in data if p["name"]=="India"]
print(india_popu)

# print neighbouring countries

country_data=get_country_data("france")
# print(country_data)
country_borders=country_data[0].get("borders")
border_of_india=[country["name"] for country in data if country["alpha3Code"] in country_borders]
print(border_of_india)

# highest population

# high_popul=max([country["population"] for country in data])
# print(high_popul)
populated_country=max(data,key=lambda d:d.get("population"))
print(populated_country["name"])

# lowest population

low_populated_country=min(data,key=lambda d:d.get("population"))
print(low_populated_country["name"])

