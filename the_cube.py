#a small little collaboration project with a good comrade: @alialyasinn (Instagram)

x = " The cube "
print(x.center(30, "-"))

for r in range(1, 16):
    for c in range(1, 16):
        if (r == 1 and c == 6) or (r == 1 and c == 15) or (r == 6 and c == 1):
            print("*", end=" ")
        elif (r == 6 and c == 10) or (r == 15 and c == 1) or (r == 15 and c == 10) or (c == 15 and r == 10):
            print("*", end=" ")
        elif (r + c == 7) or (r + c == 16 and r < 7) or (c + r == 25):
            print("/", end=" ")
        elif (r == 6 and c < 11) or (r == 15 and c < 11) or (c > 5 and r < 2):
            print("-", end=" ")
        elif (c == 15 and c + r <= 25) or (c == 10 and r > 5) or (c == 1 and r > 5):
            print("|", end=" ")
        elif (1 < c < 10) and (6 < r < 15):
            print("@", end=" ")
        elif (7 < r + c < 16) and (2 < c < 14) and (1 < r < 6):
            print("%", end=" ")
        elif (16 < c + r < 25) and (10 < c < 15) and (2 < r < 14):
            print("4", end=" ")
        else:
            print(end="  ")
    print("")