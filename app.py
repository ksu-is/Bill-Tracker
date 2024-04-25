from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

bills = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        bill_name = request.form['name']
        amount_due = request.form['amount']
        payment_date = request.form['date']
        payment_amount = request.form['payment']
        bills.append({'name': bill_name, 'amount': amount_due, 'date': payment_date, 'payment': payment_amount})
        return redirect(url_for('home'))
    return render_template('index.html', bills=bills)

if __name__ == "__main__":
    app.run(debug=True)
