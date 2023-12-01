dictPuzzle2 = {"one" : "1", "two" : "2",  "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8",  "nine" : "9"
               ,"1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}

path = "C:\\Users\\GU60TR\\OneDrive - ING\\Documentos\\2. Data Strategy\\5.Advent of code\\1\\stars.txt"

def calcualteTotal( numbers ):
    return  int(numbers[0]) *10 + int(numbers[-1])
with open(path) as f:
    lines = f.read().splitlines()

puzzle2=puzzle1=0
for line in lines:
    subPuzzle2=[]
    subPuzzle1=[]
    for i in range(len(line)):
        #puzzle 1
        if line[i].isnumeric():
            subPuzzle1.append(line[i])

        #puzzle 2
        for key, value in dictPuzzle2.items():
            if line[i:].startswith(key):
                subPuzzle2.append(dictPuzzle2[value])
                break
        
    puzzle1 += calcualteTotal(subPuzzle1)
    puzzle2 += calcualteTotal(subPuzzle2)
    
print("Puzzle 1: " + str(puzzle1))
print("Puzzle 2: " + str(puzzle2))
