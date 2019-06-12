from flask import Flask,render_template 

app1=Flask(__name__)

@app1.route('/')
@app1.route('/geetha')
def geetha():
	employee={'username':'geetha'}
	return render_template('index1.html',user=employee)

@app1.route('/siddarth')
def siddarth():
	employee={'username':'siddarth'}
	return render_template('index1.html',user=employee)


if __name__=="__main__":
	app1.run()