
from flask import Flask, render_template
app = Flask(__name__)
app.debug=True

def get_list():
    n=[x for x in range(999999)]
    print "X"
    return n

@app.route("/include")
def include():
    return render_template('hello2.html', list=get_list())


@app.route("/macro")
def macro():
    return render_template('hello.html', list=get_list())

app.run(port=1200)

