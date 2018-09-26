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





'''
Planes of section 	Frontal, Transverse, Sagittal
Anatomical Position 	The body is in a standing position, trunk is erect, head, eyes facing forward, arms by side wih palm forward, legs are straight with toes also pointing forward.
Anterior (ventral) 	Front of the body or structure.
Posterior (dorsal) 	Back of the body or structure.
Superior 	A structure that lies above another.
Inferior 	A structure that lies below another.
Medial 	A structure closer to the midline of the body or movement toward the midline.
Lateral 	A structure further away from the midline of the body or movement away from the midline of the body.
Proximal 	The end of a structure of the extremities located closest to the trunk.
Distal 	The end of a structure of the extremities located farthest from the trunk.
Superficial 	External; located close to or on the body surface.
Deep 	Internal; located further beneath the body surface than the superficial structure.
Cervical 	Regional term referring to the neck.
Thoracic 	Regional term referring to the portion of the body between the neck and the abdomen; also known as chest (thorax).
Lumbar 	Regional term referring to the portion of the back between the abdomen and the pelvis.
Plantar 	Bottom of the foot.
Dorsal 	Top of the foot.
Palmar 	The anterior or ventral surface of the hands.
Supine 	Facing upward (lying on back).
Prone 	Facing downward (lying on abdomen)
HOMEOSTASIS 	GOOD HEALTH
ventral cavity 	consists of two compartments thoracic cavity and the abdominal cavity
thoracic cavity 	heart and lungs
dorsal cavity 	the central nervous system and consist of the cranial cavity or spinal cavity
abdominal cavity 	liver stomach intestines
sectioned 	way to make particular sutures easily visible
plane 	imaginary flat surface that seperates two portions of the body
frontal section 	a plane from side to side that seperates the body into front to back
sagittal section 	a plane from front to back that seperates the body into right and left portions
transverse section 	a horizontal plane seperates the body into upper and lower portions
'''
