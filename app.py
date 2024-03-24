from flask import Flask, render_template, request
from datetime import datetime, timedelta
import functions

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        breader = str(request.form['breader'])
        amount = int(request.form['amount'])
        downed = int(request.form['downed'])
        feed = float(request.form['feed'])
        date = request.form['date'] 

        downed_amount = functions.calculation_amount(amount, downed)
        percent = functions.calculation_percent(amount, downed)
        feed_waste = functions.feed_amount(feed, downed_amount)

        if 'date' in request.form:
            selected_date = datetime.strptime(date, '%Y-%m-%d')
            target_date = selected_date + timedelta(days=84)
            return render_template("index.html", downed_amount=downed_amount, percent=percent, feed_waste=feed_waste, target_date=target_date.strftime('%Y-%m-%d'), amount=amount, feed=feed, downed=downed, breader=breader, date=date)
        else:
            return render_template("index.html", downed_amount=downed_amount, percent=percent, feed_waste=feed_waste)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)