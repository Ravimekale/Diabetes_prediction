from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def submit():
    a = request.form['a']
    b = request.form['b']
    c = request.form['c']
    d = request.form['d']
    input_data = [[float(a),float(b),float(c),float(d)]]


    model=pickle.load(open(r"C:\Users\LENOVO\Desktop\App\LR.pkl","rb"))
    
    target=['setosa', 'versicolor', 'virginica']
    
    result=model.predict(input_data)
    
    return target[result[0]]


if __name__ == '__main__':
    app.run(debug=True)