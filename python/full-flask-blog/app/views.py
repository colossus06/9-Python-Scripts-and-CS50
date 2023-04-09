from crypt import methods
from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")
    # now we'll be displaying our main page to the user when she hits the root /


my_name= "robin dawn"
age="32"
langs=['python', 'javascript', 'node', 'ruby']

friends={
    'Tom': 30,
    'Helen': 45,
    'Dennis': 12
}

colours=('red', 'green')

cool=True

def repeat(x, qty):
    return x*qty

class GitRemote:
    def __init__(self, name, description, url) -> None:
        self.name=name
        self.description=description
        self.url=url   



    def pull(self):
        return f"Pulling repo {self.name}"
    def clone(self):
        return f"Cloning into {self.url}"


my_remote=GitRemote(
    name="Flask Jinja App",
    description="Template tutorial",
    url= ""
)


@app.route("/jinja")
def jinja():
    return render_template("public/jinja.html", my_name=my_name, age=age, friends=friends, cool=cool, repeat=repeat, GitRemote=GitRemote, colours=colours, langs=langs,
    my_remote=my_remote
    )


@app.route("/about")
def about():
    return "<h1 style='color: red'> go girls</h1>"

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("public/sign_up.html")