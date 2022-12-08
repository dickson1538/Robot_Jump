
import pickle

# load the previous score if it exists
try:
    with open('score.dat', 'rb') as file:
        score = pickle.load(file)
except:
    score=0

print(score)