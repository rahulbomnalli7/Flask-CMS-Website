from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name)
app.secret_key = '54c85b795c7e5ec891b70983cfb04f8f'
login_manager = LoginManager()
login_manager.init_app(app)

# A variable to track whether the user is authenticated as an admin
is_authenticated = False


users = [
    {"username": "admin", "password": "adminpassword"},
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"},
    {"username": "user4", "password": "password4"},
    {"username": "user5", "password": "password5"},
]

# Initial content (for demonstration)
content = {
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

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html', content=content)

@app.route('/admin/login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin/login', methods=['POST'])
def check_admin_login():
    global is_authenticated  # Declare the variable as global
    username = request.form['username']
    password = request.form['password']

    for user in users:
        if user['username'] == username and user['password'] == password:
            user_obj = User(username)
            login_user(user_obj)
            is_authenticated = True  # Set the authenticated flag
            return redirect('/admin')
        
    error_message = "Invalid username or password. Please try again."
    return render_template('admin_login.html', error=error_message)

@app.route('/admin/logout')
@login_required
def admin_logout():
    is_authenticated = False
    logout_user()
    return redirect(url_for('admin_login'))

@app.route('/update', methods=['POST'])
def update_content():
    if 'admin' in request.form:
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
