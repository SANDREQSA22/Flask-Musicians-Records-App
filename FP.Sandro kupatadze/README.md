
## Flask Musicians Records App

This is a simple web application built using Flask, SQLite, and HTML/CSS. It allows users to register, log in, and manage a list of musicians, their guitars, and their songs.

### Features

- User registration and login
- Add, view, update, and delete records of musicians, their guitars, and their songs
- Simple and clean design with navigation bar

### Requirements

- Python 3.x
- Flask
- SQLite

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd flask-musicians-app
   ```

2. **Install dependencies:**
   ```bash
   pip install flask
   ```

3. **Initialize the databases:**
   Run the following commands to create the necessary databases:
   ```bash
   python init_db.py
   python init2_db.py
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

   The application will be available at [http://127.0.0.1:5000](http://127.0.0.1:5000).

### Usage

- **Register a New User:**
  - Go to the registration page: [http://127.0.0.1:5000/register](http://127.0.0.1:5000/register)
  - Enter a username and password, then click "Register"

- **Log In:**
  - Go to the login page: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)
  - Enter your username and password, then click "Login"

- **Add a New Record:**
  - After logging in, go to [http://127.0.0.1:5000/addrec](http://127.0.0.1:5000/addrec)
  - Fill in the musician's name, guitar name, and song title, then click "Submit"

- **View Records:**
  - Go to [http://127.0.0.1:5000/listrec](http://127.0.0.1:5000/listrec)
  - You will see a list of all records

- **Update or Delete Records:**
  - On the list page ([http://127.0.0.1:5000/listrec](http://127.0.0.1:5000/listrec)), you can click "Edit" or "Delete" next to each record to update or remove it.