from personexception.person import Person
from personexception.PException import AgeException

p=Person()
p.setName("曹东雪")

try:
    p.setAge(0)
except AgeException as e:
    print(e)