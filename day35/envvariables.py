# Environment variables allow us to store our keys and other secrets away from our code

# type export NAMEOFKEY=key in the terminal
# export SAMPLE_API_KEY=875894jidjf939he20u92h1hi2hru2

# to tap into it
import os
api_key = os.environ.get('SAMPLE_KEY')
print(api_key)