def game():
    return 0

score = game()
with open("hiscore.txt") as f:
    hiScoreStr = f.read()
    
if hiScoreStr=='0':
    with open("hiscore.txt", "w") as f:
        f.write(str(score))

elif int(hiScoreStr)<score :
    with open("hiscore.txt", "w") as f:
        f.write(str(score))