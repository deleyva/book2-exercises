from flask import Flask

app =  Flask(__name__)

#error handling
# it will add live reload
app.config["DEBUG"] = True

# use the decorator pattern to link the view function to a url
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return "correct"

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return "correct"

@app.route("/name/<name>")
def index(name):
    if name.lower() == "michael":
        return f"Hello, {name}", 200
    else:
        return "Not Found", 404

if __name__ == "__main__":
    app.run()