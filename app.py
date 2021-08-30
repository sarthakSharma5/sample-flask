from flask import Flask
import platform
from subprocess import getstatusoutput

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"
  
@app.route("/sys")
def get_system_info():
  try:
    return {"machine": platform.machine(), "version": platform.version(), "platform": platform.platform(), "system": platform.system(), "processor": platform.processor(),}
  except:
    return "Unable to provide system info"

@app.route("/ip")
def get_ifconfig():
  output = None
  try:
    status, output = getstatusoutput("ifconfig")
  except:
    output = "Unable to process"
  return "<PRE>{}</PRE>".format(output)

if __name__ == "__main__":
  app.run(port=5000)
