from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///valentine_responses.db'  # Ustawienie URL bazy danych
db = SQLAlchemy(app)

class ValentineResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    response = db.Column(db.String(3), nullable=False)

# Strona główna z formularzem HTML
@app.route('/')
def index():
    return render_template('Zapytanie.html')

# Obsługa zapisywania odpowiedzi w bazie danych
@app.route('/save_response', methods=['POST'])
def save_response():
    response = request.form.get('response')

    if response == 'yes':
        new_response = ValentineResponse(response='Tak')
        db.session.add(new_response)
        db.session.commit()

        return jsonify({'message': 'Odpowiedź "Tak" została zapisana w bazie danych.'})
    else:
        return jsonify({'message': 'Odpowiedź "Nie". Trzymaj się!'})

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
