import random


print("Let's play a game of Rock, Paper and Scissors. \n")

print("Rules:-")
print("(i) We have 10 Rounds where you need to Pick One of the Three - 'Rock', 'Paper' or 'Scissors'")
print("(ii) Rock Beats Scissors and Loses to Paper, Paper Beats Rock and Loses to Scissors,")
print("     Scissors Beats Paper and Loses to Rock.")
print("(iii) At the End of Each Round we'll let you know who Won and we'll provide the Results at the End of the Game.")

Round = 1
AI = 0
User = 0

while Round <= 10:
    List = ["Rock", "Paper", "Scissors"]
    Process = random.choice(List)
    Input = input("\n Enter Rock, Paper or Scissors: ").capitalize()

    if Process == "Rock" and Input == "Paper":
        print("AI's Input:", Process)
        print("Your Input:", Input)
        print("Hence, You Win.")

        Round = Round + 1
        User = User + 1

    elif Process == "Rock" and Input == "Scissors":
        print("AI's Input:", Process)
        print("Your Input:", Input)
        print("Hence, AI Wins.")

        Round = Round + 1
        AI = AI + 1

    elif Process == "Paper" and Input == "Rock":
        print("AI's Input:", Process)
        print("Your Input:", Input)
        print("Hence, AI Wins.")

        Round = Round + 1
        AI = AI + 1

    elif Process == "Paper" and Input == "Scissors":
        print("AI's Input:", Process)
        print("Your Input:", Input)
        print("Hence, You Win.")

        Round = Round + 1
        User = User + 1

    elif Process == "Scissors" and Input == "Rock":
        print("AI's Input:", Process)
        print("Your Input:", Input)
        print("Hence, You Win.")

        Round = Round + 1
        User = User + 1

    elif Process == "Scissors" and Input == "Paper":
        print("AI's Input:", Process)
        print("Your Input:", Input)
        print("Hence, AI Wins.")

        Round = Round + 1
        AI = AI + 1

    elif Process == Input:
        print("AI's Input:", Process)
        print("Your Input:", Input)
        print("Hence, It's a Draw. Round not Counted.")

    else:
        print("Wrong Input. Try Again.")


print("\n\n Scoreboard:-")
print("Your Score:", User)
print("AI's Score:", AI, "\n")



if User > AI:
    print("You WON the Game by", User - AI, "Points.")

elif AI > User:
    print("AI WON the Game by", AI - User, "Points.")

elif User == AI:
    print("We have a Tied Game.")
