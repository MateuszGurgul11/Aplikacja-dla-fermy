from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def calculation(amount, percent):
    downed = amount * (percent / 100)
    amount_pass = amount - downed
    return amount_pass

def feed_amount(amount_pass, feed):
    feed_waste = feed / amount_pass
    return feed_waste

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        amount = int(request.form['amount'])
        percent = float(request.form['percent'])
        feed = float(request.form['feed'])
        amount_pass = calculation(amount, percent)
        feed_waste = feed_amount(amount_pass, feed)
        feed_waste = round(feed_waste, 2)
        if 'date' in request.form:
            selected_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
            target_date = selected_date + timedelta(days=84)
            return render_template("index.html", amount_pass=amount_pass, feed_waste=feed_waste, target_date=target_date.strftime('%Y-%m-%d'))
        else:
            return render_template("index.html", amount_pass=amount_pass, feed_waste=feed_waste)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
