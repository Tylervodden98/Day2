import math
game = int(input("BO3 or BO5?, enter 3 or 5"))
bestof = math.floor(game / 2) + 1
p1_score = 0
p2_score = 0
while p1_score < bestof and p2_score < bestof:
    # Get user 1 input r,p,s
    player1 = input(
        "Player1, please enter r,p,s for Rock, Paper, or Scissors: ")
    player1 = player1.lower()
    print(player1)
    check_valid1 = False
    if player1 != "r" and player1 != "p" and player1 != "s":
        print("Please enter valid input of 'r','p' or 's'")
    else:
        check_valid1 = True

    # Get user 2 input r,p,s
    player2 = input(
        "Player 2, please enter r,p,s for Rock, Paper, or Scissors: ")
    player2 = player2.lower()
    print(player2)
    check_valid2 = False
    if player2 != "r" and player2 != "p" and player2 != "s":
        print("Please enter valid input of 'r','p' or 's'")
    else:
        check_valid2 = True

    if check_valid1 == True and check_valid2 == True:
        # Play r,p,s
        # First check if they chose the same option
        if player1 == player2:
            print(f"Both Players chose {player1}, it's a tie!")
        elif player1 == "r" and player2 == "s":
            print("Player 1 wins!")
            p1_score += 1
            game -= 1
        elif player1 == "p" and player2 == "r":
            print("Player 1 wins!")
            p1_score += 1
            game -= 1
        elif player1 == "s" and player2 == "p":
            print("Player 1 wins!")
            p1_score += 1
            game -= 1
        else:
            # All other cases P2 wins
            print("Player 2 wins!")
            p2_score += 1
            game -= 1
    else:
        if check_valid1 == False:
            print("Player 1 has an invalid input")
        else:
            print("Player 2 has an invalid input")
else:
    if p1_score > p2_score:
        print(
            f"Player 1 wins with a score of {p1_score} to Player 2's score of {p2_score}")
    else:
        print(
            f"Player 2 wins with a score of {p2_score} to Player 1's score of {p1_score}")
