from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.orm import relationship
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'geheimeschlüssel'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///benutzer.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'anmelden'

@login_manager.user_loader
def load_user(user_id):
    return Benutzer.query.get(int(user_id))

class Benutzer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    benutzername = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwort = db.Column(db.String(60), nullable=False)

class Frage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    antworten = db.relationship('Antwort', backref='frage', lazy=True)

class Antwort(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    ist_richtig = db.Column(db.Boolean, default=False)
    frage_id = db.Column(db.Integer, db.ForeignKey('frage.id'), nullable=False)

def erstelle_quiz():
    fragen = Frage.query.all()
    zufällige_fragen = random.sample(fragen, 5)
    return zufällige_fragen

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrieren', methods=['GET', 'POST'])
def registrieren():
    if request.method == 'POST':
        benutzername = request.form.get('benutzername')
        email = request.form.get('email')
        passwort = request.form.get('passwort')

        vorhandener_benutzer = Benutzer.query.filter_by(email=email).first()
        if vorhandener_benutzer:
            flash('Diese E-Mail ist bereits registriert. Bitte melden Sie sich an oder verwenden Sie eine andere E-Mail.', 'error')
        else:
            passwort_hash = bcrypt.generate_password_hash(passwort).decode('utf-8')
            neuer_benutzer = Benutzer(benutzername=benutzername, email=email, passwort=passwort_hash)
            db.session.add(neuer_benutzer)
            db.session.commit()
            flash('Ihr Konto wurde erstellt. Sie können sich jetzt anmelden.', 'success')

            # Füge hier die Zeile für die Umleitung hinzu
            return redirect(url_for('index'))

    return render_template('registrieren.html')





    print("Nicht im POST")
    return render_template('registrieren.html')



@app.route('/anmelden', methods=['GET', 'POST'])
def anmelden():
    if request.method == 'POST':
        email = request.form.get('email')
        passwort = request.form.get('passwort')

        benutzer = Benutzer.query.filter_by(email=email).first()
        if benutzer:
            if bcrypt.check_password_hash(benutzer.passwort, passwort):
                login_user(benutzer)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('profil'))

        flash('Anmeldung fehlgeschlagen. Bitte überprüfen Sie Ihre Eingaben.', 'error')

    return render_template('anmelden.html')
# ...

@app.route('/profil')
@login_required
def profil():
    return render_template('profil.html', benutzer=current_user)

@app.route('/abmelden')
@login_required
def abmelden():
    logout_user()
    return redirect(url_for('index'))

@app.route('/quiz')
@login_required
def quiz():
    fragen = erstelle_quiz()
    return render_template('quiz.html', fragen=fragen)

@app.route('/quiz/antworten', methods=['POST'])
@login_required
def antworten():
    benutzer_antworten = request.form.to_dict()
    score = 0

    for frage_id, antwort_id in benutzer_antworten.items():
        antwort = Antwort.query.get(int(antwort_id))
        if antwort and antwort.ist_richtig:
            score += 1

    flash(f'Ihr Score: {score}', 'info')
    return redirect(url_for('quiz'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
<<<<<<< HEAD
    app.run(debug=True, host='0.0.0.0', port=5000)

=======
    app.run(debug=True, host='127.0.0.1', port=5000)
>>>>>>> 441617b9d0998ddd3c15b1ccc3762a9ee7631e8d
