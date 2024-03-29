from flask import Flask, render_template, request, send_from_directory
from datetime import datetime, timedelta
import functions
import os

app = Flask(__name__)

@app.route("/download_summary")
def download_summary():
    directory = os.getcwd()
    filename = "summary.csv"

    return send_from_directory(directory, filename , as_attachment=True)

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

            summary_data = {
            "Hodowca" : breader,
            "Data Wstawienia" : selected_date,
            "Termin uboju kogutów" : target_date,
            "Ilość sztuk wstawionych" : amount,
            "Ilość sztuk do zdania" : downed_amount,
            "Ilość upadków" : downed,
            "Śmiertelność" : percent,
            "Ilość zużytej paszy" : feed,
            "Ilość paszy na sztukę" : feed_waste
            }

            file_path = 'summary.csv'
            functions.save_summary_to_csv(summary_data, file_path)
            
            return render_template("index.html", downed_amount=downed_amount, percent=percent, feed_waste=feed_waste, target_date=target_date.strftime('%Y-%m-%d'), amount=amount, feed=feed, downed=downed, breader=breader, date=date)
        else:
            return render_template("index.html", downed_amount=downed_amount, percent=percent, feed_waste=feed_waste)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)