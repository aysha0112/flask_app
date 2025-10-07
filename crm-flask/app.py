from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory "database"
customers = []

@app.route("/")
def home():
    return render_template("index.html", customers=customers)

@app.route("/add", methods=["POST"])
def add_customer():
    name = request.form.get("name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    customers.append({"name": name, "email": email, "phone": phone})
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
