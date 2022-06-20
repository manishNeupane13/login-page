from flask import Flask, render_template, request,make_response

app = Flask(__name__)


@app.route('/')
def student():
    return render_template('student.html')


@app.route('/score/<int:score>')
def score(score):
    return render_template("score.html", marks=score)


@app.route('/result1', methods=['POST', 'GET'])
def result1():
    if request.method == 'POST':
        result = request.form
        print(result)
    return render_template("result1.html", result=result)


@app.route('/result')
def result():
    dict = {'phy': 50, 'che': 60, 'maths': 70}
    return render_template('result.html', result=dict)

@app.route('/setcookie',methods=['POST','GET'])

def setcookie():
    if request.method =='POST':
        user=request.form['nm']
    resp=make_response(render_template('readcookie.html'))
    resp.set_cookie('userID',user)
    return resp


@app.route('/index')
def index():
   return render_template('index.html')
@app.route('/getcookie')
def getcookie():
    name=request.cookies.get('userID')
    return '<h1>welcome '+name +'</h1>'

if __name__ == "__main__":
    app.run(debug=True)
