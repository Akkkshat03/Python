matchsticks = 21
while matchsticks > 1:
    user_pick = int(input("Pick 1, 2, 3, or 4 matchsticks: "))
    if user_pick not in [1, 2, 3, 4]:
        print("Invalid input. Pick again.")
        continue
    matchsticks -= user_pick
    computer_pick = 5 - user_pick
    print(f"Computer picks {computer_pick} matchsticks.")
    matchsticks -= computer_pick
    print(f"Matchsticks left: {matchsticks}")
if matchsticks == 1:
    print("You are forced to pick the last matchstick. You lose!")
