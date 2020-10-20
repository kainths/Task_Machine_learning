from flask import Flask, render_template


app = Flask(__name__, template_folder='template')  # still relative to module
@app.route('/')
def index():
   return render_template('hello.html')

if __name__ == '__main__':
   app.run(debug = True)

