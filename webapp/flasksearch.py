from wtforms import Form, StringField, SelectField
from flask import Flask, render_template
from flask import flash, render_template, request, redirect
import pymysql

app = Flask(__name__)

class ItemSearchForm(Form):
    choices = [('Name','Name')]
    select = SelectField('Search for item:', choices=choices)
    search = StringField('')

@app.route('/', methods=['GET','POST'])
def index(): 
    search = ItemSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    
    return render_template('index.html',form=search)

@app.route('/results')
def search_results(search):
    mydb = pymysql.connect(
        host="",
        user="",
        passwd="",
        database=""
    )
    results = [] 
    search_string = search.data['search']

# Check if data is empty return all, else return like clause 
    if search_string=='':
        mycursor = mydb.cursor()
        sql = "Select name,price,link from items"
        mycursor.execute(sql)
        results = mycursor.fetchall()
    else:
        mycursor = mydb.cursor()
        sql = "Select name,price,link from items where lower(name) like lower('%{}%')".format(search_string)
        mycursor.execute(sql)
        results = mycursor.fetchall()
    return render_template('items.html',result=results)

        