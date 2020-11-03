from flask import Flask 
app = Flask(__name__) 

@app.route('/') 
def hello(): 
	return "welcome to the Jenkins with Devsecops  !!"

@app.route('/oracle') 
def hello1():
	return "Welcome to ORacle Containerization process with deployment using shell script !!"


if __name__ == "__main__": 
	app.run(host ='0.0.0.0', port = 5000, debug = True) 
