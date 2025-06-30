from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Route for the Joining Form (index.html)
@app.route('/', methods=['GET', 'POST'])
def joining_form():
    if request.method == 'POST':
        # Process and save form data here if needed
        return redirect(url_for('nomination_form'))
    return render_template('index.html')


# Route for the Nomination Form
@app.route('/nomination', methods=['GET', 'POST'])
def nomination_form():
    if request.method == 'POST':
        # Process and save nomination form data here if needed
        return "Nomination Form Submitted!"  # You can redirect to a confirmation page instead
    return render_template('nomination_form.html')


if __name__ == '__main__':
    app.run(debug=True)

