from flask import Flask, render_template, url_for, request, redirect # Flask is a class
import csv

app = Flask(__name__) #instansiate an app
# print(__name__) # or __name__ is __main__

@app.route("/")
def my_home():
    return render_template("index (2).html")

# @app.route("/index (2).html")
# def index():
#     return render_template("index (2).html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

# @app.route("/works.html")
# def works():
#     return render_template("works.html")
#
# @app.route("/about (2).html")
# def about():
#     return render_template("about (2).html")
#
# @app.route("/contact.html")
# def contact():
#     return render_template("contact.html")
#
# @app.route("/work.html")
# def work():
#     return render_template("work.html")
#
# @app.route("/components.html")
# def components():
#     return render_template("components.html")

# @app.route("/blog/2020/dogs")
# def blog2():
#     return "this is a dog blog 2020"
#
# @app.route("/<username>/<int:post_id>")
# def hello_world(username=None, post_id=None):
#     # app.add_url_rule('/favicon.ico',redirect_to=url_for('static', filename='favicon.ico'))
#     return render_template("index.html", name=username, post_id=post_id)
#
# @app.route("/about.html")
# def about():
#     return render_template("about.html")

# @app.route("/favicon.ico")
# def favicon():
#     return render_template("about.html")

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', lineterminator = "\n" , quotechar='"', quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'
    else:
        return 'try again'