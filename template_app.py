from flask import Flask,render_template
from app import app

obj = Flask(__name__)

@obj.route('/')
@obj.route('/index')
def index():
	user={'username':'geetha'}
	posts=[
	{
	'author':{'username':'sid'},
	'body':'have a nice day'
	},
	{
	'author':{'username':'kannan'},
	'body':'welcome'
	}
]

	return render_template('index.html',user=user,posts=posts)

if __name__== '__main__':
	obj.run()	


