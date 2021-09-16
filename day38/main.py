from datetime import datetime
import requests
import os

# APP_ID=dac25175
NUTRITIONIX_API_KEY= os.environ['NUTRITIONIX_API_KEY']
NUTRITIONIX_APP_ID= os.environ['NUTRITIONIX_APP_ID']

# # TODO Make Request

exercise_endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY
}
params = {
    
            "query":"cycled 5 kilometers",
            "gender":"female",
            "weight_kg":58.5,
            "height_cm":149.64,
            "age":28
    
  
}

exercise_response = requests.post(url=exercise_endpoint,json=params, headers=headers)
print(exercise_response)
# print(exercise_response.json())
exercise = exercise_response.json()
print(exercise)
name = exercise['exercises'][0]['name']
duration = exercise['exercises'][0]['duration_min']
calorie_count = exercise['exercises'][0]['nf_calories']

# get date
day = datetime(2021, 9, 10)
time = datetime.now()
workout_date = time.strftime("%Y-%m-%d")
print(time)
workout_time = time.strftime("%H:%M:%S")
print(workout_time)
# TODO Write to google sheet

# sheety_get_endpoint = "https://api.sheety.co/50b9f572d8bb9e2b9755ec54abd6fc25/workoutTracking/workouts"
# sheety_get_response = requests.get(sheety_get_endpoint)
# print(sheety_get_response)
# print(sheety_get_response.json())

sheety_add_endpoint = "https://api.sheety.co/50b9f572d8bb9e2b9755ec54abd6fc25/workoutTracking/workouts"
add_params = {
  "workout": {
	"Date":workout_date,
    "Time": workout_time,
    "Exercise": name,
    "Duration": duration,
    "Calories": calorie_count
  }
} 
# print(add_params.json())
sheety_add_response = requests.post(url=sheety_add_endpoint, json=add_params)
print(sheety_add_response)
print(sheety_add_response.json())
