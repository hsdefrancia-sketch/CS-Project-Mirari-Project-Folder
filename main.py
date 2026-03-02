#Interface for project Mirari
print("Welcome to our game")
print(" ____  ____  _____   ____  ____  ___  ____    __  __  ____  ____    __    ____  ____ ")
print("(  _ \(  _ \(  _  ) (_  _)( ___)/ __)(_  _)  (  \/  )(_  _)(  _ \  /__\  (  _ \(_  _)")
print(" )___/ )   / )(_)( .-_)(   )__)( (__   )(     )    (  _)(_  )   / /(__)\  )   / _)(_")
print("(__)  (_)\_)(_____)\____) (____)\___) (__)   (_/\/\_)(____)(_)\_)(__)(__)(_)\_)(____)")

#switch the ascii art with this
#▄▄▄▄▄▄▄                                       ▄▄▄      ▄▄▄
#███▀▀███▄              ▀▀              ██     ████▄  ▄████ ▀▀                    ▀▀
#███▄▄███▀ ████▄ ▄███▄  ██ ▄█▀█▄ ▄████ ▀██▀▀   ███▀████▀███ ██  ████▄  ▀▀█▄ ████▄ ██
#███▀▀▀▀   ██ ▀▀ ██ ██ ▀██ ██▄█▀ ██     ██     ███  ▀▀  ███ ██  ██ ▀▀ ▄█▀██ ██ ▀▀ ██
#███       ██    ▀███▀  ██ ▀█▄▄▄ ▀████  ██     ███      ███ ██▄ ██    ▀█▄██ ██    ██▄
#                      ██
#                    ▀▀▀

print("The following are the options you can choose for the quizzes")
print("1.) Mirari Floris, What type of Flower are you?")
print("2.) Mirari Ferae, What type of Fauna are you?")
print("3.) Mirari Souls, What is your fantasy background?")
print("4.) exit, i no wanna play")
print("5.) play again")
print("6.) Our game mechanics")

def mechanics():
    print("1.) Based on your chosen quiz you will be given a set of questions:>")
    print("2.) Your answers will influence the result of your quiz and your spirit identities")
    print("3.) Most importantly is to express yourself and have fun!!!!:>>")
    return mechanics()

choice = input("Please input the NUMBER of your choice:")
if choice == "6":
    print("You have reached the game mechanics")
    
