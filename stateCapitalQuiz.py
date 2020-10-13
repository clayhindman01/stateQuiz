from random import randint

#Dictionary that contains all the states and their capitals.
stateDict = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix",
            "Arkansas": "Little Rock", "California": "Sacramento", "Colorado": "Denver",
            "Connecticut": "Hartford", "Delaware": "Dover", "Florida": "Tallahassee",
            "Georgia": "Atlanta", "Hawaii": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield",
            "Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", "Kentucky": "Frankfort",
            "Louisiana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis", "Massachusetts": "Boston",
            "Michigan": "Lansing", "Minnesota": "Saint Paul", "Mississippi": "Jackson",
            "Missouri": "Jefferson City",  "Montana": "Helena", "Nebraska": "Lincoln", "Nevada": "Carson City",
            "New Hampshire": "Concord", "New Jersey": "Trenton",  "New Mexico": "Santa Fe",
            "New York": "Albany", "North Carolina": "Raleigh", "North Dakota": "Bismarck",
            "Ohio": "Columbus", "Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pennsylvania": "Harrisburg",
            "Rhode Island": "Providence", "South Carolina": "Columbia", "South Dakota": "Pierre",
            "Tennessee": "Nashville", "Texas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier",
            "Virginia": "Richmond", "Washington": "Olympia", "West Virginia": "Charleston",
            "Wisconsin": "Madison",  "Wyoming": "Cheyenne"}

states = list(stateDict.keys())

incorrect_answers = []

#Driver Method
def main():

    #Initialize local variables
    counter = 0
    incorrect = 0

    #Repeats 5 times
    while counter != 5:

        random_state = states[randint(0, len(states))]
        user_answer = input("What is the capital of {:}? ".format(random_state)).title()

        if user_answer != stateDict[random_state]:

            #Appends the questions you missed to a list so they can be referrenced later
            incorrect_answers.append(random_state)
            incorrect += 1

        counter += 1
    
    #Print how many problems you missed
    if incorrect_answers == 1:
        print("You missed {0:} question.".format(incorrect))
    #Prints same thing as before but adds the 's' to the end of question if the number of questions missed was not 1
    else:
        print("You missed {0:} questions.".format(incorrect))

    #Print the answers for the questions you missed
    for i in range(len(incorrect_answers)):
        print("{1:} is the capital of {0:}.".format(incorrect_answers[i], stateDict[incorrect_answers[i]]))


    
main()