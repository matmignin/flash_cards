#!/usr/bin/env python
from click import Choice, command, option




with open('patho study guide.txt', 'r') as f:
    qList = f.read()
    Question = (qList.split('\n\n'))

print("There are",len(Question) - 1, "questions.")
x = int(input("what question would you like to see?"))

print(Question[x])




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




