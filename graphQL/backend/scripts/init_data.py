import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath ( __file__ ) ) ) )

from app . database . database import engine , SessionLocal
from app . database . models import User

def init_database():
    User.metadata.create_all(bind=engine)

    db = SessionLocal()

    if db.query(User).count() == 0:
        users = [
            User(name="John Doe", email="john.doe@example.com"),
            User(name="Jane Smith", email="jane.smith@example.com"),
            User(name="Bob Johnson", email="bob.johnson@example.com"),
        ]

        db.add_all(users)
        db.commit()
        print("Données initiales chargées avec succès")
    else:
        print("La base de données contient déjà des données")

    db.close()

if __name__ == "__main__":
    init_database()