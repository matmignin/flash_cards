#!/usr/bin/env python
from click import Choice, command, option




with open('patho study guide.txt', 'r') as f:
    qList = f.read()
    Question = (qList.split('\n\n'))
print()
print("There are",len(Question) - 1, "questions for ", Question[0])
x = int(input("what question would you like to see?"))
print()

Review = []
Know = []
RUNNING = True

while RUNNING:
    print(Question[x])
    Correct = input("correct?")
    if "y" in Correct.lower():
        Know.append(Question[x])
    if "n" in Correct.lower():
        Review.append(Question[x])
    elif "q" in Correct.lower():
        RUNNING = False
    print(len(Review))
    print()
    x += 1


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




