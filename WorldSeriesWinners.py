
#Open the WorldSeriesWinners.txt file 
infile = open("WorldSeriesWinners.txt",'r')

#Create an empty list for winners and append the teams 
winners = []

for team in infile:
    team = team.rstrip('\n')
    winners.append(team)

#Create an empty dictionary of the win counts and count team wins 
wincount= dict()

for team_wins in winners:
    counter = winners.count(team_wins)
    wincount[team_wins] = counter


yearlist = []
win_years= dict()

#Iterate through the years of each World Series 
for year in range (1903,2009):
    #Skip the two year entries not in the database and append the others
    if year == 1904 or year == 1994:
        continue
    else:
        yearlist.append(year)

#Append the winning years data from list to dictionary
for key in yearlist:
    for value in winners:
        win_years[key] = value
        winners.remove(value)
        break 


#Prompt the user to enter a World Series year 
input_year = int(input('\nEnter a year from 1903-2008: '))

#Check if the input year is valid 
#Display the team that won 
if input_year == 1904 or input_year == 1994:
    print("No record of World Series during this year.")
elif input_year < 1993 or input_year > 2008:
    print("Enter a valid year within the mentioned range.")
else:
    if input_year in win_years:
        print("The team that won in ", input_year, " was the ",\
             win_years[input_year], sep = '')

print("\n\n***List of total wins from each team.***")
for key in list(wincount.keys()):
    print(key, ": ",wincount[key], sep = '')