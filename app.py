from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///formdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the model (table structure) - sample with only a few fields
class UserForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    middle_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    mobile_number = db.Column(db.String(20))
    dob = db.Column(db.String(20))
    address = db.Column(db.Text)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Collect only a few fields as a demonstration
        new_entry = UserForm(
            first_name=request.form.get("firstName"),
            middle_name=request.form.get("middleName"),
            last_name=request.form.get("lastName"),
            email=request.form.get("email"),
            mobile_number=request.form.get("mobileNumber"),
            dob=request.form.get("dob"),
            address=request.form.get("presentAddress")
        )
        db.session.add(new_entry)
        db.session.commit()
        return redirect("/")
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

