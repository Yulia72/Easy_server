from flask import Flask, render_template, request

app = Flask(__name__)

# --- ГОЛОВНА ---
@app.route('/')
def index():
    return render_template('index.html')

# --- ПЕРСОНАЛІЗОВАНА ГОЛОВНА ---
@app.route('/user/<name>')
def user_index(name):
    return render_template('index.html', user_name=name)

# --- СТАТТІ ---
@app.route('/articles')
def articles():
    new_articles = [
        'How to avoid expensive travel mistakes',
        'Top 5 places to experience supernatural forces',
        'Three wonderfully bizarre Mexican festivals',
        'The 20 greenest destinations on Earth',
        'How to survive on a desert island'
    ]
    return render_template('articles.html', articles=new_articles)

# --- АДМІНКА (форма логіну) ---
@app.route('/admin')
def admin():
    return render_template('login_admin.html')

# --- ДЕТАЛІ ---
@app.route('/details')
def details():
    return render_template('details.html')

# --- ФОРМА КОРИСТУВАЧА ---
@app.route('/form', methods=['GET', 'POST'])
def user_form():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        # Поки просто повертаємо відповідь на екран
        return f"Дякую, {name}! Ми отримали вашу форму."
    return render_template('form.html')


if __name__ == "__main__":
    app.run(debug=True)
