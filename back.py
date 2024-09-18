from flask import Flask, render_template, request

app = Flask(__name__, template_folder='web/templates')


@app.route('/')
def get_html():
    return render_template('index.html')


@app.route('/button_clicked', methods=['POST'])
def button_cliked():
    return "<h1>Button was clicked!</h1>"


if __name__ == '__main__':
    app.run(debug=True) # runs this in debug mode 
    
    
