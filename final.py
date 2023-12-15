from flask import Flask, render_template, request
import requests 

title_2 = 'There is no middle ground.'
url = 'https://thronesapi.com/api/v2/Characters'
r = requests.get(url)
results = r.json()
app = Flask(__name__)
# hi
@app.route('/')
def home():
    return render_template('home.html', title_2 = title_2)

@app.route('/characters')
def characters():
    return render_template('characters.html', chars = results)

@app.route('/form', methods = ["POST", "GET"])
def myform():
    if request.method == "POST":
        character_id = request.form['name']
        full_name = request.form['full-name']

        ID = int(character_id)
        character = results[ID]
        if ID < 53 and ID >= 0 and full_name == character['fullName']:
            return f"""
            <body style="background-color: gray;">
            <p style="text-align:center; margin-top:180px; font-size:36px; color:white">ID: {character['id']}</p>
            <p style="text-align:center; margin:20px; font-size:36px; color:white">First Name: {character['firstName']}</p>
            <p style="text-align:center; margin:20px; font-size:36px; color:white">Last Name: {character['lastName']}</p>
            <p style="text-align:center; margin:20px; font-size:36px; color:white">Full Name: {character['fullName']}</p>
            <p style="text-align:center; margin:20px; font-size:36px; color:white">Title: {character['title']}</p>
            <p style="text-align:center; margin:20px; font-size:36px; color:white">Family: { character['family']}</p>
            </body>
            """
        
        else:
            return f"""
            <h1 style="font-family: Game of Thrones; text-align:center; margin:200px; font-size:48px;">
            You&#39;re not in Game of Thrones</h1>
            <p style="text-align: center; font-size:24px;">ID: {character_id}<br>Full Name: {full_name}</p>
            """

    return render_template('forms.html')

if __name__ == '__main__':
    app.run(debug = True)

