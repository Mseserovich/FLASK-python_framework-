from flask import Flask, render_template, url_for, request
import sqlite3
app = Flask(__name__)
total_price = 1
price1 = 'R15'
price2 = 'R18'
price3 = 'R20'
price4 = 'R22'
price5 = 'R14.50'
price6 = 'R25'

@app.route('/')
def home():
    return render_template('jinja_index.html', title='Chess Code Cafe')

@app.route('/login')
def login():
    return render_template('jinja_login.html')

@app.route('/menu')
def menu():
    
    return render_template('jinja_menu.html', price1=price1, price2=price2, price3 = price3, price4=price4, price5=price5, price6=price6, total_price=total_price)

@app.route('/about')
def about():
    
    return render_template('jinja_about.html')

@app.route('/register')
def register():

    return render_template('Layout.html')

@app.route('/welcome', methods=["POST", "GET"])
def welcome():
    name = request.args.get("name")
    email = request.args.get("email")
    password = request.args.get("password")

    #Server side form validation
    #if not name or not email or not password:
        #return 'try again'
    
    with sqlite3.connect("database.db") as con:
        cur = con.cursor()
    cur.execute("INSERT INTO buyers(name, email, password) VALUES (?, ?, ?)", (name, email, password))
    
    con.commit()
    return render_template('jinja_profile.html', name =name)
    

@app.route('/list')
def list():
    con = sqlite3.connect("database.db")
    con.row_factory = sqlite3.Row
   
    cur = con.cursor()
    #cur.execute("UPDATE buyers SET email = 'ts1@gmail.com'")
    cur.execute("select * from buyers")
   
    rows = cur.fetchall()
    return render_template("jinja_result.html",rows = rows)

if __name__ == '__main__':
    app.run()
