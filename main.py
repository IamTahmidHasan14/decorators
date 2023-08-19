def dec(f):

  def mf(*arg, **kwarg):  #ONLY WHEN ARGUMENTS ARE PASSING THROUGH FUNCTION
    print("Good morning.")
    f(*arg, **kwarg)  #ONLY WHEN ARGUMENTS ARE PASSING THROUGH FUNCTION
    print("Thanks for using this function.\n")

  return mf


@dec
def hello():
  print("Hello, Tahmid Hasan")


@dec
def sum(a, b):
  print(f"{a}+{b}={a+b}")


# dec(hello)()
hello()
# dec(sum)(6,7)
sum(6, 7)