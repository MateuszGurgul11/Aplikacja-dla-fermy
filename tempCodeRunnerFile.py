from flask import Flask, render_template, request, send_file
from datetime import datetime, timedelta
import functions
import pdfkit
from io import BytesIO

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

@app.route("/download_pdf", methods=['POST'])
def download_pdf():
    breader = request.form['breader']
    date = request.form['date']
    target_date = request.form['target_date']
    amount = request.form['amount']
    downed_amount = request.form['downed_amount']
    downed = request.form['downed']
    percent = request.form['percent']
    feed = request.form['feed']
    feed_waste = request.form['feed_waste']

    html_content = render_template("summary_table.html", breader=breader, date=date, target_date=target_date, amount=amount, downed_amount=downed_amount, downed=downed, percent=percent, feed=feed, feed_waste=feed_waste)
    
    # Utworzenie pliku PDF z HTML
    pdf = pdfkit.from_string(html_content, False)

    # Przesłanie pliku PDF do klienta
    pdf_io = BytesIO(pdf)
    pdf_io.seek(0)

    return send_file(pdf_io, attachment_filename='summary.pdf', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)