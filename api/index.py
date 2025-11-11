# Importiert das Flask-Framework und die Funktion für Request-Parameter
from flask import Flask, request

# Erstellt die Flask-Anwendungsinstanz
app = Flask(__name__)

# Definiert die Route für den API-Endpunkt (/api)
# Der Endpunkt ist jetzt /api/prognose und akzeptiert einen optionalen Parameter
@app.route('/api/prognose')
def erstelle_prognose():
    """
    Diese Funktion liest einen Input-Wert und berechnet eine einfache lineare Prognose.
    
    Verwendung: /api/prognose?input_wert=100
    """
    try:
        # 1. Parameter aus der URL lesen (z.B. ?input_wert=50)
        input_str = request.args.get('input_wert', '0')
        input_wert = float(input_str)
        
        # 2. Einfache Prognose-Logik (Beispiel: y = 2x + 10)
        prognose_wert = (input_wert * 2) + 10
        
        # 3. Ergebnis als strukturiertes JSON zurückgeben
        return {
            "status": "success",
            "input_wert": input_wert,
            "prognose_formel": "y = 2x + 10",
            "prognose_wert": prognose_wert,
            "hinweis": "Um eine Prognose zu erhalten, verwenden Sie den Parameter: ?input_wert=IHR_WERT"
        }
    
    except ValueError:
        # Fehlerbehandlung, falls der Input keine gültige Zahl ist
        return {
            "status": "error",
            "message": "Ungültiger Wert für 'input_wert'. Bitte geben Sie eine Zahl ein.",
            "beispiel": "/api/prognose?input_wert=45.5"
        }, 400
    except Exception as e:
        # Allgemeine Fehlerbehandlung
        return {
            "status": "error",
            "message": f"Ein unerwarteter Fehler ist aufgetreten: {str(e)}"
        }, 500

# Alte /api Route wird entfernt, da /api/prognose der neue Hauptendpunkt ist.
# Sie können dies auch auf /api umbenennen, aber /api/prognose ist klarer.
