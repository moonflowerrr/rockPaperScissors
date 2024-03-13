#ROCK PAPER SCISSORS
import random
import time
import sys

#VARIABLES
rps_list = ["r", "p", "s"]
comp_guess = " "


win = False
win_count = 0

match = False
match_count = 0

lose = False
lose_count = 0


#USER
rock_list = ["    _______", "---'   ____)", "      (_____)", "      (_____)",
    "      (____)",
    "---.__(___)"]

paper_list = ["    _______    ", "---'   ____)____", "          ______)",
    "          _______)", "         _______)", "---.__________) "]

scissors_list = ["    _______    ", "---'   ____)____", "          ______)",
    "          _______)", "      (____)      ", "---.__(___)      "]


#COMPUTER
r_list = ["    _______    ", "  (____   '---", "(_____)      ", "(_____)      ",
    "  (____)      ", "    (___)__.---"]

p_list = ["         _______    ", "   ____(____   '---", " (______          ",
    "(_______          ", " (_______         ", "   (___________.---"]

s_list = ["         _______    ", "   ____(____   '---", " (______          ",
    "(_______          ", "      (____)      ", "        (___)__.---"]


   
   
'''   
("  _______    ")
(" (____   '---")
("(_____)      ")
("(_____)      ")
(" (____)      ")
("  (___)__.---")
  
   
   
   
("       _______    ")
("  ____(____   '---")
(" (______          ")
("(_______          ")
(" (_______         ")
("  (___________.---")
    
    
    
    
("       _______    ")
("  ____(____   '---")
(" (______          ")
("(_______          ")
("      (____)      ")
("       (___)__.---")
    
    
'''



#Ask user for rock paper or scissors
def user_guess():
    global comp_guess
    
    end_game()
    
    comp_guess = random.choice(rps_list)
    
    guess = input("Rock, paper, or scissors? ")
    
    if(guess.lower() == "rock"):
        guess = "r"
    elif(guess.lower() == "paper"):
        guess = "p"
    elif(guess.lower() == "scissors"):
        guess = "s"
    
    rps_shoot()
    guess_check(guess)
    
#Check the user's guess
def guess_check(guess):
    #USER GUESSES ROCK
    #rock vs rock
    if(guess == rps_list[0] and comp_guess == rps_list[0]):
        match = True
        
        for line in range(len(rock_list)):
            print(rock_list[line] + "               " + r_list[line])
        
        draw()
    #rock vs paper
    elif(guess == rps_list[0] and comp_guess == rps_list[1]):
        lose = True
        
        for line in range(len(rock_list)):
            print(rock_list[line] + "               " + p_list[line])
        
        loser()
    #rock vs scissors
    elif(guess == rps_list[0] and comp_guess == rps_list[2]):
        win = True
        
        for line in range(len(rock_list)):
            print(rock_list[line] + "               " + s_list[line])
        
        winner()
    
    #USER GUESSES PAPER
    #paper vs rock
    if(guess == rps_list[1] and comp_guess == rps_list[0]):
        win = True
        
        for line in range(len(paper_list)):
            print(paper_list[line] + "               " + r_list[line])
        
        winner()
    #paper vs paper
    elif(guess == rps_list[1] and comp_guess == rps_list[1]):
        match = True
        
        for line in range(len(paper_list)):
            print(paper_list[line] + "               " + p_list[line])
        
        draw()
    #paper vs scissors
    elif(guess == rps_list[1] and comp_guess == rps_list[2]):
        lose = True
        
        for line in range(len(paper_list)):
            print(paper_list[line] + "               " + s_list[line])
        
        loser()
    
    #USER GUESSES SCISSORS
    #scissors vs rock
    if(guess == rps_list[2] and comp_guess == rps_list[0]):
        lose = True
        
        for line in range(len(scissors_list)):
            print(scissors_list[line] + "               " + r_list[line])
        
        loser()
    #scissors vs paper
    elif(guess == rps_list[2] and comp_guess == rps_list[1]):
        win = True
        
        for line in range(len(scissors_list)):
            print(scissors_list[line] + "               " + p_list[line])
        
        winner()
    #scissors vs scissors
    elif(guess == rps_list[2] and comp_guess == rps_list[2]):
        match = True
        
        for line in range(len(scissors_list)):
            print(scissors_list[line] + "               " + s_list[line])
        
        draw()
    
 

    
    
def rps_shoot():
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    
    print("                 ROCK!")
    print("    _______                  _______    ")
    print("---'   ____)                (____   '---")
    print("      (_____)              (_____)      ")
    print("      (_____)              (_____)      ")
    print("      (____)                (____)      ")
    print("---.__(___)                  (___)__.---")
    
    print(" ")
    time.sleep(1)
    
    print("                 PAPER!")
    print("    _______                  _______    ")
    print("---'   ____)____        ____(____   '---")
    print("          ______)      (______          ")
    print("          _______)    (_______          ")
    print("         _______)      (_______         ")
    print("---.__________)         (___________.---")
    
    print(" ")
    time.sleep(1)
    
    print("               SCISSORS!")
    print("    _______                  _______    ")
    print("---'   ____)____        ____(____   '---")
    print("          ______)      (______          ")
    print("          _______)    (_______          ")
    print("      (____)                (____)      ")
    print("---.__(___)                  (___)__.---")

    print(" ")
    time.sleep(1)

    
    print("                 SHOOT!")
    
    
    
def score():
    global win_count, lose_count
    print("Score: " + str(win_count) + " - " + str(lose_count))
    
def winner():
    global win_count
    
    win_count += 1
    #rps_shoot()
    print("                 Winner!")
    score()
    
def loser():
    global lose_count
    
    lose_count += 1
    #rps_shoot()
    print("                 Loser!")
    score()
    
def draw():
    global match_count, win_count, lose_count
    
    match_count += 1
    #rps_shoot()
    print("               It's a draw!")
    score()



def end_game():
    if(win_count == 3):
        print("You win!")
        sys.exit()
    elif(lose_count == 3):
        print("You lose!")
        sys.exit()



def start_game():
        user_guess()

while True:
    start_game()