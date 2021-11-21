import random

n = 1000000;
dice = [1, 2, 3, 4, 5, 6]
def roll():
    number_rolls = 0;
    sum = 0;
    while sum < 20:
        rolls = random.randint(1,6)
        if sum % rolls == 0:
            sum = sum + rolls
        else:
            sum = sum - rolls
            if sum < 0:
                sum = 0
        number_rolls = number_rolls + 1
        '''print(str(number_rolls), "roll is:", str(rolls), "sum is:", str(sum))'''
    return number_rolls
def main():
    total_sum = 0
    for i in range(0, n):
        itr = roll()
        total_sum = total_sum + itr
        '''print(i + 1, "roll times is:", str(itr))'''
    print("average times to goal state is", total_sum / n)


for row in range(0,20):
    output = [0]*21
    sum21 = 0
    sum1 = 0
    for col in range(row + 1,row + 7):
        if (row)%(col - row) == 0:
            if col < 20:
                output[col] = 1
            else:
                sum21 = sum21 + 1
        else:
            sub = 2*row - col;
            if sub > 0:
                output[sub] = 1
            else:
                sum1 = sum1 + 1
    output[0] = sum1
    output[20] = sum21
    print(output)
absorb = [0] * 21
absorb[20] = 1
print(absorb)
