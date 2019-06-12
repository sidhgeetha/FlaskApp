from flask import Flask,render_template
app3=Flask(__name__,static_url_path='/static')

@app3.route('/')
@app3.route('/apple')
def apple():
	return render_template('image.html',name='apple')

@app3.route('/boll')
def boll():
	return render_template('image.html',name='boll')

@app3.route('/cat')	
def cat():
	return render_template('image.html',name='cat')

if __name__=="__main__":
		app3.run()	



