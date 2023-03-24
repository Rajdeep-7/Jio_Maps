from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle button click event
    if request.form['action'] == 'button1':
        print('Button 1 clicked')
    elif request.form['action'] == 'button2':
        print('Button 2 clicked')
    else:
        print('Unknown button clicked')

    # Redirect back to the homepage
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=5001)
