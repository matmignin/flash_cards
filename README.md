# flash_cards
A web based flash card game that converts a list of questions in any .txt file into individual prompts

## Getting Started
### install requirementet into virtual envv
 - `python3 -m venv quiz_cards`
 - `source quiz_cards/bin/activate`
 - `pip install -r requirements.txt`

### start the flask server
 - `./webapp.py`

 * `FLASK_APP=webapp.py flask run` to manually start flask

### create a login
 - go to [http://127.0.0.1:5000/signup] to sign up
 - go to [http://127.0.0.1:5000/login] to login



## convert a txt file
 - use `./convert.py` to convert a txt file


### CLI

0. `workon flash_cards`
1. Run `./main.py`
2. TBD
3. read a text file full of question and answers
4. convert to flash cards based on format of question
5. display flashcards in order and single out the ones that were wrong
6. review the incorrect question
