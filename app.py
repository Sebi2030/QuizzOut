from flask import Flask, render_template, request, redirect, url_for, session, g, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.urls import url_parse
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, RadioField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from sqlalchemy import desc
from datetime import datetime
from sqlalchemy import or_
import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheimeschlüssel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'benutzer.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    benutzername = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    passwort_hash = db.Column(db.String(128))
    marks = db.Column(db.Integer, index=True)

    def __repr__(self):
        return '<User {}>'.format(self.benutzername)

    def set_password(self, passwort):  
        self.passwort_hash = generate_password_hash(passwort)
    
    def check_password(self, passwort):  
        return check_password_hash(self.passwort_hash, passwort)

class QuizQuestion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500), nullable=False)
    option1 = db.Column(db.String(200), nullable=False)
    option2 = db.Column(db.String(200), nullable=False)
    option3 = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)
    explanation = db.Column(db.String(500), nullable=True) 
    difficulty = db.Column(db.String(50), nullable=False)

    def serialize(self):
        return {
            'question': self.question,
            'option1': self.option1,
            'option2': self.option2,
            'option3': self.option3,
            'answer': self.answer,
            'explanation': self.explanation
        }

class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    quiz_date = db.Column(db.DateTime, default=datetime.utcnow)

@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        g.user = user



class QuestionForm(FlaskForm):
    options = RadioField('Options: ', validators=[DataRequired()], choices=[('option1', ''), ('option2', ''), ('option3', '')])
    submit = SubmitField('Next')


class RegistrationForm(FlaskForm):
    benutzername = StringField('Benutzername', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    passwort2 = PasswordField('Passwort bestätigen', validators=[DataRequired(), EqualTo('passwort')])
    submit = SubmitField('Register')

    def validate_benutzername(self, benutzername):
        user = User.query.filter_by(benutzername=benutzername.data).first()
        if user is not None:
            raise ValidationError('Benutzername existiert bereits.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('E-Mail existiert bereits.')

class LoginForm(FlaskForm):
    benutzername = StringField('Benutzername', validators=[DataRequired()])
    passwort = PasswordField('Passwort', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(benutzername=form.benutzername.data).first()
        if user and user.check_password(form.passwort.data):
            session['user_id'] = user.id
            return redirect(url_for('home'))
        else:
            flash('Ungültiger Benutzername oder Passwort')
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    print("=== Register-Funktion wird aufgerufen ===")

    if form.validate_on_submit():
        print("Formular wurde erfolgreich validiert.")

        user = User(benutzername=form.benutzername.data, email=form.email.data)
        user.set_password(form.passwort.data)

        try:
            db.session.add(user)
            db.session.commit()
            print("User wurde erfolgreich zur Datenbank hinzugefügt.")
        except Exception as e:
            print(f"Fehler beim Hinzufügen des Benutzers zur Datenbank: {e}")

        session['user_id'] = user.id

        return redirect(url_for('home'))

    else:
        print("Formularvalidierung fehlgeschlagen.")
        for field, errors in form.errors.items():
            for error in errors:
                print(f"Fehler im Feld '{getattr(form, field).label.text}': {error}")

    return render_template('register.html', title='Register', form=form)



@app.route('/select_difficulty', methods=['GET', 'POST'])
def select_difficulty():
    if request.method == 'POST':
        difficulty = request.form['difficulty']
        session['selected_difficulty'] = difficulty
        return redirect(url_for('quiz', difficulty=difficulty))

    return render_template('select_difficulty.html')

def get_questions(difficulty):
    questions = QuizQuestion.query.filter_by(difficulty=difficulty).all()
    return questions

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html', title='Quiz')


@app.route('/quiz-questions')
def quiz_questions():
    print("=== Quiz Route aufgerufen ===")  # Hinzugefügte Lokalausgabe
    difficulty = session.get('selected_difficulty')
    print(f"Selected Difficulty: {difficulty}")  # Hinzugefügte Lokalausgabe

    # Check if the difficulty is not selected, redirect to select difficulty
    if not difficulty:
        flash('Bitte wählen Sie zuerst die Schwierigkeitsstufe aus.')
        return redirect(url_for('select_difficulty'))

    # Get the questions for the selected difficulty
    questions = get_questions(difficulty)
    formatted_questions = []
    for idx, question in enumerate(questions, start=1):
        formatted_question = {
            'numb': idx,
            'question': question.question,
            'answer': question.answer,
            'options': [
                question.option1,
                question.option2,
                question.option3,
            ],
            'explanation':question.explanation
        }
        formatted_questions.append(formatted_question)
    print(formatted_questions)
    print(f"Number of Questions: {len(formatted_questions)}")
    return jsonify(formatted_questions)

@app.route('/update_marks', methods=['POST'])
def update_marks():
    data = request.json
    
    if 'score' not in data:
        return jsonify({'error': 'score not provided'}), 400
    score = data.get('score')
    
    # Get the user from the database
    user_id = session.get('user_id',None)
    user = User.query.get(user_id)
    print(user)
    # Check if the user exists
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    previous_marks = None
    
    if user.marks == None:
        previous_marks = 0
    else:
        previous_marks = user.marks
    # Update user marks
    user.marks = previous_marks + score

    # Commit the changes to the database
    db.session.commit()

    return jsonify({'message': 'User marks updated successfully'})


# @app.route('/quiz/result')
# def quiz_result():
#     user_score = UserScore.query.filter_by(user_id=g.user.id).first()
#     return render_template('quiz_result.html', score=user_score.score if user_score else 0)


@app.route('/quiz/high-score')
def quiz_high_score_result():
    # Query users with non-null marks in descending order
    users_with_marks = User.query.filter(User.marks.isnot(None)).order_by(desc(User.marks)).all()
    return render_template('high-score-results.html', users_with_marks=users_with_marks)


@app.route('/resetQuiz', methods=['GET'])
def reset_quiz():
    session.pop('selected_difficulty', None)
    return redirect(url_for('home'))


@app.route('/profile')
def profile():
    if not g.user:
        flash("Sie müssen angemeldet sein, um auf Ihr Profil zuzugreifen.")
        return redirect(url_for('login'))
    return render_template('profile.html', title='Profil', user=g.user)

@app.route('/logout')
def logout():
    if not g.user:
        return redirect(url_for('login'))
    session.pop('user_id', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, host='127.0.0.1', port=5000)
