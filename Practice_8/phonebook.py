from connect import get_connection

def call_upsert():
    name = input("Name: ")
    phone = input("Phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL upsert_contact(%s, %s);", (name, phone))

    conn.commit()
    cur.close()
    conn.close()

    print("Saved!")


def call_search():
    keyword = input("Search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s);", (keyword,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def call_delete():
    val = input("Name or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_contact(%s);", (val,))
    conn.commit()

    cur.close()
    conn.close()

    print("Deleted!")


def call_pagination():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def call_many():
    names = ["Ali", "Dana", "ErrorUser"]
    phones = ["8777", "8701", "abc"]  

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_many(%s, %s);", (names, phones))
    conn.commit()

    cur.close()
    conn.close()

    print("Batch done!")


while True:
    print("\n--- MENU ---")
    print("1. Upsert")
    print("2. Search")
    print("3. Delete")
    print("4. Pagination")
    print("5. Insert many")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "1":
        call_upsert()
    elif choice == "2":
        call_search()
    elif choice == "3":
        call_delete()
    elif choice == "4":
        call_pagination()
    elif choice == "5":
        call_many()
    elif choice == "0":
        break