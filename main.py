import time
from random import randint
import os

init_time = time.time()

streak = 0
average = 0
time_taken = 0

correct, mistakes = 0, 0

accuracy = 0

times = []

def generate_number():
  number = randint(0, 15)
  _binary = bin(number)

  return number, _binary

def draw_screen(_streak, _average, _time_taken, _accuracy):
  os.system("clear")
  print(f"""Streak: {_streak}
Accuracy: {_accuracy}
Average Time: {_average}
Previous Time Taken: {_time_taken} """)

try:
  while True:
    number, _binary = generate_number()
    init_time = time.time()
    _input = "f"

    draw_screen(streak, average, time_taken, accuracy)

    while _input != number:
      try:
        _input = int(input(f"{_binary[2:]} "))
      except ValueError:
        mistakes += 1
        streak = 0
        continue
      if _input == number:
        streak += 1
        correct += 1
      
      else:
        streak = 0
        mistakes += 1

    accuracy = (round((correct/(correct + mistakes)), 5) * 100)

    finish_time = time.time()
    time_taken = round((finish_time - init_time), 3)
    times.append(time_taken)
    average = round((sum(times) / len(times)), 3)

except KeyboardInterrupt:
  draw_screen(streak, average, time_taken, accuracy)
  time.sleep(3)
