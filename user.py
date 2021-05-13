class User:
    def __init__(self, userid, password, database):
        self.userid = userid
        self.password = password
        self.database = database
        self.loginstatus = False
        self.email = ""

    def verifylogin(self):
        cur = self.database.connection.cursor()
        q = 'SELECT user_pass FROM MyUsers WHERE username LIKE %s'
        if self.userid == "vijay 6326":
            cur.execute(q, [self.userid])
            password = cur.fetchone()[0]
            self.database.connection.commit()
            cur.close()
            if password == self.password:
                return "admin"
        cur.execute(q, [self.userid])
        password = cur.fetchone()[0]
        self.database.connection.commit()
        cur.close()
        return self.password == password

    def update_password(self, email):
        self.email = email
        cur = self.database.connection.cursor()
        q = 'SELECT email FROM MyUsers WHERE username LIKE %s'
        statement = cur.execute(q, [self.userid])
        if statement == 1:
            q = f"UPDATE MyUsers SET user_pass = %s WHERE  email=%s"
            cur.execute(q, [self.password, self.email])
            self.database.connection.commit()
            cur.close()


class Customer:
    def __init__(self, userid):
        self.username = userid
        self.address = ""
        self.email = ""
        self.phoneNo = 0
        self.deliveryInfo = ""
        self.password = ""

    def register(self, email, password, database):
        self.email = email
        self.password = password
        cur = database.connection.cursor()

        try:
            cur.execute("INSERT INTO MyUsers(username, email, user_pass) VALUES (%s,%s, %s)",
                        [self.username, self.email, self.password])
            database.connection.commit()
            print(1)
            return True
        except Exception:
            return False
        finally:
            cur.close()

    def login(self, password, database):
        user = User(self.username, password, database)
        return user.verifylogin()

    def updateprofile(self, key, value, info, mysql):
        cur = mysql.connection.cursor()
        q = f'UPDATE MyUsers SET {key}= %s WHERE username LIKE %s'
        info[key] = value
        cur.execute(q, [value, self.username])
        mysql.connection.commit()
        return info

    def user_data(self, mysql):
        cur = mysql.connection.cursor()
        q = 'SELECT * FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        d = cur.fetchone()
        q = 'SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "MyUsers" ORDER BY ORDINAL_POSITION'
        cur.execute(q)
        e = cur.fetchall()
        e = list(e)
        mysql.connection.commit()
        cur.close()
        info = {}
        for _ in range(len(d)):
            if d[_] is not None:
                info[e[_][0]] = d[_]
            else:
                info[e[_][0]] = "___________"
        return info

    def data_updated(self, mysql):
        cur = mysql.connection.cursor()
        q = 'SELECT * FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        d = cur.fetchone()
        mysql.connection.commit()
        cur.close()
        if d[3] is None or d[4] is None or d[5] is None:
            return False
        else:
            return True

    def Complete_Pending_Order(self, details, mysql):
        changedone = False
        details = details.split("///")
        order = list(eval(details[1]).keys())
        order = "/".join(order)
        print(order)
        cur = mysql.connection.cursor()
        q = 'SELECT pending_order,pending_order_prices FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.username])
        d = list(cur.fetchone())
        mysql.connection.commit()
        d[0] = list(d[0].split("//"))
        d[1] = list(d[1].split("/"))
        print(d)
        cost = ""
        for i in d[0]:
            if i == order:
                cost = d[1][d[0].index(i)]
                d[1].remove(d[1][d[0].index(i)])
                d[0].remove(i)
                changedone = True
        d[0] = "//".join(d[0])
        d[1] = "/".join(d[1])
        if changedone:
            if d[0] == "" and d[1] == "":
                q = 'UPDATE MyUsers SET pending_order= NULL,pending_order_prices=NULL WHERE username LIKE %s'
                cur.execute(q, [details[0]])
            else:
                q = 'UPDATE MyUsers SET pending_order= %s,pending_order_prices=%s WHERE username LIKE %s'
                cur.execute(q, [d[0], d[1], details[0]])
            mysql.connection.commit()
            q = 'SELECT prev_order,cart_price,return_cart FROM MyUsers WHERE username LIKE %s'
            cur.execute(q, [self.username])
            d = list(cur.fetchone())
            mysql.connection.commit()
            if d[0] is None:
                d[0] = order + "//"
            else:
                d[0] = d[0]+order + "//"
            if d[1] is None:
                d[1] = cost + "/"
            else:
                d[1] = d[1] + cost + "/"
            if d[2] is None:
                d[2] = "0/"
            else:
                d[2] = d[2] + "0/"
            q = 'UPDATE MyUsers SET prev_order= %s,cart_price=%s,return_cart=%s WHERE username LIKE %s'
            cur.execute(q, [d[0], d[1], d[2], details[0]])
            mysql.connection.commit()
        cur.close()
        return changedone


class Adminstrator:
    def __init__(self, mysql):
        self.userid = "vijay 6326"
        self.database = mysql

    def adduser(self, userid, email, password):
        customer = Customer(userid)
        customer.register(email, password, self.database)

    def deleteuser(self, userid):
        cur = self.database.connection.cursor()
        cur.execute(
            "DELETE FROM MyUsers WHERE username=%s",
            [userid]
        )
        self.database.connection.commit()
        cur.close()

    def updatecatalog(self, details):
        selling_cost = (int(details['cost']) * 0.5)
        cur = self.database.connection.cursor()
        try:
            cur.execute(
                "INSERT INTO furniture(catogory,product,original_cost,selling_cost,image_url,discription,no_of_items,sold_items) VALUES(%s,%s,%s,%s,%s,%s,%s,0)",
                [details['catagoryname'], details['name'], details['cost'], selling_cost, details['img'],
                 details['discription'], details['quantity']])
            self.database.connection.commit()
            cur.close()
            return True
        except Exception:
            return False

    def updateprice(self, details):
        try:
            cur = self.database.connection.cursor()
            q = 'UPDATE furniture SET selling_cost= %s WHERE product LIKE %s'
            cur.execute(q, [details['cost'], details['name']])
            self.database.connection.commit()
            cur.close()
            return True
        except Exception:
            return False

    def attention(self):
        cur = self.database.connection.cursor()
        q = 'SELECT product,no_of_items,sold_items FROM furniture'
        cur.execute(q)
        e = cur.fetchall()
        e = list(e)
        k = []
        for i in e:
            if int(i[1]) - int(i[2]) <= 1:
                k.append(i[0])
        self.database.connection.commit()
        cur.close()
        return k

    def getdata(self):
        data = {}
        cur = self.database.connection.cursor()
        q = 'SELECT COUNT(username) FROM MyUsers'
        cur.execute(q)
        data['users'] = cur.fetchall()[0][0]
        self.database.connection.commit()
        q = 'SELECT SUM(original_cost) FROM furniture'
        cur.execute(q)
        data['investment'] = cur.fetchall()[0][0]
        self.database.connection.commit()
        q = 'SELECT cart_price FROM MyUsers WHERE username LIKE "vijay 6326"'
        cur.execute(q)
        data['income'] = cur.fetchall()[0][0]
        self.database.connection.commit()
        cur.close()
        return data
