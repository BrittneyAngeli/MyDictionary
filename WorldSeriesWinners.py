

#Read from file 
infile = open("WorldSeriesWinner.txt", "r")

team_name = infile.readline()
#Readline 
infile.readline()

teams_dict = {}
wins_dict = {}

count = 0
for year in range(1903, 2008):
    if year == 1904 or year == 1994: 
        print("No World Series occurred in this year.")
    else: 
        teams_dict[year] = team_name 
        

