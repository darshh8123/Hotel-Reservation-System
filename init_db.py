from models import db, Room
from app import app  # This ensures the app context is available for SQLAlchemy

with app.app_context():
    db.create_all()

    # Add sample rooms
    sample_rooms = [
        Room(room_type='AC', price_per_night=2000.0, availability=True),
        Room(room_type='Non AC', price_per_night=1500.0, availability=True),
        Room(room_type='AC', price_per_night=2200.0, availability=False),
    ]

    db.session.bulk_save_objects(sample_rooms)
    db.session.commit()
    print("Database initialized with sample data.")
