import sqlite3

db_path = "progs.db"

def connect_to_db(path):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

def read_programs_by_program_type(program_type):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM programs WHERE program_type = ?'
    value = program_type
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_program_by_program_id(program_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM programs WHERE id = ?'
    value = program_id
    results = cur.execute(query,(value,)).fetchone()
    conn.close()
    return results

def insert_program(program_data):
    conn, cur = connect_to_db(db_path)
    query = 'INSERT INTO programs (program_type, program_name, salary, duration, description, url) VALUES (?,?,?,?,?,?)'
    values = (program_data['program_type'], program_data['program_name'],
              program_data['salary'], program_data['duration'],
              program_data['description'], program_data['url'])
    cur.execute(query,values)
    conn.commit()
    conn.close()

def update_program(program_data):
    conn, cur = connect_to_db(db_path)
    query = "UPDATE programs SET program_type=?, program_name=?, salary=?, duration=?, description=?, url=? WHERE id=?"
    values = (program_data['program_type'], program_data['program_name'],
              program_data['salary'], program_data['duration'],
              program_data['description'], program_data['url'],
              program_data['program_id'])
    cur.execute(query, values)
    conn.commit()
    conn.close()
    
def delete_program(program_id):
    conn, cur = connect_to_db(db_path)
    query = "DELETE FROM programs WHERE id=?"
    values = (program_id,)
    cur.execute(query, values)
    conn.commit()
    conn.close()