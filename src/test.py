from models import YACC
from faker import Faker
import random
from collections import OrderedDict

#Going to upgrade all of my projects to 3.6, dictionaries maintain
#order, would be pretty nice to strictly enfore header order
inputdict = OrderedDict({"ID":lambda:random.randrange(100,200), "Name":lambda:f.name(),  "SSN":lambda:f.ssn()})
f = Faker()
y = YACC(inputdict, f)
y.generate(10)
y.close()
