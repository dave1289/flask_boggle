from boggle import Boggle
from flask import Flask, render_template, session, redirect, request, jsonify

"""
Flask app for playing boggle with accompanying words.txt file
"""      

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lksdfh43'

# creating boggle object for game
boggle_game = Boggle()
score = 0

@app.route('/')
def show_home():
   """shows homepage"""
   board = boggle_game.make_board()
   session['board'] = board
   highscore = session.get("highscore", 0)
   numplays = session.get("numplays", 0)
   return render_template('index.html', board=board, highscore=highscore, numplays=numplays, score=score)

@app.route('/handle-word', methods=['POST'])
def word_submit():
   global score
   """submits word for processing after guess"""
   word = request.form["word"]
   board = session["board"]
   highscore = session.get("highscore", 0)
   numplays = session.get("numplays", 0)
   return render_template('index.html', board=board, highscore=highscore, numplays=numplays, score=score)
