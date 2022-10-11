import sqlite3

class User:
    path = "DB/database.db"
    def __init__(self, name: str, username: str, admins: str, password: int, id =None):
        self.name = name
        self.username = username
        self.admins = admins
        self.password = password
        self.id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            self.__name = "NULL"

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if isinstance(username, str):
            self.__username = username
        else:
            self.__username = "NULL"

    @property
    def admins(self):
        return self.__admins

    @admins.setter
    def admins(self, admins):
        if isinstance(admins, str):
            self.__admins = admins
        else:
            self.__admins = "NULL"

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if isinstance(password, int):
            self.__password = password
        else:
            self.__password = "NULL"

    def __str__(self):
        return f"{self.username} {self.admins} {self.password}"




    def add(self):
        with sqlite3.connect(User.path) as db:
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO users(name, username, admins, password) VALUES (?, ?, ?, ?)",
                           [self.name, self.username, self.admins, self.password])

    def delete(id):
        path = "DB/database.db"
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"""DELETE FROM users WFERE id = {id}""")
        db.commit()

    def update(self, id):
        path = "DB/database.db"
        with sqlite3.connect(path) as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE users SET name = '{self.name}', username = '{self.username}', admins = '{self.admins}', password = {self.password}"
                           f" WHERE id = '{id}'")
        db.commit()

class Product:
    path = "DB/database.db"
    def __init__(self, name: str, price: float, unit: str, amount: int, id = None):
        self.name = name
        self.price = price
        self.unit = unit
        self.amount = amount
        self.id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.isalpha():
            self.__name = name
        else:
            self.__name = "NULL"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if isinstance(price, float):
            self.__price = price
        else:
            self.__price = price

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        if isinstance(unit, str) and unit.isalpha():
            self.__unit = unit
        else:
            self.__unit = "NULL"

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int):
            self.__amount = amount
        else:
            self.__amount = "NULL"


    def add(self):
        with sqlite3.connect(Product.path) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO product(name, price, unit, amount) VALUES (?, ?, ?, ?)",
                           [self.name, self.price, self.unit, self.amount]
                           )
        db.commit()

    def delete(self, id):
        with sqlite3.connect(Product.path) as db:
            cursor = db.cursor()
            cursor.execute(f"DELETE FROM product WHERE id = '{id}')")
        db.commit()

    def update(self, id):
        with sqlite3.connect(Product.path) as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE product SET name = '{self.name}', price = '{self.price}', amount = '{self.amount}' WHERE id = '{id}'")
        db.commit()


    def __str__(self):
        return f"{self.name} {self.price} {self.amount}"

class Sold:
    path = "DB/database.db"
    def __init__(self, product_id: int, amount: int, user_id: int, date: str, id= None):
        self.product_id = product_id
        self.amount = amount
        self.user_id = user_id
        self.date = date
        self.id = id

    @property
    def product_id(self):
        return self.__product_id

    @product_id.setter
    def product_id(self, product_id):
        if isinstance(product_id, int):
            self.__product_id = product_id
        else:
            self.__product_id = "NULL"

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, amount):
        if isinstance(amount, int):
            self.__amount = amount
        else:
            self.__amount = "NULL"

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, user_id):
        if isinstance(user_id, int):
            self.__user_id = user_id
        else:
            self.__user_id = "NULL"

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        if isinstance(date, str):
            self.__date = date
        else:
            self.__user_id = "NULL"

    def add(self):
        with sqlite3.connect(Sold.path) as db:
            cursor = db.cursor()
            cursor.execute("INSERT INTO sold(product_id, amount, user_id, date) VALUES (?, ?, ?, ?)",
                           [self.product_id, self.amount, self.user_id, self.date])
        db.commit()


    def update(self, id):
        with sqlite3.connect(Sold.path) as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE sold SET name = '{self.product_id}', price = '{self.amount}', amount = '{self.user_id}', date = '{self.date}' WHERE id = '{id}'")
        db.commit()


def __str__(self):
    return f"{self.product_id} {self.amount} {self.user_id} {self.date}"

