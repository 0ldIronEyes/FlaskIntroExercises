from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


def add(a, b):
    """Add a and b."""
    
    return a + b

def sub(a, b):
    """Substract b from a."""
    return a - b

def mult(a, b):
    """Multiply a and b."""
    return a * b

def div(a, b):
    """Divide a by b."""
    return a / b


operations = {
    
    "add"  : add,
    "sub"  : sub,
    "mult" : mult,
    "div"  : div
}


@app.route("/add")
def add_function():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))


@app.route("/sub")
def add_function():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a + b))



@app.route("/mult")
def add_function():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a + b))


@app.route("/div")
def add_function():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a + b))


@app.route("/math/<oper>")
def operation(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(operations[oper](a, b))
