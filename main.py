#!/usr/bin/env python
from click import Choice, command, option


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
    # http://click.pocoo.org/6/options/#choice-options
    type=Choice(available_cards),
)
def cli(card):
    print("Hi Mat!")
    print(cards[card])


if __name__ == "__main__":
    cli()
