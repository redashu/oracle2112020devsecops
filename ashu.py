from flask import Flask 
app = Flask(__name__) 

@app.route('/') 
def hello(): 
	return "welcome to the Oracle web app with python in DevSecOPs this is change new  !!"

@app.route('/oracle') 
def hello1():
	return "Welcome to ORacle Containerization process with deployment using shell script !!"


if __name__ == "__main__": 
	app.run(host ='0.0.0.0', port = 5000, debug = True) 
