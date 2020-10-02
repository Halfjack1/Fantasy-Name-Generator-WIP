needSet = True
first1 = []
first2 = []
last1 = []
last2 = []
import names
while True:
  if needSet:
    race = input("Which race?(dragon, dragonborn, dwarf, elf, halfling, human, goblinoid, kobold)\n> ")
    if race.lower() != "kobold":
      gend = input("M or F?\n> ")
    needSet = False
  print()
  for i in range(0, 10):
    if race.lower() == "dwarf":
      names.dwarf(gend)
    elif race.lower() == "human":
      names.human(gend)
    elif race.lower() == "kobold":
      names.kobold()
    elif race.lower() == "goblinoid":
      names.goblinoid(gend)
    elif race.lower() == "elf":
      names.elf(gend)
    elif race.lower() == "halfling":
      names.halfling(gend)
    elif race.lower() == "dragonborn":
      names.dragonborn(gend)
    elif race.lower() == "dragon":
      names.dragon(gend)
    else:
      needSet = True
  if not needSet:
    setCheck = input("\nChange settings?(Y or N)\n> ")
    if setCheck.lower() == "y":
      needSet = True
