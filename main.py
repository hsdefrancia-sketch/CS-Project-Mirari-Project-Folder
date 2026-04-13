import json
import time

try:
    # Load the JSON files
    with open('floris.json', 'r') as f:
        floris_data = json.load(f)

    with open('ferae.json', 'r') as f:
        ferae_data = json.load(f)

    with open('souls.json', 'r') as f:
        souls_data = json.load(f)

        # ANSI codes (DECORATIVE TEXT FORMATS)
    red = "\033[0;31m"
    green = "\033[0;32m"
    blue = "\033[0;34m"
    purple = "\033[0;35m"
    cyan = "\033[0;36m"
    yellow = "\033[1;33m"
    italic = "\033[3m"
    reset = "\033[0m"

    # Interface for project Mirari
    print("Welcome to our game!")
    print("Drumroll Please !!!!!!!!")
    time.sleep(.5)
    print(".---.             _             .-.   .-..-. _                   _ "
          "\n: .; :           :_;           .' `.  : `' ::_;                 :_;"
          "\n:  _.'.--.  .--. .-. .--.  .--.`. .'  : .. :.-..--.  .--.  .--. .-."
          "\n: :   : ..'' .; :: :' '_.''  ..': :   : :; :: :: ..'' .; ; : ..': :"
          "\n:_;   :_;  `.__.': :`.__.'`.__.':_;   :_;:_;:_;:_;  `.__,_;:_;  :_;"
          "\n               .-. :                                               "
          "\n               `._.'                                               ")


    # Input
    def get_choice():
        choice = input("Enter your answer [letter only]: ")
        while choice not in ["A", "B", "C", "a", "b", "c"]:
            print("Please enter a valid answer.")
            choice = input("Enter your answer [letter only]: ")
        return choice


    def play_again():
        choice = input("\n Do you want to play again? [y/n]: ")
        while choice not in ["y", "n", "Y", "N"]:
            print("Please enter a valid answer.")
            choice = input("Do you want to play again? [y/n]: ")
        return choice


    # Information about the game
    def mechanics():
        print("You have reached the game mechanics")
        print("1.) Based on your chosen quiz, you will be given a set of questions:>")
        print("2.) Your answers will influence the result of your quiz and your spirit identities.")
        print("3.) Most importantly, express yourself and have fun!!!!:>>")


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


    # Game quizzes
    def mirari_floris():
        sunflower = 0
        hydrangea = 0
        carnation = 0

        for i in floris_data:
            print("\n" + i["question"])
            print(f"A. {i["A"]}")
            print(f"B. {i["B"]}")
            print(f"C. {i["C"]}"

            choice = get_choice()
            if choice == "A" or choice == "a":
                sunflower = sunflower + 1
            elif choice == "B" or choice == "b":
                hydrangea = hydrangea + 1
            elif choice == "C" or choice == "c":
                carnation = carnation + 1

        print("\nYour results are:")
        time.sleep(1)
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


    def mirari_ferae():
        lion = 0
        horse = 0
        monkey = 0

        for i in floris_data:
            print("\n" + i["question"])
            print(f"A. {i["A"]}")
            print(f"B. {i["B"]}")
            print(f"C. {i["C"]}"

            choice = get_choice()
            if choice == "A" or choice == "a":
                lion = lion + 1
            elif choice == "B" or choice == "b":
                horse = horse + 1
            elif choice == "C" or choice == "c":
                monkey = monkey + 1

        print("\nYour results are:")
        time.sleep(1)
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


    def mirari_souls():
        mermaidQueen = 0
        knight = 0
        fairy = 0

        for i in floris_data:
            print("\n" + i["question"])
            print(f"A. {i["A"]}")
            print(f"B. {i["B"]}")
            print(f"C. {i["C"]}"

            choice = get_choice()
            if choice == "A" or choice == "a":
                mermaidQueen = mermaidQueen + 1
            elif choice == "B" or choice == "b":
                knight = knight + 1
            elif choice == "C" or choice == "c":
                fairy = fairy + 1

        print("\nYour results are:")
        time.sleep(1)
        if max(mermaidQueen, fairy, knight) == fairy:
            print("Your spirit flower is the carnation,"
                  "\n you are usually fancy and delicate"
                  "\n keep dedicating yourself!!")
        elif max(mermaidQueen, fairy, knight) == knight:
            print("Your spirit flower is the hydrangea,"
                  "\n you are subtle and gentle"
                  "\n keep you humility glowing!!")
        elif max(mermaidQueen, fairy, knight) == mermaidQueen:
            print("Your spirit flower is the sunflower,"
                  "\n you bring light to every day"
                  "\n keep being the light of your own life!!")


    # Main
    while True:
        time.sleep(.2)
        print("Main Menu:")
        print(" 1. Mirari Floris, What type of Flower are you?"
              "\n 2. Mirari Ferae, What type of Fauna are you?"
              "\n 3. Mirari Souls, What is your Fantasy Background?"
              "\n 4. Game Description"
              "\n 5. Game Mechanics"
              "\n 6. Exit")

        try:
            choice = int(input("Enter a number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            mirari_floris()
        elif choice == 2:
            mirari_ferae()
        elif choice == 3:
            mirari_souls()
        elif choice == 4:
            desciptions()
        elif choice == 5:
            mechanics()
        elif choice == 6:
            print("Goodbye have a nice day!!")
            break
        else:
            print("Please enter a valid number.")


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")
