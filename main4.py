import random

block = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15,
    16: 0

}

output_block = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9,
    10: 10,
    11: 11,
    12: 12,
    13: 13,
    14: 14,
    15: 15,
    16: 0

}

possible_blocks = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
move = None

def mix_blocks():
    random.shuffle(possible_blocks)
    for i in range(1,17):
        block[i] = possible_blocks[i - 1]


mix_blocks()


def beautiful_output():
    global output_block
    for i in range(1,17):
        if block[i] < 10:
            output_block[i] = str(block[i]) + "    "
        else:
            output_block[i] = str(block[i]) + "   "
    print(f"{output_block[1]},{output_block[2]},{output_block[3]},{output_block[4]}")
    print(f"{output_block[5]},{output_block[6]},{output_block[7]},{output_block[8]}")
    print(f"{output_block[9]},{output_block[10]},{output_block[11]},{output_block[12]}")
    print(f"{output_block[13]},{output_block[14]},{output_block[15]},{output_block[16]}")


def right():
    for i in range(1, 17):
        if block[i] == 0:
            if i not in [1,5,9,13]:
                block[i] = block[i-1]
                block[i-1] = 0
                break

def left():
    for i in range(1, 17):
        if block[i] == 0:
            if i not in [4,8,12,16]:
                block[i] = block[i+1]
                block[i+1] = 0
                break

def up():
    for i in range(1, 17):
        if block[i] == 0:
            if i not in [13,14,15,16]:
                block[i] = block[i+4]
                block[i+4] = 0
                break

def down():
    for i in range(1, 17):
        if block[i] == 0:
            if i not in [1,2,3,4]:
                block[i] = block[i-4]
                block[i-4] = 0
                break

def check():
    win = 0
    for i in range(1,16):
        if block[i] == i:
            win += 1
    if win == 15:
        print("You won!!!")
while True:
    if move in ["right","r"]:
        right()
    elif move in ["left","l"]:
        left()
    elif move in ["up","u"]:
        up()
    elif move in ["down","d"]:
        down()
    elif move in ["new game","ng"]:
        mix_blocks()

    beautiful_output()
    check()
    move = str(input("right(r)/left(l)/up(u)/down(d)/new game(ng)."))








