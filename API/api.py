import sqlite3

# Set up db connection
con = sqlite3.connect('fun_facts.db')
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
    