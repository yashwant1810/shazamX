# from shazamX directory run these commands

# run this first 
source backend/venv/bin/activate

# run this to start the API on: http://127.0.0.1:8000
uvicorn backend.main:app --reload
