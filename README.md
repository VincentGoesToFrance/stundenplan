# Entwicklungsumgebung 
    python -m venv .venv
    wenn base: conda deactivate
    . .venv/bin/activate

# pip 
    (pip freeze > requirements.txt)
    pip install -r requirements.txt

# app starten
    entweder:
        flask --app app run --debug
    oder:
        python app.py

# datenbank einlesen
    terminal: mysql -u root -p < ./static/db/test_stundenplanDB.sql
    
    terminal: sqlite3 ./static/db/test_stundenplanDB.db
    terminal: .read ./static/db/test_stundenplanDB.sql

