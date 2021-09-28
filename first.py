import main
from flask import Flask, request


app = Flask(__name__)
@app.route('/v1/sanitized/input/',methods=['POST'])
def v1():
    
    data = request.get_json()  
    name = data['name']
    result = main.check(name)  
    return result
 
if __name__=="__main__": 
    app.run(port = 8000)


