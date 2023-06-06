from flask import Flask, render_template
from app import business_logic
from app.word_list import WordList

app = Flask('Latin Wordle')
words = WordList()
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/colorize_guess/<string:target_word>/<string:guess>')
def colorize_guess(target_word, guess):
    return business_logic.colorize_guess(target_word, guess)

@app.route('/validate_word/<string:word>')
def validate_word(word: str) -> str:
    return str(word in words)
