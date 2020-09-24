needSet = True
first1 = []
first2 = []
last1 = []
last2 = []
import names
while True:
  if needSet:
    race = input("Which race?(dwarf, )\n> ")
    gend = input("M or F?\n> ")
    needSet = False
  switch (lower(race)){
    case "dwarf":
      break;
    default: needSet = True
      break;
  }
  if needSet == False:
    setCheck = input("Change settings?(Y or N)\n> ")
    if setCheck == "Y":
      needSet = True

