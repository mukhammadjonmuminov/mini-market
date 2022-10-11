import models_admin
import sqlite3
path = "DB/database.db"

def print_product_name(id):
    with sqlite3.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT name, unit FROM product WHERE id = {id}")
    db.commit()
    a = []
    for i in cursor:
        a.append(i)
    return a

def sold(product_id, amount, user_id, total_sum, date):
    with sqlite3.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(f"INSERT INTO sold(product_id, amount, user_id, total_sum, date) VALUES (?, ?, ?, ?, ?)",
                       [product_id, amount, user_id, total_sum, date])
    db.commit()

def delete_sold(n, m):
    return models_admin.delete(n, m)

def user_id(username, password):
    with sqlite3.connect(path) as db:
        cursor = db.cursor()
        cursor.execute(f"SELECT id FROM users WHERE (username = '{username}' and password = '{password}')")
    return cursor

if __name__ == "__main__":
    delete_sold(1, 499)