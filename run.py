'''
Created on Oct 28, 2014

@author: Swapna Bhi
'''
from flask import Flask
import twilio.twiml
import json
import urllib, json
import time
from time import sleep

 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    
    try:
        child = req_json()
    except:
        sleep(31)
        child = req_json()
    
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hi! My name is Swapna Bhide. And current headline on reddit is " + child)
 
    return str(resp)

def req_json():
    url = "http://api.reddit.com/"
    response = urllib.request.urlopen(url)
    data1 = response.read()
    data = json.loads(data1.decode())
    ch=data["data"]
    child = ch["children"][0]["data"]["title"]
    return child
 
if __name__ == "__main__":
    app.run(debug=True)