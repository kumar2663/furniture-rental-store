import math
import os


class Category:
    def __init__(self, name, mysql):
        self.database = mysql
        self.name = name

    def getproductsincategory(self):
        cur = self.database.connection.cursor()
        q = 'SELECT * FROM furniture WHERE catogory LIKE %s'
        cur.execute(q, [self.name])
        d = cur.fetchall()
        d = list(d)
        q = 'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE ' \
            'TABLE_NAME = "furniture" ORDER BY ORDINAL_POSITION'
        cur.execute(q)
        e = cur.fetchall()
        e = list(e)
        self.database.connection.commit()
        cur.close()
        product_list = {}
        for i in range(len(d)):
            product_list['product-' + str(i + 1)] = {}
            for j in range(len(e)):
                product_list['product-' + str(i + 1)][e[j][0]] = d[i][j]
        return product_list


class Product:
    def __init__(self, name, catogery, mysql):
        cur = mysql.connection.cursor()
        q = 'SELECT * FROM furniture WHERE product LIKE %s'
        cur.execute(q, [name])
        d = cur.fetchall()
        mysql.connection.commit()
        d = list(d)
        q = 'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE ' \
            'TABLE_NAME = "furniture" ORDER BY ORDINAL_POSITION'
        cur.execute(q)
        e = cur.fetchall()
        e = list(e)
        mysql.connection.commit()
        cur.close()
        product_list = {}
        if d:
            for j in range(len(e)):
                product_list[e[j][0]] = d[0][j]
        self.p = product_list
        if product_list != {}:
            self.database = mysql
            self.name = name
            self.catogory = product_list['catogory']
            self.original_cost = product_list['original_cost']
            self.selling_cost = product_list['selling_cost']
            self.image_url = product_list['image_url']
            self.no_of_items = product_list['no_of_items']
            self.sold_items = product_list['sold_items']
            self.feedback = product_list['feedback']

    def getproductdetails(self):
        return self.p

    def addfeedback(self,user,feedback):
        cur = self.database.connection.cursor()
        q = 'SELECT feedback FROM furniture WHERE product LIKE %s'
        cur.execute(q, [self.name])
        e = cur.fetchall()
        e = e[0][0]
        text = user+'-'+feedback+'/'
        if e is None:
            q = 'UPDATE furniture SET feedback = %s WHERE  product LIKE %s'
            cur.execute(q, [text, self.name])
            self.database.connection.commit()
            cur.close()
        else:
            q = 'UPDATE furniture SET feedback = %s WHERE  product LIKE %s'
            cur.execute(q, [e + text, self.name])
            self.database.connection.commit()
            cur.close()

    def checkremain(self):
        return int(self.no_of_items) - int(self.sold_items)

    def updatesale(self, quantity):
        cur = self.database.connection.cursor()
        q = 'SELECT sold_items FROM furniture WHERE product LIKE %s'
        cur.execute(q, [self.name])
        e = cur.fetchall()
        q = 'UPDATE furniture SET sold_items = %s WHERE  product LIKE %s'
        quantity = str(int(quantity) + int(e[0][0]))
        cur.execute(q, [quantity, self.name])
        self.database.connection.commit()
        cur.close()


class RentingCart:
    def __init__(self, username, mysql):
        self.username = username
        self.database = mysql
        self.price = 0
        self.order = {}

    def addcartitem(self, item, quantity):
        cur = self.database.connection.cursor()
        q = 'SELECT renting_cart FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        e = cur.fetchall()
        self.database.connection.commit()
        cur.close()
        product = item.name + '-' + quantity + '/'
        y = 0
        su = 0
        if e[0][0] is None:
            if item.checkremain() >= int(quantity):
                cur = self.database.connection.cursor()
                q = "UPDATE MyUsers SET renting_cart = %s WHERE  username LIKE %s"
                cur.execute(q, [product, self.username])
                self.database.connection.commit()
                cur.close()
                y = 1
                item.updatesale(quantity)

        else:
            print(1)
            p = e[0][0].split("/")
            for i in range(len(p)):
                k = p[i].split("-")
                if k[0] == item.name:
                    print(2)
                    if int(quantity) <= item.checkremain():
                        k[1] = str(int(k[1]) + int(quantity))
                        su = k[1]
                k = '-'.join(k)
                p[i] = k
                print(p[i])
            e = '/'.join(p)
            print(e)
            if su == 0:
                print(3)
                if item.checkremain() >= int(quantity):
                    cur = self.database.connection.cursor()
                    q = "UPDATE MyUsers SET renting_cart = %s WHERE  username LIKE %s"
                    cur.execute(q, [e + product, self.username])
                    self.database.connection.commit()
                    cur.close()
                    y = 1
                    item.updatesale(quantity)
            else:
                print(4)
                if item.checkremain() >= int(quantity):
                    cur = self.database.connection.cursor()
                    q = "UPDATE MyUsers SET renting_cart = %s WHERE  username LIKE %s"
                    cur.execute(q, [e, self.username])
                    self.database.connection.commit()
                    cur.close()
                    y = 1
                    item.updatesale(quantity)
        if y == 1:
            return True
        else:
            return False

    def deletecartitem(self, item, quantity):
        cur = self.database.connection.cursor()
        q = 'SELECT renting_cart FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        e = cur.fetchall()
        self.database.connection.commit()
        cur.close()
        p = e[0][0].split("/")
        for i in range(len(p)):
            su = 10
            k = p[i].split("-")
            if k[0] == item.name:
                k[1] = str(int(k[1]) - int(quantity))
                su = int(k[1])
                item.updatesale(str(-int(quantity)))
            if su == 0:
                p[i] = ''
            else:
                k = '-'.join(k)
                p[i] = k
        p = [i for i in p if i != '']
        if not p:
            cur = self.database.connection.cursor()
            q = "UPDATE MyUsers SET renting_cart = NULL WHERE  username LIKE %s"
            cur.execute(q, [self.username])
            self.database.connection.commit()
            cur.close()
        else:
            e = '/'.join(p)
            cur = self.database.connection.cursor()
            q = "UPDATE MyUsers SET renting_cart = %s WHERE  username LIKE %s"
            cur.execute(q, [e + '/', self.username])
            self.database.connection.commit()
            cur.close()

    def viewcartdetails(self):
        cart = {}
        cur = self.database.connection.cursor()
        q = 'SELECT renting_cart FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        e = cur.fetchall()
        self.database.connection.commit()
        if e[0][0] is not None:
            e = e[0][0].split("/")
            for _ in range(len(e) - 1):
                cart[e[_]] = {}
                k = e[_].split("-")
                q = 'SELECT selling_cost,catogory FROM furniture WHERE product LIKE %s'
                cur.execute(q, [k[0]])
                c = cur.fetchall()
                self.database.connection.commit()
                cart[e[_]]['name'] = k[0]
                cart[e[_]]['cost'] = str(int(c[0][0]) * int(k[1]))
                cart[e[_]]['catogory'] = c[0][1]
                cart[e[_]]['quantity'] = k[1]
        cur.close()
        self.order = cart
        return cart

    def calprice(self, content, loan=None):
        price = 0
        if loan is not None:
            for i in content.keys():
                price = int(content[i]['cost']) + price
                price = price + math.floor(price * 0.04)
        else:
            for i in content.keys():
                price = int(content[i]['cost']) + price
                price = price
        return str(price)

    def checkout(self, cost):
        cur = self.database.connection.cursor()
        q = 'SELECT prev_order FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        self.database.connection.commit()
        e = cur.fetchall()
        e = e[0][0]
        if e is None:
            q = 'SELECT renting_cart FROM MyUsers WHERE username LIKE %s'
            cur.execute(q, [self.username])
            self.database.connection.commit()
            c = cur.fetchall()
            c = c[0][0]
            e = c
            q = 'UPDATE MyUsers SET prev_order=%s WHERE username=%s'
            cur.execute(q, [e + '/', self.username])
            self.database.connection.commit()
            q = 'UPDATE MyUsers SET renting_cart=NULL WHERE username=%s'
            cur.execute(q, [self.username])
            self.database.connection.commit()
        else:
            q = 'SELECT renting_cart FROM MyUsers WHERE username LIKE %s'
            cur.execute(q, [self.username])
            self.database.connection.commit()
            c = cur.fetchall()
            c = c[0][0]
            e = e + c
            q = 'UPDATE MyUsers SET prev_order=%s WHERE username=%s'
            cur.execute(q, [e + '/', self.username])
            self.database.connection.commit()
            q = 'UPDATE MyUsers SET renting_cart=NULL WHERE username=%s'
            cur.execute(q, [self.username])
            self.database.connection.commit()
        q = 'SELECT cart_price FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        self.database.connection.commit()
        c = cur.fetchall()
        c = c[0][0]
        if c is None:
            q = 'UPDATE MyUsers SET cart_price=%s WHERE username=%s'
            cur.execute(q, [str(cost) + '/', self.username])
            self.database.connection.commit()
        else:
            q = 'UPDATE MyUsers SET cart_price=%s WHERE username=%s'
            cur.execute(q, [c + str(cost) + '/', self.username])
            self.database.connection.commit()
        q = 'SELECT cart_price FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [os.environ['ADMIN_NAME']])
        self.database.connection.commit()
        c = cur.fetchall()
        c = c[0][0]
        if c is None:
            q = 'UPDATE MyUsers SET cart_price=%s WHERE username=%s'
            cur.execute(q, [cost, os.environ['ADMIN_NAME']])
            self.database.connection.commit()
        else:
            q = 'UPDATE MyUsers SET cart_price=%s WHERE username=%s'
            cost = str(int(c.split("/")[0]) + int(cost))
            cur.execute(q, [cost, os.environ['ADMIN_NAME']])
            self.database.connection.commit()
        cur.close()
        return e[0][0]


class Orders:
    def __init__(self, cart, username, database):
        self.cart = cart
        self.username = username
        self.database = database
        self.confirm = False

    def placeorder(self, cost):
        self.cart.viewcartdetails()
        self.cart.checkout(cost)
        cur = self.database.connection.cursor()
        q = 'SELECT return_cart FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        d = list(cur.fetchone())
        self.database.connection.commit()
        if d[0] is None:
            d[0] = "0/"
        else:
            d[0] = d[0] + "0/"
        q = 'UPDATE MyUsers SET return_cart=%s WHERE username LIKE %s'
        cur.execute(q, [d[0], self.username])
        self.database.connection.commit()
        cur.close()
