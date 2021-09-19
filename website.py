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

@app.route('/create/edit/<id>', methods=['GET','POST'])
def edit(id):
    id = int(id)
    data = main.getInfo(id)
    name = data[0]
    chapters = data[1]
    content = data[2]

    if request.method == 'POST':
        print(request.form['chapters'])
        print("content")
        print(request.form['contents'])
        main.update(id,request.form['chapters'], request.form['contents'])

        id = int(id)
        data = main.getInfo(id)
        name = data[0]
        chapters = data[1]
        content = data[2]

    return render_template('edit.html',id=id, name=name, chapters=chapters, content=content)

@app.route('/view/<id>', methods=['GET','POST'])
def view(id):

    id = int(id)
    data = main.getInfo(id)
    name = data[0]
    chapters = data[1]
    content = data[2]

    return render_template('view.html',id=id, name=name, chapters=chapters, content=content)

# run the app
if __name__ == "__main__":
    app.run(debug=True)
