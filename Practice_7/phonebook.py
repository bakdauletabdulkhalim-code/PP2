import csv
from connect import get_connection

def insert_from_csv():
    conn = get_connection()
    cur = conn.cursor()

    with open("Practice_7/contacts.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row[0], row[1])
            )

    conn.commit()
    print("Data loaded from CSV!")

    cur.close()
    conn.close()


def insert_manual():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Name: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    print("Added!")

    cur.close()
    conn.close()


def show_all():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def update_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Enter name to update: ")
    new_phone = input("New phone: ")

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE name=%s",
        (new_phone, name)
    )

    conn.commit()
    print("Updated!")

    cur.close()
    conn.close()


def delete_contact():
    conn = get_connection()
    cur = conn.cursor()

    name = input("Enter name to delete: ")

    cur.execute(
        "DELETE FROM phonebook WHERE name=%s",
        (name,)
    )

    conn.commit()
    print("Deleted!")

    cur.close()
    conn.close()


def search():
    conn = get_connection()
    cur = conn.cursor()

    keyword = input("Search name: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE name ILIKE %s",
        (f"%{keyword}%",)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


while True:
    print("\n--- PHONEBOOK ---")
    print("1. Load from CSV")
    print("2. Add contact")
    print("3. Show all")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Search")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_from_csv()
    elif choice == "2":
        insert_manual()
    elif choice == "3":
        show_all()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        search()
    elif choice == "0":
        break
    else:
        print("Invalid choice!")