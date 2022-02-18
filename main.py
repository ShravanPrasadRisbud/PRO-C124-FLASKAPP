from flask import Flask,jsonify, request

app = Flask(__name__)

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

{
  "data": [
    {
      'Contact': "9987644456",
      'Name': 'Raju',
      'done': False,
      'id': 1
    },
    {
      'Contact': "9876543222",
      'Name': 'Rahul',
      'done': False,
      'id': 2
    }
  ]
}

@app.route("/")
def hello_world():
  return "Hello World!"

@app.route("/add-data", methods=["POST"])
def add_task():
  if not request.json:
    return jsonify({
      "status":"error",
      "message": "Please provide the data!"
    }, 400)
    
  contact = {
    'id': tasks[-1]['id'] + 1,
    'Name': request.json['Name'],
    'Contact': request.json.get('Contact', ""),
    'done': False
  }
  tasks.append(task)
  
  return jsonify({
    "status":"success",
    "message": "Task added successfully!"
  })

@app.route("/get_data")

def get_task():
  return jsonify({
    "data" : tasks
  })

if (__name__ == "__main__"):
  app.run(debug=True)