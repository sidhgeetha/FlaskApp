from flask import Flask,render_template
from app import app

@template_app.route('/')
@template_app.route('/index')
def index():
	user={'username':'geetha'}
	posts=[
	{
	'author':{'username':'sid'}
	'body':'have a nice day'
	},
	{
	'author':{'username':'kannan'}
	'body':'welcome'
	}
]
return render_template('loops.html',user=user,posts=posts)

if __name__== '__main__':
	template_app.run()	
	