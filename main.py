#!/usr/bin/env python
from click import Choice, command, option
import re

def PrintQuestion(str):
    PostNum = "\. "
    newstr = re.sub(PostNum, " ]\n", str, 1)
    print("[",newstr, "\n")

with open('patho study guide.txt', 'r') as f:
    qList = f.read()
    Question = (qList.split('\n\n'))
print()
NumberOfQuestions = len(Question) - 1
print("There are", NumberOfQuestions, "questions for ", Question[0])
x = int(input("what question would you like to see? \n"))

Review = []
Know = []
RUNNING = True


while RUNNING:
   # print(Question[x], "\n")
    PrintQuestion(Question[x])
    Correct = input("correct?")
    if "y" in Correct.lower():
        Know.append(Question[x])
        x += 1
    if "n" in Correct.lower():
        Review.append(Question[x])
        x += 1
    elif "q" in Correct.lower():
        RUNNING = False
   # print("number of questions to review [", len(Review), "]")
    if x > NumberOfQuestions:
        RUNNING = False
    print()
    
NumberToReview = len(Review)    
print("_____________________________________________________________")
print("_____________________________________________________________")
print("\n \t \t  Number of Questions to Review", NumberToReview, "\n")
print("_____________________________________________________________")
print("_____________________________________________________________")
y = 0
while NumberToReview > 0:
    print (Review[y], "\n")
    Correct = input("correct?")
    if "y" in Correct.lower():
        Review.pop(y)
        NumberToReview -= 1
        y -= 1
        continue
    if "n" in Correct.lower():
        y += 1
    elif "q" in Correct.lower():
        break
    if y > NumberToReview - 1:
        y = 0
    else:
        continue 

print("good job! \n youre done")

"""
cards = {
    "default": "DEFAULT",
    "hypocampus": "brain",
    "heart": "chest",
    "eyeballs": "head",
    "feet": "legs",
}

available_cards = cards.keys()


@command()
@option(
    "--card",
    help="The card we want to select",
    default="default",
    # type=Choice(available_cards),
)
def cli(card):
    try:
        print(cards[card])
    except KeyError:
        print("thats not a thing")

if __name__ == "__main__":
    cli()

"""




