from flask import Flask, render_template, request, redirect, session
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Configure Flask-Session to use server-side sessions
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# A variable to track whether the user is authenticated as an admin
users = {
    "admin": "adminpassword",
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
}

# Initial content (for demonstration)
content = {
    # ... (your content data)
    "notification_title_1": "New Admission Schedule for 2023-24",
    "notification_date_1": "October 15, 2023",
    "notification_content_1": "Stay updated with the latest admission schedule for the academic year 2023-24.",
    "pdf_url_1": "https://example.com/pdf1.pdf",
    "notification_title_2": "Another Notification Title",
    "notification_date_2": "October 20, 2023",
    "notification_content_2": "This is another sample notification content.",
    "pdf_url_2": "https://example.com/pdf2.pdf",
    "notification_title_3": "Yet Another Notification",
    "notification_date_3": "October 25, 2023",
    "notification_content_3": "This is a third sample notification content.",
    "pdf_url_3": "https://example.com/pdf3.pdf",
    "notification_title_4": "Previous Notification 1",
    "notification_date_4": "September 30, 2023",
    "notification_content_4": "View the results of the recent semester-end examinations.",
    "pdf_url_4": "https://example.com/pdf4.pdf",
    "notification_title_5": "Previous Notification 2",
    "notification_date_5": "September 25, 2023",
    "notification_content_5": "This is another previous notification content.",
    "pdf_url_5": "https://example.com/pdf5.pdf",
}

@app.route('/')
def index():
    return render_template('index.html', **content)

@app.route('/admin')
def admin():
    if not session.get('is_authenticated'):
        return redirect('/admin/login')
    return render_template('admin.html', content=content)

@app.route('/admin/login')
def admin_login():
    if not session.get('is_authenticated'):
        return render_template('admin_login.html')
    return redirect('/admin')

@app.route('/admin/login', methods=['POST'])
def check_admin_login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['is_authenticated'] = True
        return redirect('/admin')

    error_message = "Invalid username or password. Please try again."
    return render_template('admin_login.html', error=error_message)

@app.route('/update', methods=['POST'])
def update_content():
    if not session.get('is_authenticated'):
        return redirect('/admin/login')
    if 'admin' in request.form:
        # Update the content as needed
        content['notification_title_1'] = request.form['notification_title']
        content['notification_date_1'] = request.form['notification_date']
        content['notification_content_1'] = request.form['notification_content']
        content['pdf_url_1'] = request.form['pdf_url']
        content['notification_title_2'] = request.form['notification_title_2']
        content['notification_date_2'] = request.form['notification_date_2']
        content['notification_content_2'] = request.form['notification_content_2']
        content['pdf_url_2'] = request.form['pdf_url_2']
        content['notification_title_3'] = request.form['notification_title_3']
        content['notification_date_3'] = request.form['notification_date_3']
        content['notification_content_3'] = request.form['notification_content_3']
        content['pdf_url_3'] = request.form['pdf_url_3']
        content['notification_title_4'] = request.form['notification_title_4']
        content['notification_date_4'] = request.form['notification_date_4']
        content['notification_content_4'] = request.form['notification_content_4']
        content['pdf_url_4'] = request.form['pdf_url_4']
        content['notification_title_5'] = request.form['notification_title_5']
        content['notification_date_5'] = request.form['notification_date_5']
        content['notification_content_5'] = request.form['notification_content_5']
        content['pdf_url_5'] = request.form['pdf_url_5']

    return redirect('/admin')

if __name__ == '__main__':
    app.run(debug=True)
