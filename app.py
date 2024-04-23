
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
    title = request.form.get('title')
    descr= request.form.get('descr')
    new_task = Todo(title=title, description=descr)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
       db.session.delete(task_to_delete)
       db.session.commit()
       return redirect('/')
    except:
       return "There is a problem deleting"
    


@app.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    task_to_update= Todo.query.get_or_404(id)
    if request.method =='POST':
       title = request.form.get('title')
       descr= request.form.get('descr')
       task_update = Todo(title=title, description=descr)
       db.session.add(task_update)
       db.session.commit()
       return redirect(url_for('index'))

    else:
        return render_template('update.html', task=task_to_update)

    
    


# @app.route('/update')



if __name__=="__main__":
   app.run(debug=True)

