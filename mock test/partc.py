import csv 

gameTitles = []
genres = []
ageRatings = []
platform = []

def readGameDataFromCSV():
    with open("mock test/game_platform_data.csv", 'r') as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            gameTitles.append(row[0])
            genres.append(row[1])
            ageRatings.append(row[2])
            platform.append(row[3])

    return gameTitles, genres, ageRatings, platform 
    
def countSuitableGames(genre_to_check, gameTitles, genres, ageRatings):
    count = 0 
    for genre_to_check in genres:
        if genre_to_check == genres + ageRatings < 18 :
            count += 1 
            print(gameTitles[genre_to_check])

def countSuitableGamesPlatform(genre_to_check, gameTitles, genres, ageRatings, platform ):
   with open("platform_suitable_games.txt", 'w', newline= '')as file:
    for genre_to_check in genres:
        if genre_to_check == genres + ageRatings < 18 :
            file.write()

#main
readGameDataFromCSV()
countSuitableGames("Horror", gameTitles, genres, ageRatings)
 countSuitableGamesPlatform(genre_to_check, gameTitles, genres, ageRatings, platform )