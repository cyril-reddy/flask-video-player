from flask import Flask,render_template
import requests
import json
#from waitress import serve


app = Flask(__name__)

@app.route('/')
def start():
    
    result=requests.get('http://jsonplaceholder.typicode.com/posts')
    return render_template('index.html',results=result.json())


@app.route('/video')
def vid():
    return render_template('video.html')

@app.route('/video/backgroundplugin')
def plugin():
     return render_template('plugin.html')

if __name__ == "__main__":
   app.run(debug=True)
    
