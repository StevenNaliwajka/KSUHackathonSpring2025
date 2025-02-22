from app import app
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        name = request.form.get('name')
        phone = request.form.get('phone')
        return f"Name:{name} and phone:{phone}"

    return render_template('index.html')