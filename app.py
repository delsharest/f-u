from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ganti dengan kunci rahasia yang lebih kuat

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/question1', methods=['GET', 'POST'])
def question1():
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == "Iyaa, gw di siniii":  # Memperbarui untuk mencocokkan nilai baru
            return render_template('question2.html')  # Arahkan ke pertanyaan kedua
        else:
            flash('Kenapa jawab ngga? Berarti bukan Yas, ya?')  # Menyimpan pesan
            return redirect(url_for('home'))  # Kembali ke home
    return render_template('question1.html')

@app.route('/question2', methods=['GET', 'POST'])
def question2():
    if request.method == 'POST':
        destination = request.form.get('destination')
        if destination == 'Bandung, kuliah nih sibuk':
            return render_template('bandung_reminders.html', show_popup=True)
        elif destination == 'Sukabumi, libur cuyyy':
            return render_template('sukabumi_reminders.html', show_popup=True)
    return render_template('question2.html')

@app.route('/final_message', methods=['GET', 'POST'])
def final_message():
    answer1 = request.args.get('answer1')
    answer2 = request.args.get('answer2')
    return render_template('final_message.html', answer1=answer1, answer2=answer2)

if __name__ == '__main__':
    app.run(debug=True)