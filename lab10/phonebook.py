import psycopg2
import csv

# ========== Настройки подключения ==========
DB_NAME = "phonebook_db"
DB_USER = "postgres"
DB_PASSWORD = "Aididar110906$"
DB_HOST = "localhost"
DB_PORT = "5433"

def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# ========== PHONEBOOK ==========
def create_phonebook_table():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100),
                    phone VARCHAR(20)
                );
            """)
            conn.commit()

def insert_from_console():
    name = input("Name: ")
    phone = input("Phone: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s);", (name, phone))
            conn.commit()

def insert_from_csv(filename):
    with connect() as conn:
        with conn.cursor() as cur:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s);", (row['first_name'], row['phone']))
            conn.commit()

def update_phone(name, new_phone):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET phone = %s WHERE first_name = %s;", (new_phone, name))
            conn.commit()

def search_user(name=None, phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if name:
                cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s;", (f"%{name}%",))
            elif phone:
                cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s;", (f"%{phone}%",))
            else:
                cur.execute("SELECT * FROM phonebook;")
            rows = cur.fetchall()
            for row in rows:
                print(row)

def delete_user(name=None, phone=None):
    with connect() as conn:
        with conn.cursor() as cur:
            if name:
                cur.execute("DELETE FROM phonebook WHERE first_name = %s;", (name,))
            elif phone:
                cur.execute("DELETE FROM phonebook WHERE phone = %s;", (phone,))
            conn.commit()

# ========== SNAKE GAME DB ==========
def create_snake_tables():
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS user_score (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    level INTEGER,
                    score INTEGER,
                    state TEXT
                );
            """)
            conn.commit()

def login_user():
    username = input("Enter your username: ")
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
            user = cur.fetchone()
            if user:
                user_id = user[0]
                cur.execute("SELECT level FROM user_score WHERE user_id = %s ORDER BY id DESC LIMIT 1;", (user_id,))
                level = cur.fetchone()
                print(f"Welcome back, {username}! Your current level is {level[0] if level else 1}")
            else:
                cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
                user_id = cur.fetchone()[0]
                cur.execute("INSERT INTO user_score (user_id, level, score, state) VALUES (%s, %s, %s, %s);",
                            (user_id, 1, 0, 'new'))
                print(f"New user {username} created! Starting at level 1.")
            conn.commit()

def save_game(user_id, level, score, state):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO user_score (user_id, level, score, state) VALUES (%s, %s, %s, %s);",
                        (user_id, level, score, state))
            conn.commit()
            print("🎮 Game state saved!")

# ========== MAIN MENU ==========
def menu():
    create_phonebook_table()
    create_snake_tables()

    while True:
        print("\n📚 Lab 10 Menu:")
        print("1. Insert contact from console")
        print("2. Insert contacts from CSV")
        print("3. Update phone")
        print("4. Search contact")
        print("5. Delete contact")
        print("6. Snake Game - Login")
        print("7. Exit")

        try:
            choice = input("Select option: ")
        except KeyboardInterrupt:
            print("\n❗ Program interrupted by user. Exiting safely...")
            break

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            filename = input("CSV filename (e.g., contacts.csv): ")
            insert_from_csv(filename)
        elif choice == '3':
            name = input("Whose phone to update? ")
            new_phone = input("New phone: ")
            update_phone(name, new_phone)
        elif choice == '4':
            name = input("Search by name (or press enter): ")
            phone = input("Search by phone (or press enter): ")
            search_user(name=name if name else None, phone=phone if phone else None)
        elif choice == '5':
            name = input("Delete by name (or press enter): ")
            phone = input("Delete by phone (or press enter): ")
            delete_user(name=name if name else None, phone=phone if phone else None)
        elif choice == '6':
            login_user()
        elif choice == '7':
            print("👋 Exiting Lab 10...")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    menu()
