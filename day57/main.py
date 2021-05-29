from flask import Flask
app = Flask(__name__)

from flask import render_template
import random
from datetime import date

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






if __name__ == "__main__":
    app.run(debug=True)