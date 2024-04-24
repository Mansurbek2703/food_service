
from flask import Flask , render_template, request,redirect
from db.db import obj
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")



@app.route('/foods')
def menulist():
    foodlist = obj.foodlist()
    return render_template("menu/menulist.html",foodlist = foodlist)

@app.route("/haqida")
def haqida():
    return render_template("about.html")

@app.route("/detail/<id>/<nomi>/")
def menudetail(id,nomi):
    ovqat=obj.menudetail(id)
    return render_template("menu/menudetail.html", ovqat=ovqat, nomi=nomi)

@app.route("/savatcha")
def savatcha():
    zakazlar=obj.savatcha()
    return render_template("zakaz/savatcha.html", zakazlar=zakazlar)

@app.route("/addsavat/<ovqatid>/")
def addsavat(ovqatid):
    pass

@app.route('/zakazqushish', methods=['GET', 'POST'])
def add():
    if request.method=='GET':
        return render_template('zakaz/zakazqushish.html')
    elif request.method=='POST':
        ism =request.form['ism']
        familiya=request.form['familiya']
        tel=request.form['tel']
        obj.zakazqushish(ism,familiya,tel)
        return redirect('/savatcha')

@app.route('/login')
def login():
    return render_template("users/login.html")

@app.route("/user/registration/")
def registr():
    return render_template(("users/registr.html"))

if __name__=="__main__":
    app.run(debug=True)



