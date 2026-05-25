from pathlib import Path
import random
import qdata
import sys

global val
global score
num = list(range(0, 10))
file = Path("score.txt")

def main():
    while True:
        ask_user = input("Wanna play the fun python quiz?(yes/no) ").strip().lower()
        if ask_user == "yes" or ask_user == "no":
            break
    if ask_user == "yes":
        while True:
            score = 0
            random.shuffle(num)
            for n in num:
                val = n
                marked_options = dict(zip(qdata.markers, qdata.options[val]))
                display_question(val)
                display_option(marked_options)
                score = user_choice(val, score, marked_options)
            high_score(score)
            while True:
                usr = input("Wanna play again(yes/no)? ").strip().lower()
                if usr == "yes" or usr == "no":
                    break
            if usr == "no":
                sys.exit()
    else:
        sys.exit()



def display_question(val):
    print(qdata.questions[val])

def display_option(marked_options):
    for marker,option in marked_options.items():
        print(f"{marker}. {option}")

def user_choice(val, score, marked_options):
    while True:
        try:
            user_ans = input("Choose your option: ").strip().upper()
            if marked_options[user_ans] == qdata.qna[qdata.questions[val]]:
                score += 4
                print("You got it right!")
            else:
                score -= 1
                print("You are wrong:(")
            print(f"Current Score: {score}")
            return score
        except KeyError:
            print("Choose A/ B/ C/ D!!")

def high_score(score):
    h_score = 0
    if h_score < score:
        h_score = score
        file.write_text(f"High score: {h_score}")
        print(file.read_text())
    else:
        file.write_text(f"High scores: {h_score}")

main()



