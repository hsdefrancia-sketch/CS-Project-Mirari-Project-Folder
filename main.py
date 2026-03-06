import json

try:
    # READING from the file
    filename = "questions.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

# Interface for project Mirari
    print("Welcome to our game")
    print(".---.             _             .-.   .-..-. _                   _ "
            "\n: .; :           :_;           .' `.  : `' ::_;                 :_;"
            "\n:  _.'.--.  .--. .-. .--.  .--.`. .'  : .. :.-..--.  .--.  .--. .-."
            "\n: :   : ..'' .; :: :' '_.''  ..': :   : :; :: :: ..'' .; ; : ..': :"
            "\n:_;   :_;  `.__.': :`.__.'`.__.':_;   :_;:_;:_;:_;  `.__,_;:_;  :_;"
            "\n               .-. :                                               "
            "\n               `._.'                                               ")

    print("Main Menu:")
    print(" 1. Mirari Floris, What type of Flower are you?"
            "\n 2. Mirari Ferae, What type of Fauna are you?"
            "\n 3. Mirari Souls, What is your Fantasy Background?"
            "\n 4. Game mechanics"
            "\n 5. Play again"
            "\n 6. Exit, I don't want to play.")


    def mechanics():
        print("You have reached the game mechanics")
        print("1.) Based on your chosen quiz, you will be given a set of questions:>")
        print("2.) Your answers will influence the result of your quiz and your spirit identities.")
        print("3.) Most importantly, express yourself and have fun!!!!:>>")
        return mechanics()


    def mirari_floris():
        for questions in data:
            if questions["quiz_name"] == ["mirari_floris"]:
                print(questions["questions"])
                print(questions["options"])
                choice = input("Enter your anser [letter only] ")
                while choice == "A" or choice == "B" or choice == "C":
                        if choice == "A":
                                sunflower = sunflower + 1
                        elif choice == "B":
                                hydrangea = hydrangea + 1
                        elif choice == "C":
                                carnation = carnation + 1
                        else:
                                print("Please enter a valid answer.")
                
        return mirari_floris()

    def mirari_ferae():
        for questions in data:
            if questions["quiz_name"] == ["mirari_ferae"]:
                print(questions["questions"])
        return mirari_ferae()
        #the flowers are sunflower hydreangea and Carnation btw
    def mirari_souls():
        for questions in data:
            if questions["quiz_name"] == ["mirari_souls"]:
                print(questions["questions"])
                print(questions["options"])
                
                        
        return mirari_souls()
    

    def desciptions():
        for questions in data:
            print(questions["descriptions"])
        return desciptions()

    def play_again():
        print("Main Menu:")
        print(" 1. Mirari Floris, What type of Flower are you?"
                "\n 2. Mirari Ferae, What type of Fauna are you?"
                "\n 3. Mirari Souls, What is your Fantasy Background?"
                "\n 4. Game mechanics"
                "\n 5. Play again"
                "\n 6. Exit, I don't want to play.")

    def exit():
        print("Goodbye have a nice day!!")
        return exit()


    choice = int(input("Please input the NUMBER of your choice: "))

    if choice == 6:
        print(mechanics())
    elif choice == 1:
        print(mirari_floris())
    elif choice == 2:
        print(mirari_ferae())
    elif choice == 3:
        print(mirari_souls())
    elif choice == 4:
        print(desciptions())
    elif choice == 5:
        print(exit())


    print("Your results are:")
    floris_results = max(sunflower, hydrangea, carnation)
    if max(sunflower, hydrangea, carnation) == carnation:
            print("Your spirit flower is the carnation,"
                  "\n you are usually fancy and delicate"
                  "\n keep dedicating yourself!!")
    elif max(sunflower, hydrangea, carnation) == hydrangea:
            print("Your spirit flower is the hydrangea,"
                  "\n you are subtle and gentle"
                  "\n keep you humility glowing!!")
    elif max(sunflower, hydrangea, carnation) == sunflower:
            print("Your spirit flower is the sunflower,"
                  "\n you bring light to every day"
                  "\n keep being the light of your own life!!")
        


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")



