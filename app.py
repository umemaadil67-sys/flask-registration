from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/register',methods=['GET','POST'])
def register():
  if request.method == 'POST':
    name = request.from['name']
    email = request.from['email']
    password = request.from['password']
    # Store the user data in a database or file 
    return render_template('success.html')
    return render_template('register.html')
    if __name__=='__main__':
      app.run(host='0.0.0.0')
