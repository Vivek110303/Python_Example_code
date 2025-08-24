#IMPORTING
from flask import Flask ,render_template, request


#INTERACTION
app = Flask(__name__)

#MAPPING
@app.route('/')
@app.route('/register')

#INPUTS
def homepage():
    return render_template('register.html')


@app.route('/confirmation' ,methods=['GET','POST'])
def register():
    if request.method == 'POST':
        n = request.form.get('name')
        c = request.form.get('city')
        p = request.form.get('phone no')
        return render_template('confirm.html',name=n,city=c,phone_no=p)



#MAIN
if __name__ == '__main__':
    app.run(debug=True)

