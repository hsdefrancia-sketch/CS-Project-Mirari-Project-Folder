import json
import time

try:
    # READING from the file
    filename = "floris.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

    filename = "ferae.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

    filename = "souls.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

	# Ansi codes
	red = "\e[1;31m"
	green = "\e[1;32m"
	yellow = "\e[1;33m"
	blue = "\e[1;34m"
	purple = "\e[1;35m"
	cyan = "\e[1;36m"
		
    # Interface for project Mirari
    print("Welcome to our game")
    print("Drumroll Please !!!!!!!!")
    time.sleep(2)
    print(".---.             _             .-.   .-..-. _                   _ "
          "\n: .; :           :_;           .' `.  : `' ::_;                 :_;"
          "\n:  _.'.--.  .--. .-. .--.  .--.`. .'  : .. :.-..--.  .--.  .--. .-."
          "\n: :   : ..'' .; :: :' '_.''  ..': :   : :; :: :: ..'' .; ; : ..': :"
          "\n:_;   :_;  `.__.': :`.__.'`.__.':_;   :_;:_;:_;:_;  `.__,_;:_;  :_;"
          "\n               .-. :                                               "
          "\n               `._.'                                               ")

    time.sleep(1)
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

    sunflower = 0
    hydrangea = 0
    carnation = 0

    def mirari_floris():
        for floris in data:

            print(floris["question"])
            print(floris["A"])
            print(floris["B"])
            print(floris["C"])
            choice = input("Enter your answer [letter only] ")
            while choice == "A" or choice == "B" or choice == "C" or choice == "a" or choice == "b" or choice == "c":
                if choice == "A" or choice == "a":
                    sunflower = sunflower + 1
                elif choice == "B" or choice == "b":
                    hydrangea = hydrangea + 1
                elif choice == "C" or choice == "c":
                    carnation = carnation + 1
                else:
                    print("Please enter a valid answer.")

        return mirari_floris()

    lion = 0
    horse = 0
    monkey = 0
    def mirari_ferae():
        for ferae in data:
            print(ferae["question"])
            print(ferae["A"])
            print(ferae["B"])
            print(ferae["C"])
            choice = input("Enter your answer [letter only] ")
            while choice == "A" or choice == "B" or choice == "C" or choice == "a" or choice == "b" or choice == "c":
                if choice == "A" or choice == "a":
                    lion = lion + 1
                elif choice == "B" or choice == "b":
                    horse = horse + 1
                elif choice == "C" or choice == "c":
                    monkey = monkey + 1
                else:
                    print("Please enter a valid answer.")
        return mirari_ferae()


    Mermaid_queen = 0
    Knight = 0
    Fairy = 0
    def mirari_souls():
        for souls in data:
            for souls in data:
                print(souls["question"])
                print(souls["A"])
                print(souls["B"])
                print(souls["C"])
                choice = input("Enter your answer [letter only] ")
                while choice == "A" or choice == "B" or choice == "C" or choice == "a" or choice == "b" or choice == "c":
                    if choice == "A" or choice == "a":
                        Mermaid_queen = Mermaid_queen + 1
                    elif choice == "B" or choice == "b":
                        Knight = Knight + 1
                    elif choice == "C" or choice == "c":
                        Fairy = Fairy + 1
                    else:
                        print("Please enter a valid answer.")

        return mirari_souls()


    def desciptions():
        print("Game Description:"
              "\n Our game consists of 3 quizzes that will determine:"
              "\n 1. Your spirit animal!"
              "\n 2. What flower represents you!"
              "\n 3. Your spirit fantasy background!"
              "\n This is a fun and engaging game for everyone."
              "\n Human, monster, unicorns. Whatever you are it doesn't matter."
              "\n What matters is that you enjoy!"
              "\n Have fun!!!")
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
    time.sleep(2)
    if max(sunflower, hydrangea, carnation) == carnation:
        print("""
You appear to be a Carnation, 
	The Florescence deity incarnate

    As vigorous winds attempt to uproot it from love
    It remains fascinating, as it is just a delicate statue
    With nothing else but a deep sense of respect for others""")

    elif max(sunflower, hydrangea, carnation) == hydrangea:
        print("""
You appear to be a Hydrangea
	The Triumphant veil of clouds

	As dreams persist, they hold an abundance of hearts
	Rich with overflowing glam, the prosperity of beauty
	Yet wherever it expresses heartfelt gratitude""")

    elif max(sunflower, hydrangea, carnation) == sunflower:
        print("""
You appear to be a Sunflower
	The Helios’ ultimate laudation

	Hugging the sun with open arms, it cherishes happiness
	The radiating positivity reminds everybody of alms
	When triumphant ends, keep smiling, for it is a beauty""")


    if max(lion, horse, monkey) == lion:
        print("""
You appear to be a Lion
    The embodiment of the mightiest

    For the fierce, and all invigorated by your passion of strife. 
    As the lands rise to climax, the cup's filled with fight
    The Prominent compass of the north is the jurisdiction""")

    elif max(lion, horse, monkey) == horse:
        print("""
You appear to be a Horse
The fleeting-time fluorescence

Galloping restricting chains, disintegrating the choking miasma
For the light from its path restores mankind’s expression
Upon free lands where peculiarity is normality, filled with creativity""")

    elif max(lion, horse, monkey) == monkey:
        print("""
You appear to be a Monkey
    The traversing brilliance of Cor’

    Brazen halos surrounded by fire, as the mind erupts with acumen
    With easy adaptation to the shallow depths with crazed ease
    Abundant brilliance and mischief control the traversing mind""")


    if max(Mermaid_queen, Fairy, Knight) == Fairy:
        print("Your spirit flower is the carnation,"
              "\n you are usually fancy and delicate"
              "\n keep dedicating yourself!!")
    elif max(Mermaid_queen, Fairy, Knight) == Knight:
        print("Your spirit flower is the hydrangea,"
              "\n you are subtle and gentle"
              "\n keep you humility glowing!!")
    elif max(Mermaid_queen, Fairy, Knight) == Mermaid_queen:
        print("Your spirit flower is the sunflower,"
              "\n you bring light to every day"
              "\n keep being the light of your own life!!")


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")


