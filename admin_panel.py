import main_1
import models_admin
import os
import sqlite3
from prettytable import PrettyTable

def id_have(path, id):
    all_id = []
    with sqlite3.connect(f"DB/database.db") as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM {path} ")
        for i in cursor:
            all_id.append(object.__str__(*i))
    m = id in all_id
    if m == True:
        return True
    else:
        return False

def exit_panel():
    cmd = input("0. Back\n\t>>>| ")
    while True:
        if cmd == '0':
            return main_file()
        else:
            print("Warning! (You can enter -> 0")
            cmd = input("0. Back\n\t>>>| ")

def add_user():
    name = input("Name: ")
    username = input("Username: ")
    admins = input("Admin: ")
    password = int(input("Password: "))
    save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)
    while True:
        if save == '1':
            user = models_admin.User(name, username, admins, password)
            user.add()
            print("The user insertion process was successful")
            return main_file()
        elif save == '2':
            print("The operation was canceled")
            return main_file()
        else:
            print("Warning! (You can enter -> 1 or 2")
            save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)

def update_user():
    id = input("Enter the user ID you want to update: ")
    while True:
        if id.isdigit():
            break
        else:
            os.system("color 4")
            print("Warning! ID should be equal to type integer.")
            print(" _ _ " * 10)
            id = input("Enter the user ID you want to update: ")
    os.system("color 2")
    while True:
        if id_have("users", id) == True:
            break
        else:
            os.system("color 4")
            print("Error! There is no user with such an id")
            print(" _ _ " * 10)
            id = input("Enter the user ID you want to update: ")
    name = input("Name: ")
    username = input("Username: ")
    admins = input("Admin: ")
    password = int(input("Password: "))
    save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)
    while True:
        if save == '1':
            user = models_admin.User(name, username, admins, password)
            user.update(id)
            print("The user insertion process was successful")
            return main_file()
        elif save == '2':
            print("The operation was canceled")
            return main_file()
        else:
            print("Warning! (You can enter -> 1 or 2")
            save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)

def delete_user():
    id = input("Enter the user ID you want to delete: ")
    while True:
        if id_have("users", id) == True:
            break
        else:
            os.system("color 4")
            print("Error! There is no user with such an id")
            print(" _ _ " * 10)
            id = input("Enter the user ID you want to delete: ")

    os.system("color 2")
    s = """Data storage:\n 1. Yes\t2. No\n\t>>>|"""
    save = input(s)
    while True:
        if save == '1':
            with sqlite3.connect("DB/database.db") as db:
                cursor = db.cursor()
                cursor.execute(f"""DELETE FROM users WHERE id = {id}""")
            db.commit()
            print("The user insertion process was successful")
            return main_file()
        elif save == "2":
            print("The operation was canceled")
            return main_file()
        else:
            print("Warning! (You can enter -> 1 or 2")
            save = input(s)

def add_product():
    name = input("Name: ")
    price = float(input("Price: "))
    unit = input("Unit: ")
    arount = int(input("Arount: "))
    save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)
    while True:
        if save == '1':
            user = models_admin.Product(name, price, unit, arount)
            user.add()
            print("The product insertion process was successful")
            return main_file()
        elif save == '2':
            print("The operation was canceled")
            return main_file()
        else:
            print("Warning! (You can enter -> 1 or 2")
            save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)

def edit_product():
    id = input("Enter the product ID you want to update: ")
    while True:
        if id.isdigit():
            break
        else:
            os.system("color 4")
            print("Warning! ID should be equal to type integer.")
            print(" _ _ " * 10)
            id = input("Enter the product ID you want to update: ")
    os.system("color 2")
    while True:
        if id_have("product", id) == True:
            break
        else:
            os.system("color 4")
            print("Error! There is no user with such an id")
            print(" _ _ " * 10)
            id = input("Enter the product ID you want to update: ")
    name = input("Name: ")
    price = float(input("Price: "))
    unit = input("Unit: ")
    arount = int(input("Arount: "))
    save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)
    while True:
        if save == '1':
            user = models_admin.Product(name, price, unit, arount)
            user.update(id)
            print("The user insertion process was successful")
            return main_file()
        elif save == '2':
            print("The operation was canceled")
            return main_file()
        else:
            print("Warning! (You can enter -> 1 or 2")
            save = input("""\t Save:\n\t1. Yes\t2. No\n\t>>>| """)

def delete_product():
    id = input("Enter the product ID you want to delete: ")
    while True:
        if id_have("product", id) == True:
            break
        else:
            os.system("color 4")
            print("Error! There is no product with such an id")
            print(" _ _ " * 10)
            id = input("Enter the product ID you want to delete: ")

    os.system("color 2")
    s = """Data storage:\n 1. Yes\t2. No\n\t>>>|"""
    save = input(s)
    while True:
        if save == '1':
            with sqlite3.connect("DB/database.db") as db:
                cursor = db.cursor()
                cursor.execute(f"""DELETE FROM product WHERE id = '{id}'""")
            db.commit()
            print("The product insertion process was successful")
            return main_file()
        elif save == "2":
            print("The operation was canceled")
            return main_file()
        else:
            print("Warning! (You can enter -> 1 or 2")
            save = input(s)

def delete_report_archive():
    id = input("Enter the product ID you want to delete: ")
    while True:
        if id_have("sold", id) == True:
            break
        else:
            os.system("color 4")
            print("Error! There is no product with such an id")
            print(" _ _ " * 10)
            id = input("Enter the product ID you want to delete: ")

    os.system("color 2")
    s = """Data storage:\n 1. Yes\t2. No\n\t>>>|"""
    save = input(s)
    while True:
        if save == '1':
            with sqlite3.connect("DB/database.db") as db:
                cursor = db.cursor()
                cursor.execute(f"DELETE FROM sold WHERE id = '{id}'")
            db.commit()
            print("The product insertion process was successful")
            break
        elif save == "2":
            print("The operation was canceled")
            return main_file()
        else:
            print("Warning! (You can enter -> 1 or 2")
            save = input(s)
    print("MMMMMMMMMMMMMMM")
def report_archive():
    print("\t\tReport Archive")
    x = PrettyTable()
    x.field_names = ["id", "Product id", "Amount", "User id", "Total sum", "Data"]
    with sqlite3.connect("DB/database.db") as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT id, product_id, amount, user_id, total_sum, date FROM sold")
    db.commit()
    for i in cursor.fetchall():
        x.add_row(i)
    print(x)
    return exit_panel()

def about_users():
    print("\t\tAbout users")
    with sqlite3.connect("DB/database.db") as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM users")
    db.commit()
    x = PrettyTable()
    x.field_names = ["ID", "Name", "Username", "Admins", "Password"]
    for i in cursor.fetchall():
        x.add_row(i)
    print(x)
    return exit_panel()

def about_product():
    print("\t\tAbout Product")
    with sqlite3.connect("DB/database.db") as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM product")
    db.commit()
    x = PrettyTable()
    x.field_names = ["ID", "Name", "Price", "Unit", "Amount"]
    for i in cursor.fetchall():
        x.add_row(i)
    print(x)
    return exit_panel()


def main_file():
    s = """
    1. Add user
    2. Add product
    3. Update user
    4. Delete user
    5. Update Product
    6. Delete Product
    7. Delete report archive
    8. About Report Archive
    9. About Users
    10. About Product
    0 . Exit
    \t>>>| """

    cmd = input(s)
    while True:
        if cmd == '1':
            return add_user()
        elif cmd == '2':
            return update_user()
        elif cmd == '3':
            return delete_user()
        elif cmd == '4':
            return add_product()
        elif cmd == '5':
            return edit_product()
        elif cmd == '6':
            return delete_product()
        elif cmd == '7':
            return delete_report_archive()
        elif cmd == '8':
            return report_archive()
        elif cmd == '9':
            return about_users()
        elif cmd == '10':
            return about_product()
        elif cmd == '0':
            return main_1.main()
        else:
            print("Warning! (You can enter -> 0, 1, 2, 3 ...... 8, 9")
            cmd = input(s)

# if __name__ == "__main__":
#     main_file()