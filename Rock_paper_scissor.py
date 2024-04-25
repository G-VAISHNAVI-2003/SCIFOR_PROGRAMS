import random
def user_input():
    ch = str(input("Select one from : 'rock','paper',scissor' :"))
    if ch == 'rock':
        return 'rock'
    elif ch == 'paper':
        return 'paper'
    elif ch == 'scissor':
        return 'scissor'
    else:
        print("Not valid input!..")
def opponent():
    x = random.choice(['rock','paper','scissor'])
    return x
def result(a,b):
    if a == b:
        return 'Tie breaker'
    elif(a == 'rock' and b == 'scissor') or (a == 'paper' and b == 'rock') or (a == 'scissor' and b == 'paper'):
        return "user wins"
    else:
        return "opponent wins"
def run():
    user_inp = user_input()
    opponent_inp = opponent()
    print("user entered",user_inp)
    print("opponent input",opponent_inp)
    print(result(user_inp,opponent_inp))
run()