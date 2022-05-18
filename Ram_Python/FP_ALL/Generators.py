"""Generator is a function which is used to generate sequence of elements By using a keyword called yield.
  YIELD
  Yield is a keyword which is used to  make the  control come out from the function and  pauses the current
  excicution to store the value into result variable then it will go back to the same function to excicute remaining
  iterations"""

def sam():
    print("hai")
    yield 1
    print("hello")
    yield 2
    print("bye")
res = sam()
print(tuple(res))
