from countryinfo import CountryInfo

OPTIONS = [
          "area","capital","provinces","other name",
          "borders","call code","capital position", 
          "currency","population"
          ]

def getCountryInfo(name, infoType):
    country = CountryInfo(name)
    infoType = infoType.lower()
    if(infoType == "area"):
        return country.area()
    if(infoType == "capital"):
        return country.capital()
    if(infoType == "provinces"):
        return country.provinces()
    if(infoType == "other name"):
        return country.alt_spellings()
    if(infoType == "borders"):
        return country.borders()
    if(infoType == "call code"):
        return country.calling_codes()
    if(infoType == "capital"):
        return country.capital()
    if(infoType == "capital position"):
        return country.capital_latlng()
    if(infoType == "currency"):
        return country.currencies()
    if(infoType == "population"):
        return country.population()
    else:
        return "Invalid Option"

choice = "yes"
while choice == "yes":
    countryName = input("Enter Country Name: ")
    print("Type option to show: ")
    for option in OPTIONS:
        print("* " + option)
    selectedOption =input("Option: ")
    print(getCountryInfo(countryName, selectedOption))
    choice = input("Do you want info for another country?: ")