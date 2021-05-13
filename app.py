from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_mysqldb import MySQL
from user import Customer, Adminstrator, User
from Product import Category, Product, RentingCart, Orders
from return_cart import Return
from email_sender import mail, send_email
from url_generator import generate_confirmation_token, confirm_token

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'p8t6kzaeEk'
app.config['MYSQL_PASSWORD'] = '5R9kzJJJ41'
app.config['MYSQL_DB'] = 'p8t6kzaeEk'
app.config['MYSQL_PORT'] = 3306
app.config['DEFAULT_MAIL_SENDER'] = "testapp12a45@gmail.com"
app.config['SECURITY_PASSWORD_SALT'] = "vijay kumar 6326"
app.secret_key = "iamvijaykumar"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'testapp12a45@gmail.com'
app.config['MAIL_PASSWORD'] = 'Naku Teliyadhu'
mysql = MySQL(app)
data = {
    'users': 0,
    'investment': 0,
    'income': 0
}


def verifysession(user):
    cur = mysql.connection.cursor()
    q = 'SELECT user_pass FROM MyUsers WHERE username LIKE %s'
    t = cur.execute(q, [user])
    mysql.connection.commit()
    cur.close()
    if t == 1:
        return True
    else:
        return False


def login_required(func):
    def secure_function(*args, **kwargs):
        if session['username'] is not None:
            return func(*args, **kwargs)
        return redirect(url_for("hello"))

    secure_function.__name__ = func.__name__
    return secure_function


@app.route("/", methods=['GET', 'POST'])
def hello():
    session['username'] = None
    if request.method == "POST":
        details = request.form
        user = Customer(details['username'])
        if details['login'] == "signup":
            if user.register(details["email"], details["password"], mysql):
                session["username"] = user.username
                session['email'] = details["email"]
                return render_template("home.html", name=user.username)
            else:
                return render_template('login.html', sign=' ', type='hidden')
        if verifysession(details['username']):
            if details['login'] == "login":
                if user.login(details['password'], mysql) == "admin":
                    user = Adminstrator(mysql)
                    session['username'] = user.userid
                    return redirect(url_for("join_admin"))
                elif user.login(details['password'], mysql):
                    session["username"] = details['username']
                    return redirect(url_for("home"))
                else:
                    return render_template('login.html', type=' ', name='password')
        else:
            return render_template('login.html', sign=" ", signup='it may exist or over length')

    return render_template('login.html', type='hidden', sign='hidden')


@app.route("/admin", methods=['GET', 'POST'])
@login_required
def join_admin():
    user = Adminstrator(mysql)
    need = user.attention()
    data = user.getdata()
    if session['username'] == user.userid:
        if request.method == 'POST':
            details = request.form
            if details['type'] == 'add':
                user.adduser(details['name'], details['email'], details['password'])
            if details['type'] == 'delete':
                user.deleteuser(details['username'])
            if details['type'] == "update item":
                if user.updatecatalog(details):
                    return render_template("admin.html", name=session["username"], action="Successful", need=need,
                                           data=data)
                else:
                    return render_template("admin.html", name=session["username"], action="Unsuccessful", need=need,
                                           data=data)
            if details['type'] == "update price":
                if user.updateprice(details):
                    return render_template("admin.html", name=session["username"], action="Successful", need=need,
                                           data=data)
                else:
                    return render_template("admin.html", name=session["username"], action="Unsuccessful", need=need,
                                           data=data)
            if details['type'] == "update data":
                return redirect(url_for("join_admin"))
    return render_template("admin.html", name=session["username"], action="", need=need, data=data)


@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("home.html", name=session["username"])


@app.route("/account_info", methods=['GET', 'POST'])
def acoount_info():
    user = Customer(session['username'])
    info = user.user_data(mysql)
    if request.method == "POST":
        details = request.form
        if details['type'] == "return":
            ret = Return(session['username'], mysql)
            ret.update(details['content'])
            return redirect(url_for("return_cart"))
        if details['type'] == "update":
            if details['selection-1'] != "choose":
                info = user.updateprofile(details['selection-1'], details['input1'], info, mysql)
            if details['selection-2'] != "choose":
                info = user.updateprofile(details['selection-2'], details['input-2'], info, mysql)
            return render_template('account.html', **info)
    return render_template('account.html', **info)


@app.route("/return", methods=["GET", "POST"])
@login_required
def return_cart():
    ret = Return(session['username'], mysql)
    content = ret.get()
    if request.method == "POST":
        details = request.form
        if details['type'] == "return":
            additional = ret.is_return_success(details)
            ret.endreturn(additional)
            user = Customer(session['username'])
            info = user.user_data(mysql)
            return render_template('account.html', **info)
    return render_template('return.html', content=content)


@app.route("/Home/<name>", methods=["GET", "POST"])
def catogory(name):
    cato = Category(name, mysql)
    return render_template('productlist.html', name=name, list=cato.getproductsincategory())


@app.route("/<category>/<name>", methods=["GET", "POST"])
def product(category, name):
    cato = Category(category, mysql)
    item = Product(name, category, mysql)
    if request.method == "POST":
        rent = RentingCart(session['username'], mysql)
        details = request.form
        if details['type'] == "product":
            if not rent.addcartitem(item, details['quantity']):
                flash("You have exceded the limit limit your quantity")
                return render_template('product.html', **item.getproductdetails())
            else:
                return render_template('productlist.html', name=category, list=cato.getproductsincategory())
        if details['type'] == "feedback":
            item.addfeedback(session['username'], details['feedback'])
            return render_template('product.html', **item.getproductdetails())
    return render_template('product.html', **item.getproductdetails())


@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        details = request.form
        user = User(details['username'], details['password'], mysql)
        user.update_password(details['email'])
        return redirect(url_for("hello"))
    return render_template("forgot_password.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("email", None)
    return redirect(url_for("hello"))


@app.route("/cart&checkout", methods=["GET", "POST"])
def cart():
    rent = RentingCart(session['username'], mysql)
    content = rent.viewcartdetails()
    cost = rent.calprice(content)
    if request.method == "POST":
        details = request.form
        if details['type'] == "cart":
            for i in details:
                if details[i] == "+":
                    item = Product(i.split("_")[1], i.split("_")[0], mysql)
                    rent.addcartitem(item, "1")
                    return redirect(url_for("cart"))
                if details[i] == "-":
                    item = Product(i.split("_")[1], i.split("_")[0], mysql)
                    rent.deletecartitem(item, "1")
                    return redirect(url_for("cart"))
        user = Customer(session['username'])
        if user.data_updated(mysql):
            if details['type'] == "payment":
                if details['payment'] == "complete payment":
                    token = generate_confirmation_token(f"{session['username']}///{content}///{details}",
                                                        app.secret_key, app.config['SECURITY_PASSWORD_SALT'])
                    confirm_url = url_for('confirm_email', token=token, _external=True)
                    mail.init_app(app)
                    template = f'<p>An Order has been booked please confirm if you received payment.' \
                               f'</p>{session["username"]}<p>' \
                               f'<a href="{confirm_url}">{confirm_url}</a></p><br><p>Cheers!</p> '
                    send_email(app.config['DEFAULT_MAIL_SENDER'], "furniturerentalstore@gmail.com",
                               f"An Order is placed by {session['username']}", template)
                    order = Orders(rent, session['username'], mysql)
                    order.placeorder(rent.calprice(content))
                    return redirect(url_for("acoount_info"))
        else:
            flash("Please fill all the details Delivery Adress and Adress and phoneNumber")
            return render_template('checkout.html', contents=content, cost=cost)
    return render_template('checkout.html', contents=content, cost=cost)


@app.route('/confirm/<token>', methods=["GET", "POST"])
def confirm_email(token):
    username = confirm_token(token, app.secret_key, app.config['SECURITY_PASSWORD_SALT'])
    details = username.split("///")[1]
    details = eval(details)
    if request.method == "POST":
        customer = Customer(username.split("///")[0])
        if customer.Complete_Pending_Order(username, mysql):
            cur = mysql.connection.cursor()
            q = 'SELECT email FROM MyUsers WHERE username LIKE %s'
            cur.execute(q, [username.split("///")[0]])
            email = cur.fetchone()[0]
            template = f'<p>Your Order is successful you can visit and verify from our website' \
                       f'<br><p>Cheers!</p> '
            send_email(app.config['DEFAULT_MAIL_SENDER'], email,
                       f"{username.split('///')[0]}, Your Order has been conformed", template)
            flash('Order Payment is confirmed. Thanks!', 'success')
            return render_template("confirm.html",
                                   user=username.split("///")[0],
                                   details=list(dict(details).keys()),
                                   bank=eval(username.split("///")[2].split("[")[1].split("]")[0])[1][1])
        else:
            flash('Conformation is Already')
            return render_template("confirm.html",
                                   user=username.split("///")[0],
                                   details=list(dict(details).keys()),
                                   bank=eval(username.split("///")[2].split("[")[1].split("]")[0])[1][1])

    return render_template("confirm.html",
                           user=username.split("///")[0],
                           details=list(dict(details).keys()),
                           bank=eval(username.split("///")[2].split("[")[1].split("]")[0])[1][1])


if __name__ == "__main__":
    app.run(debug=True)
