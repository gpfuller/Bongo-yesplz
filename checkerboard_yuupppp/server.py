from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def check_1():
    return render_template('index.html', num_1 = 8, num_2 = 8, color_1 = 'blue', color_2 = 'red')

@app.route('/<int:num_2>')
def check_2 (num_2):
    return render_template('index.html', num_1 = 8, num_2 = num_2, color_1 = 'blue', color_2 = 'red')

@app.route('/<int:num_1>/<int:num_2>')
def check_3 (num_1, num_2):
    return render_template('index.html', num_1 = num_1, num_2 = num_2, color_1 = 'blue', color_2 = 'red')

@app.route('/<int:num_1>/<int:num_2>/<color_1>/<color_2>')
def check_4 (num_1, num_2, color_1, color_2):
    return render_template('index.html', num_1 = num_1, num_2 = num_2, color_1 = color_1, color_2 = color_2)

if __name__=="__main__":
    app.run(debug=True)