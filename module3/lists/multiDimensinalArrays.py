rooms = [
    [[False for room in range(20)] for floor in range(15)] for building in range(3)
]
rooms[1][9][13] = True
vacancy = 0

for roomNum in range(20):
    if not rooms[2][14][roomNum]:
        vacancy += 1

print(vacancy)
