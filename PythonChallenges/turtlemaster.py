board = []
for i in range(8):
    line = input()
    board.append([c for c in line])
actions = input()
dir = [0, 1]
pos = [7, 0]
for action in actions:
    if action == "L":
        x = dir[0]
        y = dir[1]
        dir[0] = -y
        dir[1] = x
    if action == "R":
        x = dir[0]
        y = dir[1]
        dir[0] = -y
        dir[1] = x
    