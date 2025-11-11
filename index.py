# Importiert das Flask-Framework und die Funktion für Request-Parameter
from flask import Flask, request

# Erstellt die Flask-Anwendungsinstanz
app = Flask(__name__)

# NEU: Standard-API-Route als Health Check und Anleitung
@app.route('/api')
def api_root():
    """
    Diese Funktion dient als Health Check und gibt eine Anleitung für die Nutzung
    des /api/prognose Endpunkts.
    """
    return {
        "status": "ok",
        "message": "API Root erfolgreich erreicht. Verwenden Sie den Endpunkt /api/prognose für eine Berechnung.",
        "anleitung": "Hängen Sie ?input_wert=IHR_WERT an die URL an.",
        "beispiel": "/api/prognose?input_wert=150"
    }

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
        # Der Default-Wert '0' stellt sicher, dass es immer eine Zahl gibt, 
        # wenn der Parameter fehlt.
        input_str = request.args.get('input_wert', '0')
        
        # Sicherstellen, dass die Konvertierung fehlschlägt, falls es kein reiner String ist
        if not isinstance(input_str, str):
            raise ValueError("Input ist kein String.")
            
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
        # Wichtig: Im Produktivsystem sollte der detaillierte Fehler nicht angezeigt werden
        return {
            "status": "error",
            "message": "Ein interner Serverfehler ist aufgetreten.",
            "details": f"Fehler: {type(e).__name__}: {str(e)}"
        }, 500

# Alte /api Route wird entfernt, da /api/prognose der neue Hauptendpunkt ist.
# Sie können dies auch auf /api umbenennen, aber /api/prognose ist klarer.
