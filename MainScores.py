from flask import Flask, render_template
from Score import read_score
from Utils import BAD_RETURN_CODE

app = Flask(__name__)


@app.route('/')
def score_server():
    template = "<!DOCTYPE html> " \
               "<html lang='en'> " \
               "<head> " \
               "<title>Scores Game</title> " \
               "</head> " \
               "<body> " \
               f"<h1>The score is <div id='score'>{read_score()}</div></h1> " \
               "</body> " \
               "</html> "

    err_template = "<!DOCTYPE html> " \
                   "<html lang='en'> " \
                   "<head> " \
                   "<title>Scores Game</title> " \
                   "</head> " \
                   "<body> " \
                   f"<h1>The score is <div id='score'>{BAD_RETURN_CODE}</div></h1> " \
                   "</body> " \
                   "</html> "
    try:
        return render_template(template)
    except FileNotFoundError:
        return render_template(err_template)


