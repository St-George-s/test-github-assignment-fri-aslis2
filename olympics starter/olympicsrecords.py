import csv

class Country:
    def __init__(self, rank, countryName, countryCode, countryGold, countrySilver, countryBronze, countryMedals):
        self.rank = rank
        self.countryName = countryName
        self.countryCode = countryCode
        self.countryGold = countryGold
        self.countrySilver = countrySilver
        self.countryBronze = countryBronze
        self.countryMedals = countryMedals 


def loadFile():
    file = "olympics starter/olympics2024.csv"
    with open(file, 'r' ) as file:
        reader = csv.reader(file)
        next(reader)
        countries = []
        for row in reader:
            newRecord = Country(row[0], row[1], row[2], int(row[3]), int(row[4]), int(row[5]), int(row[6]))
            countries.append(newRecord)
           
    return countries 


def medalCalculation(countries):
    total_medal = 0
    for i in range(len(countries)):
        total_medal = total_medal + countries[i].countryMedals
    print(total_medal)

def topCountryIdentification(countries):
    max_value = countries[0]
    for country in countries:
        if country.countryMedals > max_value.countryMedals:
           max_value = country
    
    print(max_value.countryName +  " has the highest amount of medals with " + str(max_value.countryMedals) )


def goldMedalReport(countries):
    with open('topCountries.txt', 'w', newline= '' ) as file:
        for country in countries:
            if country.countryGold > 30:
                file.write( country.countryName  + str(country.countryGold)+"\n")
            



#main
countries = loadFile()
medalCalculation(countries)
topCountryIdentification(countries)
goldMedalReport(countries)

