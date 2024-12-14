from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Diminombre1*'
app.config['MYSQL_DB'] = 'invitados'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM invitados")
    data = cur.fetchall()
    cur.close()
    return render_template("index.html", invitados=data)

@app.route('/enviar', methods=['GET', 'POST'])
def enviar():
    if request.method == 'POST':
        nombre = request.form.get('nombre', '')
        opcion = request.form.get('opcion', '')
        opcion2 = request.form.get('opcion2', '')
        opcion3 = request.form.get('opcion3', '')
        opcion4 = request.form.get('opcion4', '')
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO invitados (nombre, opcion, opcion2, opcion3, opcion4) VALUES (%s, %s, %s, %s, %s)", (nombre, opcion, opcion2, opcion3, opcion4))
        mysql.connection.commit()
        cur.close()
        
        return redirect(url_for('enviar'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
