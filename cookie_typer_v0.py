from random import sample
from time import perf_counter
import getpass
import pickle
try:
    passwords = pickle.load(open("passwords.pkl", "rb"))
except:
    passwords = {}
    
try:
    high_scores = pickle.load(open("high_scores.pkl", "rb"))
except:
    high_scores = {}
    
try:
    win_count = pickle.load(open("win_count.pkl", "rb"))
except:
    win_count = {}
# Not a good idea for security. 

# If you get FileNotFoundError:
# Run it once with an empty dictionary there
# Enter a username/password combo in singleplayer
# Add the correct code back
# Try again

def prevent_copy_paste(word):
    # Takes in a word and outputs a version that cannot be easily
    # copypasted.
    # I suggest adding a space in between each letter.
    # Hint 1: Strings behave like tuples. You can index them to grab letters.
    # Hint 2: Loop over the string and use string concatenation to BUILD the
    # output up.
    output = ""
    for letter in word:
        output += letter + " " # choose a space or a \u200c
    return output.rstrip()

def scoring(length, time):
    # Takes in a length of the word and a time the user took
    # and gives an appropriate score.
    lps = length / time
    return min(lps, 30)

def load_wordlist(filename="safedict_full.txt"):
    f = open(filename)
    wordlist = f.readlines()
    f.close()
    return wordlist

def load_data(players):
    global passwords
    scores = []
    names = []
    for i in range(players):
        scores.append(0)
        name = input(f"Player {i+1}, please enter your name: ")
        if name in passwords:
            # ask for password!
            print(f"Welcome back, {name}!")
            password = getpass.getpass("Please enter your password: ")
            # correct password is passwords[name]
            while password != passwords[name]:
                print("That password is incorrect.")
                password = getpass.getpass("Please enter your password: ")
        else:
            # register the user :D
            print("You have not yet registered.")
            password = getpass.getpass("Please set your password now: ")
            passwords[name] = password
            print("Password set successfully!")
        names.append(name)
    pickle.dump(passwords, open("passwords.pkl", "wb"))
    return scores, names
# email to: eyang10000@gmail.com

def scoreboard(scores, names):
    sorted_names_and_scores = sorted(zip(scores, names), reverse=True)
    # Outputs a list containing:
    # [(50, "Eric"), (25, "Ernest"), (10, "Edwin")]

    print("Scoreboard: ")
    for score, name in sorted_names_and_scores:
        print(f"{name} - {round(score, 2)} points")
        # print the scoreboard here
    
    # eyang10000@gmail.com

    return sorted_names_and_scores

def game(players):
    scores, names = load_data(players)
    for i in range(players):
        words = sample(wordlist, 10)

        print(f"\n{names[i]}, you're up!\n")

        for word in words:
            word = word.rstrip()

            input("When you are ready, press ENTER to proceed.")

            start_time = perf_counter()

            print(f"Type the word {prevent_copy_paste(word)}")

            guess = input()

            while guess != word and guess != "debug_anbbububjsnd":
                guess = input("Wrong! Try again: ")

            end_time = perf_counter()

            points = scoring(len(word), end_time - start_time)
            scores[i] += points
            print(f"{names[i]}, you scored {round(points, 2)} points.")
            print(f"Your score thus far: {round(scores[i], 2)}")

        # store high score
        if names[i] in high_scores:
            # update it
            if scores[i] > high_scores[names[i]]:
                print("That's a new record!")
                high_scores[names[i]] = scores[i]
        else:
            # add it to highscores
            print("That's a new record!")
            high_scores[names[i]] = scores[i]
        pickle.dump(high_scores, open("high_scores.pkl", "wb"))
        
        board = scoreboard(scores, names)
    winner = board[0][1]

    if players > 1:
        if winner in win_count:
            win_count[winner] += 1
        else:
            win_count[winner] = 1
        pickle.dump(win_count, open("win_count.pkl", "wb"))
    print(f"The winner is {board[0][1]}!")

def print_menu():
    print("Type 1 to start a game.")
    print("Type 2 to view high scores.")
    print("Type 3 to view win counts.")
    print("Type 4 to exit.")

def sort_scoreboard(scoreboard):
    people = []
    for name, score in scoreboard.items():
        people.append((score, name))

    return sorted(people, reverse=True) # sort descending
            

if __name__ == "__main__": # be courteous to people loading our module!
    wordlist = load_wordlist()

    print("Welcome to Cookie Typer (R) (C) TM! This fun [citation needed] typing game")
    print("will improve your typing skills!")

    while True:
        print_menu()
        
        choice = input("What would you like to do? ")

        if choice == "1":
            while True:
                try:
                    num_players = int(input("How many players are playing? "))
                except ValueError:
                    print("I didn't understand that.")
                    continue
                
                if num_players < 1:
                    print("There must be at least 1 player.")
                    continue
                
                break
            
            game(num_players)
        elif choice == "2":
            # view high scores
            
            for score, name in sort_scoreboard(high_scores):
                print(f"{name} - {round(score, 2)}")    
        elif choice == "3":
            # view win counts
            
            for score, name in sort_scoreboard(win_count):
                print(f"{name} - {score}")    
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("I didn't understand that...")

# Improvements:
# Add a win count dictionary
# Add a menu that allows you to view scoreboard data (win counts, high scores, etc.)
# Email code to eyang10000@gmail.com
# TEST BEFORE YOU SEND

# Email: eyang10000@gmail.com
