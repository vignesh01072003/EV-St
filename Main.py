
from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from werkzeug.utils import secure_filename
import datetime
import mysql.connector
import sys
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():

    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():

    return render_template('AdminLogin.html')

@app.route("/cbunk")
def cbunk():
    return render_template('cbunk.html')
@app.route("/vbunk")
def vbunk():
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
    # cursor = conn.cursor()
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM bunk ")
    data1 = cur1.fetchall()
    return render_template('vbunk.html',data=data1)

@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register ")
    data = cur.fetchall()

    return render_template('AdminHome.html', data=data)
@app.route("/viewrequest")
def viewrequest():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM booking where status='Waiting'")
    data = cur.fetchall()
    return render_template('viewrequest.html', data=data)

@app.route("/citizenLogin")
def citizenLogin():
    return render_template('citizenLogin.html')
@app.route("/citizenlogin")
def citizenlogin():
    return render_template('citizenLogin.html')

@app.route("/citizenregister")
def citizenregister():
    return render_template('NewUser.html')

@app.route("/viewstatus")
def viewstatus():
    conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
    # cursor = conn.cursor()
    cur1 = conn1.cursor()
    cur1.execute("SELECT * FROM land where status='Accepted' and amount!=''")
    data1 = cur1.fetchall()

    return render_template('viewstatus.html',data1=data1)
@app.route("/UserHome")
def UserHome():
    uname=session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM register where uname='" + uname + "'")
    data = cur.fetchall()

    return render_template('UserHome.html', data=data)
    return render_template('UserHome.html')

@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

           conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
           # cursor = conn.cursor()
           cur = conn.cursor()
           cur.execute("SELECT * FROM register ")
           data = cur.fetchall()

           return render_template('AdminHome.html' , data=data)

       else:
        return render_template('index.html', error=error)

@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():

    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + username + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            alert = 'Username or Password is wrong'
            render_template('goback.html', data=alert)



        else:
            print(data[0])
            session['uid'] = data[0]
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM register where uname='" + username + "' and password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data )







@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':

        name1 = request.form['name']
        gender = request.form['gender']
        age = request.form['age']
        email = request.form['email']

        phone = request.form['phone']

        address = request.form['address']
        uname = request.form['uname']
        password = request.form['psw']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        cursor = conn.cursor()
        cursor.execute("SELECT * from register where uname='" + uname + "' and password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO register VALUES ('','" + name1 + "','" + gender + "','" + age + "','" + email + "','" + phone + "','" + address + "','" + uname + "','" + password + "')")
            conn.commit()
            conn.close()



        else:
            return "User Name and Password Is Already Given"





    return render_template('citizenLogin.html')

@app.route("/action")
def action():
    id = request.args.get('id')
    act = request.args.get('act')
    if act=='Accept':
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        cursor = conn.cursor()
        cursor.execute("update booking set status='"+act+"' where id='"+id+"'")
        conn.commit()
        conn.close()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM booking where status='Waiting'")
        data = cur.fetchall()
        return render_template('viewrequest.html', data=data)
    if act=='Reject':
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        cursor = conn.cursor()
        cursor.execute("update booking set status='" + act + "' where id='" + id + "'")
        conn.commit()
        conn.close()
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM booking where status='Waiting'")
        data = cur.fetchall()
        return render_template('viewrequest.html', data=data)









@app.route("/search", methods=['GET', 'POST'])
def search():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT city FROM bunk ")
    data = cur.fetchall()
    print(data)

    return render_template("search.html",data1=data)

@app.route("/Send")
def Send():


         #categories=request.form['id']
         id=request.args.get('id')
         conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
         cursor = conn.cursor()

         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
         # cursor = conn.cursor()
         cur1 = conn1.cursor()
         cur1.execute("SELECT * FROM land where id='"+id+"'")
         data = cur1.fetchall()
         return render_template("sendpaper.html", data=data)



@app.route("/accept")
def accept():


         #categories=request.form['id']
         id=request.args.get('id')
         act = request.args.get('act')


         return render_template("paperpub.html")
@app.route("/addbunk", methods=['GET', 'POST'])
def addbunk():

    if request.method == 'POST':
        name = request.form['name']
        city=request.form['city']
        location = request.form['location']
        solt = request.form['solt']
        amount = request.form['amount']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        cursor = conn.cursor()
        cursor.execute(
            "insert into bunk values('','" + name + "','"+city+"','" + location + "','" + solt + "','" + amount + "')")
        conn.commit()
        conn.close()
        return render_template("cbunk.html")

@app.route("/searchbunk", methods=['GET', 'POST'])
def searchbunk():

        location = str(request.form['location'])
        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        # cursor = conn.cursor()
        cur1 = conn1.cursor()
        sql = 'SELECT * FROM bunk where location LIKE %s'
        args = ['%'+location + '%']
        cur1.execute(sql, args)
        #cur1.execute("SELECT * FROM bunk where location LIKE (%s%)"%(location))
        data = cur1.fetchall()
        print(data)
        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        # cursor = conn.cursor()
        cur1 = conn1.cursor()
        cur1.execute("SELECT DISTINCT city FROM bunk ")
        data1 = cur1.fetchall()



        return render_template("search.html",data=data)
@app.route("/request1")
def request1():


         #categories=request.form['id']
         id=request.args.get('id')
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
         # cursor = conn.cursor()
         cur1 = conn1.cursor()
         cur1.execute("SELECT * FROM bunk where id='"+id+"'")
         data1 = cur1.fetchall()



         return render_template("booking.html",data=data1)
@app.route("/booking", methods=['GET', 'POST'])
def booking():


        id = request.form['id']
        name = request.form['name']
        location = request.form['location']
        amount = request.form['amount']
        date = request.form['date']
        slot = request.form['slot']
        uname=session['uname']
        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
        # cursor = conn.cursor()
        cur1 = conn1.cursor()
        cur1.execute("SELECT * FROM booking where date='" + date + "' and slot='"+slot+"'")
        data1 = cur1.fetchone()
        if data1 is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
            cursor = conn.cursor()
            cursor.execute(
                "insert into booking values('','" + id + "','" + name + "','" + location + "','" + amount + "','" + date + "','" + slot + "','" + uname + "','Waiting','')")
            conn.commit()
            conn.close()

            conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
            # cursor = conn.cursor()
            cur1 = conn1.cursor()
            cur1.execute("SELECT * FROM booking where uname='" + uname + "'")
            data1 = cur1.fetchall()

            return render_template("notification.html", data=data1)
        else:
            return "Slot Already Booked"

@app.route("/notifi")
def notifi():


         #categories=request.form['id']
         uname=session['uname']
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
         # cursor = conn.cursor()
         cur1 = conn1.cursor()
         cur1.execute("SELECT * FROM booking where uname='"+uname+"'")
         data1 = cur1.fetchall()



         return render_template("notification.html",data=data1)

@app.route("/viewbooking")
def viewbooking():


         #categories=request.form['id']
         uname=session['uname']
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
         # cursor = conn.cursor()
         cur1 = conn1.cursor()
         cur1.execute("SELECT * FROM booking where uname='"+uname+"' and status='Accept'")
         data1 = cur1.fetchall()



         return render_template("viewbooking.html",data=data1)
@app.route("/vrecharge")
def vrecharge():


         #categories=request.form['id']
         uname=session['uname']
         conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='lams1')
         # cursor = conn.cursor()
         cur1 = conn1.cursor()
         cur1.execute("SELECT * FROM booking where status='Accept'")
         data1 = cur1.fetchall()



         return render_template("vrecharge.html",data=data1)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)