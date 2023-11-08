from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)
def isSafe(cmd):
    blacklist = [" "]
    for i in blacklist:
        if i in cmd:
            return False
    return True
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    image = None
    if request.method == 'POST':
      if isSafe(request.form.get('command')):
        command = "ping "+request.form.get('command')
        result = subprocess.getoutput(command)
      else:
        image = "no.png"
        result = "...."
    return render_template('command.html', result=result,image=image)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
