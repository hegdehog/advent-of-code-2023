path = "input.txt"

with open(path) as f:
    lines = f.read().splitlines()


total = 0
subtotal = []
for line in lines:
    idGame = int(line.split(":")[0].split(" ")[1])
    check  = True

    blue=red=green=0
    for games in line.split(":")[1].strip().split("; "):
        games = games.strip().split(',')

        for gameSets in games:
            gameSets = gameSets.strip().split(" ")
            if ((gameSets[1] == "blue" and int(gameSets[0]) > 14) or     
                (gameSets[1] == "red" and int(gameSets[0]) > 12) or
                (gameSets[1] == "green" and int(gameSets[0]) > 13)) :
                check = False
      

            blue  = int(gameSets[0]) if gameSets[1] == "blue" and int(gameSets[0]) > blue  else blue
            red   = int(gameSets[0]) if gameSets[1] == "red" and int(gameSets[0]) > red else red
            green = int(gameSets[0]) if gameSets[1] == "green" and int(gameSets[0]) > green else green
               
    # part 1
    total += idGame if check else 0

    # part 2
    subtotal.append(blue*green*red)


print(total)
print(sum(subtotal))