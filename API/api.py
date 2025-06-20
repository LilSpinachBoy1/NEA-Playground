import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel

# Create bade model for searching by ID
class ID(BaseModel):
    id: int

# Set up db connection
con = sqlite3.connect('fun_facts.db', check_same_thread=False)
cur = con.cursor()

# function to run a query against the database
def run_query(query):
    try:
        cur.execute(query)
        con.commit()
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    

# Create FastAPI app
app = FastAPI()

# Endpoint to provide info on the API and database functionality
@app.get("/api/test")
def test():
    if run_query("SELECT * from facts;"): valid = True  # If the funtion returns something, the db is working
    else: valid = False
    return {"api": True, "db": valid}


# Endpoint to get a fact from a sent ID
@app.post("/api/search_id")
def search(id: ID):
    query = f"SELECT fact FROM facts WHERE id = {id.id};"
    result = run_query(query)
    if result: return {"fact": result[0][0]}
    else: return {"fact": "No fact found with that ID OR an issue with the database."}