path = "C:\\Users\\GU60TR\\OneDrive - ING\\Documentos\\2. Data Strategy\\5. Advent of code\\advent-of-code-2023\\avd_2023_3\\input.txt"

with open(path) as f:
    input_list = f.read().splitlines()

sum = 0
for y in range(0, len(input_list)):
    for x in range(0, len(input_list[0])):
        nums = []
        if input_list[y][x] == '*':
            length = 1
            x_start = max(0, x-length)
            x_end = min(len(input_list[0])-1, x+1)
            y_start = max(0, y-1)
            y_end = min(len(input_list)-1, y+1)

            considered = []
            for xx in range(x_start, x_end+1):
                for yy in range(y_start, y_end+1):
                    if input_list[yy][xx].isnumeric() and [xx, yy] not in considered:
                        x2 = xx
                        cur_num = []
                        while True:
                            x2 -= 1
                            if x2>=0:
                                if not input_list[yy][x2].isnumeric():
                                    break
                            else:
                                break
                        x2+=1
                        while True:
                            if x2 < len(input_list[0]):
                                if input_list[yy][x2].isnumeric():
                                    considered.append([x2, yy])
                                    cur_num.append(input_list[yy][x2])
                                    x2+=1
                                else:
                                    break
                            else:
                                break
                        nums.append(int("".join(cur_num)))
            if len(nums) == 2:
                sum += nums[0]*nums[1]
print(sum)  