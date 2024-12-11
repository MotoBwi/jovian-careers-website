from flask import Flask, render_template, jsonify

app = Flask(__name__)


@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                          company_name="Bapan's")
  

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)