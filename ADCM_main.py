from flask import Flask , render_template,jsonify
from flask_bower import Bower
from flask_triangle import Triangle

app = Flask(__name__)
Bower(app)
Triangle(app)

@app.route('/')
def index():
    return render_template('index.html')


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
