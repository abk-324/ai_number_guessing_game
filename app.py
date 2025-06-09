import os
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Change this to a secure random key

# Configure server-side session
SESSION_FILE_DIR = os.path.join(os.getcwd(), 'flask_session')
os.makedirs(SESSION_FILE_DIR, exist_ok=True)

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_FILE_DIR'] = SESSION_FILE_DIR
app.config['SESSION_PERMANENT'] = False

Session(app)

@app.route('/')
def index():
    # Initialize game state in session
    session['low'] = 1
    session['high'] = 100
    session['guess'] = 50
    session['attempts'] = 0
    session['game_over'] = False
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    if session.get('game_over', False):
        return jsonify({'status': 'game_over', 'message': 'Game is over. Refresh to play again.'})

    feedback = request.json.get('feedback')
    low = session.get('low', 1)
    high = session.get('high', 100)
    guess = session.get('guess', 50)
    attempts = session.get('attempts', 0) + 1

    if feedback == 'correct':
        session['game_over'] = True
        session['attempts'] = attempts
        return jsonify({'status': 'correct', 'guess': guess, 'attempts': attempts})

    if feedback == 'low':
        low = guess + 1
    elif feedback == 'high':
        high = guess - 1
    else:
        return jsonify({'status': 'error', 'message': 'Invalid feedback'})

    if low > high:
        session['game_over'] = True
        return jsonify({'status': 'error', 'message': 'Inconsistent feedback, no numbers left.'})

    guess = (low + high) // 2

    session['low'] = low
    session['high'] = high
    session['guess'] = guess
    session['attempts'] = attempts

    return jsonify({'status': 'continue', 'guess': guess, 'attempts': attempts})

if __name__ == '__main__':
    app.run(debug=True)
