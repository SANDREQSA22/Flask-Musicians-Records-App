from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import os
from init_db import init_db
from init2_db import init2_db



app = Flask(__name__)
app.secret_key = 'supersecretkey'
DATABASE = 'database.db'
DATABASE2 = 'database2.db'



class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password



    def register(self):
        try:
            conn = sqlite3.connect(DATABASE)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (self.username, self.password))
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False



    def login(self):
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT password FROM users WHERE username = ?', (self.username,))
        record = cursor.fetchone()
        conn.close()
        if record and record[0] == self.password:
            return True
        return False



@app.route('/')
def home():
    if 'username' in session:
        return render_template('index.html')
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        if user.login():
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username, password)
        if user.register():
            flash('Registration successful! You can now login.')
            return redirect(url_for('login'))
        else:
            flash('Username already exists.')
    return render_template('register.html')



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))



@app.route('/addrec', methods=['GET', 'POST'])
def addrec():
    if request.method == 'POST':
        conn = sqlite3.connect(DATABASE2)
        cursor = conn.cursor()
        musician_name = request.form['musician_name']
        guitar_name = request.form['guitar_name']
        song_title = request.form['song_title']
        image_url = request.form['image_url']
        cursor.execute('INSERT INTO records (musician_name, guitar_name, song_title, image_url) VALUES (?, ?, ?, ?)', 
                       (musician_name, guitar_name, song_title, image_url))
        conn.commit()
        conn.close()
        flash('Record was successfully added')
        return redirect(url_for('listrec'))
    return render_template('addrec.html')




@app.route('/listrec')
def listrec():
    conn = sqlite3.connect(DATABASE2)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM records')
    records = cursor.fetchall()
    conn.close()
    return render_template('listrec.html', records=records)


@app.route('/editrec/<int:id>', methods=['GET', 'POST'])
def editrec(id):
    conn = sqlite3.connect(DATABASE2)
    cursor = conn.cursor()
    if request.method == 'POST':
        musician_name = request.form['musician_name']
        guitar_name = request.form['guitar_name']
        song_title = request.form['song_title']
        image_url = request.form['image_url']
        cursor.execute('UPDATE records SET musician_name = ?, guitar_name = ?, song_title = ?, image_url = ? WHERE id = ?', 
                       (musician_name, guitar_name, song_title, image_url, id))
        conn.commit()
        conn.close()
        flash('Record was successfully updated')
        return redirect(url_for('listrec'))
    else:
        cursor.execute('SELECT * FROM records WHERE id = ?', (id,))
        record = cursor.fetchone()
        conn.close()
        return render_template('editrec.html', record=record)

@app.route('/deleterec/<int:id>', methods=['GET'])
def deleterec(id):
    conn = sqlite3.connect(DATABASE2)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM records WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Record was successfully deleted')
    return redirect(url_for('listrec'))


if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        init_db()
    if not os.path.exists(DATABASE2):
        init2_db()
    app.run(debug=True)

















