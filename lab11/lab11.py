import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5433",
    database="phonebook_db",
    user="postgres",
    password="Aididar110906$"
)
cur = conn.cursor()

def search_pattern(pattern):
    try:
        cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
        results = cur.fetchall()
        for name, phone in results:
            print(f"{name} -> {phone}")
    except Exception as e:
        print("Error:", e)

def insert_or_update(name, phone):
    try:
        cur.execute("CALL insert_or_update_user(%s, %s);", (name, phone))
        conn.commit()
        print(f"Inserted/Updated user: {name}")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

def insert_many(names_list, phones_list):
    try:
        del conn.notices[:]
        cur.execute("CALL insert_many_users(%s, %s);", (names_list, phones_list))
        conn.commit()
        if conn.notices:
            print("Notice:", conn.notices[-1].strip())
    except Exception as e:
        conn.rollback()
        print("Error:", e)

def paginate(limit, offset):
    try:
        cur.execute("SELECT * FROM paginate_phonebook(%s, %s);", (limit, offset))
        results = cur.fetchall()
        for name, phone in results:
            print(f"{name} -> {phone}")
    except Exception as e:
        print("Error:", e)

def delete_user(name=None, phone=None):
    try:
        cur.execute("CALL delete_user(%s, %s);", (name, phone))
        conn.commit()
        if conn.notices:
            print("Notice:", conn.notices[-1].strip())
    except Exception as e:
        conn.rollback()
        print("Error:", e)

if __name__ == "__main__":
    search_pattern("Ali")
    insert_or_update("Aididar", "87011234567")
    insert_many(["Bob", "Carol", "Dave"], ["1234567890", "12345", "9876543210"])
    paginate(2, 0)
    delete_user(name="Bob")

cur.close()
conn.close()