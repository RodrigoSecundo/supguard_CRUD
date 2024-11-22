from app import app, db

# Garante que o código rode dentro do contexto da aplicação
with app.app_context():
    db.create_all()
    print("Database created!")