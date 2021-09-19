from flask import Flask, render_template, redirect, url_for, request
import main

# SITE SETUP
app = Flask(__name__)

@app.route('/')
def index():

    return render_template('home.html',name="Home")

@app.route('/create')
def create():
    books = main.getUsersBooks()
    return render_template('create.html',name="Create",books=books)

@app.route('/create/new', methods=['GET','POST'])
def createNew():
    if request.method == 'POST':
        index = main.addTextbook(request.form['Lesson name'])
        return redirect('/create/edit/'+str(index))
    else:
        return render_template('createNew.html',name="Create new lesson")

@app.route('/create/edit/<id>')
def edit(id):
    id = int(id)
    data = main.getInfo(id)
    name = data[0]
    data.pop(0)
    return render_template('edit.html', name=name, data=data)

# run the app
if __name__ == "__main__":
    app.run(debug=True)
