from flask import Flask,render_template
app6=Flask(__name__,static_url_path='/static')

app6=route('/')

app6=route('/<input>')
def display(input):
	input_values=['a','b','c']
	if input in input_values:
		return render_template('index2.html',name=input)
	else:
		return "<html><body><b> error</b></body></html"


if(__name__)=="__main__":
		app6.run()		




