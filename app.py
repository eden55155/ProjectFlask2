from flask import Flask, request, render_template

   app = Flask(__name__)

   @app.route('/', methods=['GET', 'POST'])
   def hello():
       if request.method == 'POST':
           username = request.form['username']
           return f'Hello, {username}!'
       return render_template('form.html')

   if __name__ == '__main__':
       app.run(host='0.0.0.0', port=8080)
