import admin_panel
import models_user
import user_panel
import sqlite3
import os

def user_have():
    with sqlite3.connect("DB/database.db") as db:
        cursor = db.cursor()
        cursor.execute("Select username, admins, password from users")
    return cursor

def main():
    print("""\t\tMain Main""")
    username = input("Username: ")
    password = input("Password: ")
    user = []
    pas = []
    for i in user_have():
        user.append(i[0])
        pas.append(str(i[2]))
    while True:
        if user.count(username) == 1 and pas.count(password) > 0:
            os.system("color 2")
            break
        else:
            os.system("color 4")
            print("Warning! User not fount!")
            username = input("Username: ")
            password = input("Password: ")
    for i in user_have():
        if (i[0] == username and  i[2] == password ) and i[1] == '1':
            return admin_panel.main_file()
        elif (i[0] == username and i[2] == password) and i[1] == '0':
            id = models_user.user_id(username, password)
            return user_panel.main(id.__str__())

if __name__ == "__main__":
    main()
