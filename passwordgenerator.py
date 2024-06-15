import random


letter1 = chr(random.randint(97, 122))
letter2 = chr(random.randint(97, 122))
letter3=chr(random.randint(65,90))
letter4=chr(random.randint(65,90))
letter5=chr(random.randint(48,57))
letter6=chr(random.randint(48,57))
letter7=chr(random.randint(33,47))
letter8=chr(random.randint(33,47))
random_letters = letter8 + letter6+letter1+letter4+letter7+letter2+letter5+letter3
print(random_letters)