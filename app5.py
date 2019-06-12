#import required libraries
from flask import Flask,render_template
app4=Flask(__name__,static_url_path='/static')

#Default home page method
@app5.route('/')
def index():
	return render_template('image.html',name="home")

#Display image based on input
@app5.route('/<input>')
def display(input):
	valid_inputs =['apple','ball','cat','dog']

	if input in valid_inputs:
		return render_template('image.html',name=input)
	else:
		return "<html><body><b>ERROR</b></body></html>"


if __name__=="__main__":
		app5.run()	
