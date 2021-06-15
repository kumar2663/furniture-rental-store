import os
class Return:
    def __init__(self, user, database):
        self.user = user
        self.database = database
        self.content = ""
        self.details = None

    def update(self, content):
        cur = self.database.connection.cursor()
        q = 'UPDATE MyUsers SET dummy = %s WHERE username LIKE %s'
        cur.execute(q, [content, self.user])
        self.database.connection.commit()
        cur.close()

    def get(self):
        cur = self.database.connection.cursor()
        q = 'SELECT dummy FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.user])
        e = cur.fetchall()[0][0]
        self.database.connection.commit()
        cur.close()
        return e

    def is_return_success(self, details):
        content = self.get()
        su = 0
        self.details = details
        cur = self.database.connection.cursor()
        q = 'SELECT original_cost FROM furniture WHERE product LIKE %s'
        for i in content.split("/"):
            cur.execute(q, [i.split("-")[0]])
            e = cur.fetchall()[0][0]
            self.database.connection.commit()
            su = su + int(e) * int(details[i.split("-")[0]])
        cur.close()
        return [su, details]

    def endreturn(self, details):
        content = self.get()
        cur = self.database.connection.cursor()
        q = 'SELECT additional FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.user])
        e = cur.fetchall()[0][0]
        self.database.connection.commit()
        if e is not None:
            e = str(int(e) + int(details[0]))
        else:
            e = details[0]
        q = 'UPDATE MyUsers SET additional = %s WHERE username LIKE %s'
        cur.execute(q, [e, self.user])
        self.database.connection.commit()
        q = 'SELECT cart_price FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [os.environ['ADMIN_NAME']])
        e = cur.fetchall()[0][0]
        self.database.connection.commit()
        if e is not None:
            e = str(int(e) + int(details[0]))
        else:
            e = details[0]
        q = 'UPDATE MyUsers SET cart_price = %s WHERE username LIKE "vijay 6328"'
        cur.execute(q, [e])
        self.database.connection.commit()
        for i in content.split("/"):
            q = 'SELECT no_of_items FROM furniture WHERE product LIKE %s'
            cur.execute(q, [i.split("-")[0]])
            e = cur.fetchall()[0][0]
            self.database.connection.commit()
            e = str(int(e) - int(details[1][i.split("-")[0]]))
            q = 'UPDATE furniture SET no_of_items = %s WHERE product LIKE %s'
            cur.execute(q, [e, i.split("-")[0]])
            self.database.connection.commit()
        for i in content.split("/"):
            q = 'SELECT sold_items FROM furniture WHERE product LIKE %s'
            cur.execute(q, [i.split("-")[0]])
            e = cur.fetchall()[0][0]
            self.database.connection.commit()
            e = str(int(e) - int(i.split("-")[1]))
            q = 'UPDATE furniture SET sold_items = %s WHERE product LIKE %s'
            cur.execute(q, [e, i.split("-")[0]])
            self.database.connection.commit()
        q = 'SELECT prev_order FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.user])
        e = cur.fetchall()[0][0].split("//")
        q = 'SELECT return_cart FROM MyUsers WHERE username LIKE %s'
        cur.execute(q, [self.user])
        ret = cur.fetchall()[0][0].split("/")
        for i in range(len(e)):
            if content == e[i]:
                ret[i] = "1"
        ret = "/".join(ret)
        q = 'UPDATE MyUsers SET return_cart = %s WHERE username LIKE %s'
        cur.execute(q, [ret, self.user])
        self.database.connection.commit()
        cur.close()
