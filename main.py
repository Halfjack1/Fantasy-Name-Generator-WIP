needSet = True
first1 = []
first2 = []
last1 = []
last2 = []
import names
while True:
  if needSet:
    race = input("Which race?(dwarf, human, )\n> ")
    if race.lower() != "kobold":
      gend = input("M or F?\n> ")
    needSet = False
  print()
  for i in range(0, 10):
    if (race.lower() == "dwarf"):
      names.dwarf(gend)
    elif race.lower() == "human":
      names.human(gend)
    elif race.lower() == "kobold":
      names.kobold()
    else:
      needSet = True
  if needSet == False:
    setCheck = input("\nChange settings?(Y or N)\n> ")
    if setCheck.lower() == "y":
      needSet = True
