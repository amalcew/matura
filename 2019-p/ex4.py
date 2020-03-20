p1 = open("data/plansza.txt")
board = []
p2 = open("data/robot.txt")
players = []

for line in p1:
    line = line.rstrip().split()
    line = list(map(int, line))
    board.append(line)

for player in p2:
    player = player.rstrip()
    players.append(player)


max_score = 0
player_number = 0
scores = []
eliminated = []
for i in range(len(players)):
    player = players[i]
    points = 0
    position = {"x": 0, "y": 0}
    turn = list(player)
    for j in range(len(turn)):
        move = turn[j]
        if move == "N":
            position["y"] = position["y"] - 1
        if move == "S":
            position["y"] = position["y"] + 1
        if move == "E":
            position["x"] = position["x"] + 1
        if move == "W":
            position["x"] = position["x"] - 1

        if position["x"] < 0 or position["x"] > 19 or position["y"] < 0 or position["y"] > 19:
            # GAME OVER
            eliminated.append(player)
            scores.append(0)
            break
        else:
            points += board[position["y"]][position["x"]]
    # PLAYER WON
    if points > max_score:
        max_score = points
        player_number = i+1


def ex_1():
    print("Eliminated players: "+str(len(eliminated)))


def ex_2():
    print("Max score: "+str(max_score)+" - player"+str(player_number))

ex_1()
ex_2()