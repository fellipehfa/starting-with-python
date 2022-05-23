import random

from sample_madlibs import code, harrypotter, hungergames, zombie

if __name__ == "__main__":
  m = random.choice([harrypotter, code, zombie, hungergames])
  m.madlib()
