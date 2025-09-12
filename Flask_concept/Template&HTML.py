from flask import Flask , render_template

app = Flask(__name__, template_folder = 'html')

@app.route('/')
def index(): 
  myValue = 'NurealNine'
  myresult = 10 + 20
  return render_template('index.html', m=myValue , M=myresult)






if __name__ == '__main__':
  app.run(host = '0.0.0.0' , debug = True, port = 5555)