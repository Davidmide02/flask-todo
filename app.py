
from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db.sqlite'

db = SQLAlchemy(app)




class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
       return f'<Todo {self.title}'




@app.route('/', methods=["POST","GET"])
def index():
    if request.method=="POST":
     title= request.form.title
     todo_list = Todo.query.all()
     print(todo_list)
     print("index file block here")
     return render_template('base.html',)
    else: 
       print("welcome")
       todo_list = Todo.query.all()
       print(todo_list)
       return render_template('base.html',todo_list=todo_list)

@app.route('/add', methods=["POST"])
def add():
    # todo_list = Todo.query.all()
    # print(todo_list)
    title = request.form.get('title')
    descr= "Hard codoed value decr"
    new_task = Todo(title=title, description=descr, completed=True)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))
    # return render_template('about.html')


# @app.route('/update')



if __name__=="__main__":
   app.run(debug=True)

