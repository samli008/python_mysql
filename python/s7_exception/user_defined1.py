# user defined exception
class error(Exception):
  pass
class toosmall(error):
  pass
class toolarge(error):
  pass

number=10

while True:
  try:
    num=int(input("Enter a number: "))
    if num < number:
      raise toosmall
    elif num > number:
      raise toolarge
    break
  except toosmall:
    print("This value is too small,try again!\n")
  except toolarge:
    print("This value is too large,try again!\n")

print("Congratulation! you guessed it correctly.")
