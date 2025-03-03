from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia yang lebih kuat

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question1', methods=['POST'])
def question1():
    answer = request.form.get('answer')
    if answer == "Iyaa, gw di siniii":
        return redirect(url_for('question2'))  # Arahkan ke pertanyaan kedua
    else:
        flash('Kenapa jawab ngga? Berarti bukan Yas, ya?')
        return redirect(url_for('home'))  # Kembali ke home

@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        destination = request.form.get('destination')
        if destination == 'Bandung, kuliah nih sibuk':
            return redirect(url_for('bandung_reminders'))
        elif destination == 'Sukabumi, libur cuyyy':
            return redirect(url_for('sukabumi_reminders'))
    return render_template('question2.html')

@app.route('/bandung_reminders')
def bandung_reminders():
    return render_template('bandung_reminders.html', show_popup=True)

@app.route('/sukabumi_reminders')
def sukabumi_reminders():
    return render_template('sukabumi_reminders.html', show_popup=True)

@app.route('/final_message')
def final_message():
    answer1 = request.args.get('answer1', 'Tidak diketahui')
    answer2 = request.args.get('answer2', 'Tidak diketahui')
    return render_template('final_message.html', answer1=answer1, answer2=answer2)

if __name__ == '__main__':
    app.run(debug=True)
