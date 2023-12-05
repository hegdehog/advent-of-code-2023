path = "input.txt"

with open(path) as f:
    lines = f.read().splitlines()


def checkPart( string, positions):
      check_positions = positions + [p - 1 for p in positions if p > 0] + [p + 1 for p in positions if p < len(string) - 1]
      return any(not string[pos].isnumeric() and string[pos] != "." for pos in check_positions)   

totalParts=totalGears=0
for lineNum, line in enumerate(lines):
    number =""
    positions=[]
    check = False
    for i in range(len(line)):
        #part1
        if line[i].isnumeric():
            number += line[i]
            positions.append(i)
        
        if number != "" and (i == len(line)-1 or not line[i+1].isnumeric()):
            check_positions = [lineNum - 1, lineNum, lineNum + 1]
            checks = [checkPart(lines[pos], positions) for pos in check_positions if 0 <= pos < len(lines)]
            if any(checks):
                totalParts += int(number)
        

            number = ""
            positions=[]
            check = False
        

#part1    
print(totalParts)


  
