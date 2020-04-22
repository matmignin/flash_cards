#!/usr/bin/env python3
from click import Choice, command, option
import re


def PrintQuestion(str):
    post_number = "\. "
    new_string = re.sub(post_number, " ]\n", str, 1)
    part_of_string = new_string.split("\n")
    print("[", part_of_string[0])
    print(part_of_string[1], "\n")
    print("\t", part_of_string[2])
    if len(part_of_string) > 3:
        for i in range(3, len(part_of_string)):
            print("\t", part_of_string[i])
    print()


with open('patho.txt', 'r') as f:
    list_of_questions = f.read()
    question = (list_of_questions.split('\n\n'))


def start(x):
    print()
    number_of_questions = len(question) - 1
    print("_____________________________________________________________")
    print("_____________________________________________________________")
    print("\t\t ", question[0])
    print("\t\t\t[", number_of_questions, "]")
    print("_____________________________________________________________")
    print("_____________________________________________________________")

    review = []
    know = []

    while number_of_questions >= x:
        PrintQuestion(question[x])
        correct = input("correct?")
        if "y" in correct.lower():
            know.append(question[x])
            x += 1
        if "n" in correct.lower():
            review.append(question[x])
            x += 1
        elif "q" in correct.lower():
            break
        print()
    number_to_review = len(review)
    print("_____________________________________________________________")
    print("\n \t \t  Number of questions to review", number_to_review, "\n")
    print("_____________________________________________________________")
    y = 0
    while number_to_review > 0:
        # print (review[y], "\n"
        PrintQuestion(review[y])
        correct = input("correct?")
        if "y" in correct.lower():
            review.pop(y)
            number_to_review -= 1
            y -= 1
            continue
        if "n" in correct.lower():
            y += 1
        elif "q" in correct.lower():
            break
        if y > number_to_review - 1:
            y = 0
        else:
            continue

    print("good job! \n youre done")
    return


@command()
@option(
    "--n",
    help="The question we want to select",
    default=1,
    show_default=True,
    type=int
)
def cli(n):
    try:
        start(n)
    except KeyError:
        print("thats not a thing you can do")


if __name__ == "__main__":
    cli()
