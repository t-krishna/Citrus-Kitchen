# Full site!

import sys
anaconda_path = ['C:\\Users\\Syris Norelli\\Anaconda3\\python35.zip', 'C:\\Users\\Syris Norelli\\Anaconda3\\DLLs', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib', 'C:\\Users\\Syris Norelli\\Anaconda3', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib\\site-packages', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib\\site-packages\\Sphinx-1.4.6-py3.5.egg', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib\\site-packages\\win32', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib\\site-packages\\win32\\lib', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib\\site-packages\\Pythonwin', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib\\site-packages\\setuptools-27.2.0-py3.5.egg', 'C:\\Users\\Syris Norelli\\Anaconda3\\lib\\site-packages\\IPython\\extensions', 'C:\\Users\\Syris Norelli\\.ipython']
for loc in anaconda_path:
    sys.path.append(loc)

from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/restaurant')
def restaurant():
    return render_template('restaurant.html')

@app.route('/restaurant',methods=['POST'])
def restaurant_post():
    name = request.form['restaurantname']
    foodname = request.form['foodname']
    fooddesc = request.form['fooddesc']
    expdate = request.form['expdate']
    quantity = request.form['quant']
    f.write("{}\t{}\t{}\t{}\t{}\n".format(name, foodname, fooddes, expdate, quantity))
    f.flush()
    f.close()
    return "<h1> IT WORKED! THE NUKES HAVE BEEN LAUNCHED </h1>"

@app.route('/shelter')
def shelter(dataset=[1,2,3,4,6,3,6]):
    with open("db.txt","r") as f:
        dataset = f.readlines()
        dataset = [' '.join(x.strip('\n').split(r'/t')) for x in dataset]
    return render_template('shelter.html', dataset=str(dataset))

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/restaurantsec')
def restaurantsec():
    return render_template('restaurantsec.html')

@app.route('/test')
def test():
    arbitrary_var = [1,6,2,7,3,0,9,2]
    return str(arbitrary_var)

if __name__ == '__main__':
    f = open("db.txt", 'w')
    f.write("Name\tFood\tDescription\tExpiration\Quantity\n")
    # Generate file
    names = ['costco','stater bros','trader joe\'s']
    food = ['bananas','apples','wheat bread']
    descript = ['fruit','fruit','grain']
    expiration = ['1 week','3 days','1 weeks']
    quantity = ['1','6','8']
    for i,x in enumerate(names):
        f.write("{}\t{}\t{}\t{}\t{}\n".format(names[i], food[i], descript[i], expiration[i], quantity[i]))
    f.close()
    app.run()
