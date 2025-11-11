# Importiert das Flask-Framework
from flask import Flask

# Erstellt die Flask-Anwendungsinstanz
app = Flask(__name__)

# Definiert die Route für den API-Endpunkt (/api)
@app.route('/api')
def hello_world():
    """
    Diese Funktion gibt eine einfache "Willkommen"-Nachricht als JSON zurück.
    """
    # Flask konvertiert Python-Dictionaries automatisch in JSON
    return {
        "message": "Willkommen bei Ihrer Python-Web-App auf Vercel!",
        "language": "Deutsch",
        "framework": "Flask"
    }
