import random

guesses=""
turns = 10

infile = open("d:\\words.txt","r")
lines = infile.readlines()
word = random.choice(lines)
word = word.rstrip()

while turns >0:
    failed = 0
    for char in word:   #word 문자열에서 글자를 1개씩 가져온다.
        if char in guesses:
            print(char,end="")
        else:
            print("_",end="")
            failed +=1
    if failed == 0:
        print("사용자 승리")
        break
    print("")
    guess = input("단어를 추측하시오:")
    guesses += guess
    if guess not in word:
        turns -=1
        print("틀렸음!")
        print(str(turns)+"기회가 남았슴!")
        if turns ==0:
            print("사용자가 패배 정답은"+word)

infile.close()
        
