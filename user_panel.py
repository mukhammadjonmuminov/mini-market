import sqlite3
from datetime import datetime
import models_user
path = "DB/database.db"

def print_product_name( id):
    with sqlite3.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT name, price, unit FROM product WHERE id = {id}")
    db.commit()
    a = []
    for i in cursor:
        a.append(*i)
    return a

def buy(id):
    with sqlite3.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(f"Select name, price, unit, amount from product Where id = '{id}'")
    db.commit()
    for i in cursor:
        return [*i]


def user_id(username, password):
    with sqlite3.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM users WHERE (username = '{username}' and password = '{password}')")
    return cursor

def add_product(user_id, all):
    id = input("Product id: ")
    print(buy(id)[0], " - ", buy(id)[2])
    amount = int(input("Amount: "))
    s = 0
    for i in all:
        s += all[4]
    s += float(buy(id)[1]) * int(amount)
    print(f"Products price - {s}")
    core = [id, amount, s]
    return condition(user_id, core)

def condition(user_id, core):
    cmd = input("\tSell\n1. Yes   2.No \n\t>>>| ")
    while True:
        if cmd == '1':
            now = datetime.now()
            date = now.strftime("%x")
            all = [core[0], core[1], user_id, core[2], date]
            models_user.sold(all[0], all[1], all[2], all[3], all[4])
            print("Finish")
            break
        elif cmd == '2':
            del all
            print("Finished")
            print("_______________________________")
            print("Start")
            return main(user_id)
        else:
            print("Warning! You can => 1, 2, 3")
            cmd = input(" 1. Sell\n\t2. Add product\n\t3. Delet")

    print(f"{buy(all[0])[0]} -> {all[1]} * {buy(all[0])[1]} = {all[3]}")
    print("Finished")
    print("_______________________________")
    print("Start")
    return main(user_id)

def main(user_id):
    id = input("Product id: ")
    print(buy(id)[0], " - ",  buy(id)[2])
    amount = int(input("Amount: "))
    s = float(buy(id)[1]) * int(amount)
    print(f"Products price - {s}")
    core = [id, amount, s]

    return condition(user_id, core)




