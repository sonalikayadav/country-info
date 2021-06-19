"""A python module for returning data about countries, ISO info and states/provinces within them."""
#coding = utf-8
from countryinfo import CountryInfo
countryName = input("enter any countryname to get full info:")
country = CountryInfo(countryName)
n = country.info()
for key, values in n.items():
    print(f"{key} => {values}")
