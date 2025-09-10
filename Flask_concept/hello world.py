from flask import Flask, request 
app = Flask(__name__)  # applications created

@app.route('/')                   # decorator
def Hello_world():                  # function
    return "<h1>Hello World!!🎈</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}"

@app.route('/add/<int:n1>/<int:n2>')
def add(n1, n2):
    return f" {n1} + {n2}  = {n1 + n2}"

"""
# Now we are creating the handle_url_params 
@app.route('/url_params')
def handle_url_params():
    return str(request.args) # like this it create  a immutable dict ([]) 
"""

@app.route('/url_params')
def handle_url_params():
  if 'greeting' in request.args.keys() and 'name' in request.args.keys():
    greeting =  request.args['greeting']
    name = request.args.get('name')
    return f'{greeting} , {name}'
  else:
    return 'some parameters are missing'


# X Post method
@app.route('/hello',methods =['POST'])                   
def Hello_world2():                  
    return "<h1>Hello World!!🎈</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)           # run the application
