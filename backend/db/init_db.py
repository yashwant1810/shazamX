# backend/db/init_db.py

from sqlalchemy import create_engine
from backend.db.models import Base

def init_db(db_path="sqlite:///shazam.db"):
    engine = create_engine(db_path)
    Base.metadata.create_all(engine)
    print("✅ Database initialized!")

if __name__ == "__main__":
    init_db()