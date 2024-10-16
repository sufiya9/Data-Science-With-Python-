import random
lst = ['r','p','s']
i = 0
p1_win = 0
p2_win = 0
while i < 5:
    p1 = input("Rock (r), Paper (p) or Scissor (s) ? ")
    p2 = random.choice(lst)
    print(f"My {p2}")
    if p1 != p2:
        if p1 == 'r':
            if p2 == 'p':
                print("I WON")
                p2_win += 1
            else:
                print("YOU WON")
                p1_win += 1
        elif p1 == 's':
            if p2 == 'r':
                print("I WON")
                p2_win += 1
            else:
                print("YOU WON")
                p1_win += 1
        else:
            if p2 == 's':
                print("I WON")
                p2_win += 1
            else:
                print("YOU WON")
                p1_win += 1
    else:
        print("SAME HERE")
    i += 1

print(f"\nYOU WON {p1_win} ROUNDS")
print(f"\nI WON {p2_win} ROUNDS")

if p2_win > p1_win:
    print("\n I AM WINNER")
elif p2_win < p1_win:
    print("\nYOU ARE WINNER")
else:
    print("\nMATCH DRAW")