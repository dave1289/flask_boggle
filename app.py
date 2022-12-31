from boggle import Boggle
from flask import Flask, render_template, session, redirect, request, jsonify

"""
Flask app for playing boggle with accompanying words.txt file
"""      

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lksdfh43'

# creating boggle object for game
boggle_game = Boggle()


@app.route('/')
def show_home():
   """shows homepage"""
   board = boggle_game.make_board()
   session['board'] = board
   highscore = session.get("highscore", 0)
   numplays = session.get("numplays", 0)
   return render_template('index.html', board=board, highscore=highscore, numplays=numplays)

@app.route('/handle-word', methods=['POST'])
def word_submit():
   """submits word for processing after guess"""
   word = request.args["word"]
   board = session["board"]
   response = boggle_game.check_valid_word(board, word)

   return jsonify({'result': response})