from flask import Flask, render_template, request
from datetime import datetime, timedelta

app = Flask(__name__)

def calculation_percent(amount, downed):
    percent = (downed / amount) * 100
    return percent

def calculation_amount(amount, downed):
    downed_amount = amount - downed
    return downed_amount

def feed_amount(percent, feed):
    feed_waste = feed / percent
    return feed_waste

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        amount = int(request.form['amount'])
        downed = int(request.form['downed'])
        feed = float(request.form['feed'])
        downed_amount = calculation_amount(amount, downed)
        percent = calculation_percent(amount, downed)
        feed_waste = feed_amount(percent, feed)
        feed_waste = round(feed_waste, 2)
        if 'date' in request.form:
            selected_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
            target_date = selected_date + timedelta(days=84)
            return render_template("index.html", downed_amount=downed_amount, percent=percent, feed_waste=feed_waste, target_date=target_date.strftime('%Y-%m-%d'))
        else:
            return render_template("index.html", downed_amount=downed_amount, percent=percent, feed_waste=feed_waste)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
