#store and read a tuple of scores
scores = (72,85,90,85)
first_score = scores[1]
last_score = scores[-1]
print(f"first score: {first_score} and last score: {last_score}")
print(scores.count(85))
a, b =  scores[:2]
scores[0] = 100