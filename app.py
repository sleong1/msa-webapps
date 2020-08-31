from app import app

## Code for logging in
# @app.route('/login',  methods=["GET", "POST"])
# def login():
#     """The view for the login page"""
#     try:
#         error = ''
#         if request.method == "POST":
#             attempted_username = request.form['username']
#             attempted_password = request.form['password']
#             if attempted_username == 'admin' and attempted_password == os.environ['USER_PASSWORD']:
#                 session['logged_in'] = True
#                 session['username'] = request.form['username']
#                 return redirect(url_for('edit_database', city_id=city_id))
#             else:
#                 print('invalid credentials')
#                 error = 'Invalid credentials. Please, try again.'
#         return render_template('login.html', error=error, city_name=city_record.city_name, city_id=city_id)
#     except Exception as e:
#         return render_template('login.html', error=str(e), city_name=city_record.city_name, city_id=city_id)


# def login_required(f):
#     @wraps(f)
#     def wrap(*args, **kwargs):
#         """login session"""
#         if 'logged_in' in session:
#             return f(*args, **kwargs)
#         else:
#             pass
#         return redirect(url_for('login'))
#     return wrap