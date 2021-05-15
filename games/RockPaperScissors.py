import random


rock = 1
paper = 2
scissors = 3

names = {rock: "Rock", paper: "Paper", scissors: "Scissors"}
rules = {rock: scissors, paper: rock, scissors: paper}

player_score = 0
computer_score = 0


def start():
    print("Lets play Rock, Paper, Scissors!!")
    while game():
        pass
    scores()


def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()


def move():
    while True:
        player = input("1: Rock\n2: Paper\n3: Scissors\nMake your move: ")

        try:
            player = int(player)
            if player in (1, 2, 3):
                return player

        except ValueError:
            print("Please enter 1, 2 or 3")


def result(player, computer):
    global player_score, computer_score

    print("Computer's move: {}".format(names[computer]))

    if player == computer:
        print("Tie!!")
    else:
        if rules[player] == computer:
            print("You win!! :)")
            player_score += 1
        else:
            print("Sorry, you lost! :(")
            computer_score += 1


def play_again():
    answer = input("Would you like to play again (y/n): ")

    if answer in ('y', 'Y', 'yes', 'YES', 'Yes'):
        return answer
    else:
        print("Thanks for playing the game!")


def scores():
    global player_score, computer_score

    print("---------- FINAL SCORES ----------------")
    print("Computer: {}".format(computer_score))
    print("You: {}".format(player_score))


if __name__ == '__main__':
    start()


