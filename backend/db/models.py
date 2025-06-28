# backend/db/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Index, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import String

Base = declarative_base()

class Song(Base):
    __tablename__ = 'songs'

    id = Column(String(75), primary_key=True)
    title = Column(String(255))
    artist = Column(String(255))
    album = Column(String(255))
    youtube_video_id = Column(String(50))
    spotify_url = Column(String(500))
    duration = Column(Integer)
    created_at = Column(String)

    fingerprints = relationship("Fingerprint", back_populates="song")


class Fingerprint(Base):
    __tablename__ = 'fingerprints'

    id = Column(Integer, primary_key=True)
    hash = Column(Integer, index=True)
    timestamp = Column(Float)
    song_id = Column(Integer, ForeignKey('songs.id'))

    song = relationship("Song", back_populates="fingerprints")