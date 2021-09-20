from flask import Flask
app = Flask(__name__)

from flask import render_template
import random
from datetime import date
import requests

@app.route('/')
def index():
    random_num = random.randint(1,10)
    current_date = date.today()
    print(current_date)
    # print(date.today())
    # >>>2021-05-29
    current_year = current_date.year
    print(current_year)
     # >>>2021
    return render_template('index.html',num=random_num, year=current_year)



@app.route('/guess/<guessname>')
def guess(guessname):
    # parameters = {
    #     'name': guessname
    # }
    # agify_response = requests.get(url="https://api.agify.io",params=parameters)
    # gender_response = requests.get(url="https://api.genderize.io",params=parameters)
    # or 
    agify_response = requests.get(url=f"https://api.agify.io/?name={guessname}")
    gender_response = requests.get(url=f"https://api.genderize.io/?name={guessname}")

    agify_response.raise_for_status()
    dataone = agify_response.json()
    datatwo = gender_response.json()
    print(dataone)
    agify_name = dataone["name"]
    print(agify_name)
    agyify_age=dataone["age"]
    print(agyify_age)
    print(datatwo)
    gender = datatwo["gender"]
    print(gender)
    return render_template('index.html',name=agify_name,age=agyify_age, gender=gender )


# guess('ashley')


    





if __name__ == "__main__":
    app.run(debug=True)