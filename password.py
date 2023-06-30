import random
import string
import numpy

passwordlength = int(input("please enter the length of password you need\n"))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers =string.digits
panc = string.punctuation
hexa = string.hexdigits.upper()
combine = lower + upper + panc + numbers
rand =random.sample(combine,passwordlength)
passw = "".join(rand)
print(passw)
# hh=["sef","tg", "digk"]
# hh.append("hello")
# print(hh)

