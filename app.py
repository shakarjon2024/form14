from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/form14', methods=['GET', 'POST'])
def form14():
    if request.method == 'POST':
        ism = request.form.get('ism')
        email = request.form.get('email')
        return f"<h2>Majburiy maydonlar to‘ldirildi!</h2><p>Ism: {ism}<br>Email: {email}</p><br><a href='/'>Orqaga</a>"
    return render_template('form14.html')

if __name__ == '__main__':
    app.run(debug=True)
