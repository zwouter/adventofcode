inp = open("data22").read().split("\n\nPlayer 2:\n")

inp = [i.split("\n") for i in inp]

player1 = list(map(int, inp[0][1:]))
player2 = list(map(int, inp[1]))

while player1 and player2:
    card1 = player1[0]
    card2 = player2[0]
    player1.remove(card1)
    player2.remove(card2)
    if card1 > card2:
        player1.append(card1)
        player1.append(card2)
    else:
        player2.append(card2)
        player2.append(card1)

winner = player1 if player1 else player2

print(sum((len(winner) - i) * winner[i] for i in range(len(winner))))


