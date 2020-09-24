import random
def dwarf(gend):
  temp = random.randint(1,3)
  first1 = ["Ba","Brue","Zi","I","U","Kil","Bru","Ka","Gwoi","Fri","Thro","A","Du","Pi"]
  if gend.lower() != "f":
    first2 = ["ri","nain", "li","nor","fur","lmal","van","krad","ghal","mral","gnon","rlag","kel"]
  else:
    first2 = ["rdu","narv","tur","znar","kar","da","ri","rvil","kat","rim","ged","ndin"]
  if temp < 3:
    last1 = ["Stone","Steel","Dusk","Battle","Boulder","Brawn","Forge","Stout","Hard","Fire","Frost"]
    last2 = ["shield","blade","hammer","shoulder","anvil","hand","axe","beard","fist"]
  else:
    last1 = ["Troll","Dragon","Orc","Goblin","Gnoll","Drow"]
    last2 = ["killer","slayer","breaker"]
  temp = (random.choice(first1) + random.choice(first2) + " " + random.choice(last1) + random.choice(last2))
  print(temp)


def human(gend):
  temp = random.randint(1,6)
  if gend.lower() != "f":
    if False:#temp == 1:
      first1 = [""]
      first2 = []
      last1 = []
      last2 = []
    else:
      #calashite
      first1 = ["As","Bard","Has","Khem","Mehm","Sud","Zash"]
      first2 = ["eir", "eid", "ed", "en", "eiman"]
      last1 = ["Bash","Dum","Jass","Khal","Pash","R"]
      last2 = ["a","ein","an","id","ar"]
  else:
    if False:#temp == 1:
      first1 = [""]
      first2 = []
      last1 = []
      last2 = []
    else:
      #calashite
      first1 = ["At","Ceid","Ham","Jasm","Meil","Zash","Seip"]
      first2 = ["ala","il","a","al","ora","eida"]
      last1 = ["Bash","Dum","Jass","Khal","Pash","R"]
      last2 = ["a","ein","an","id","ar"]
  temp = (random.choice(first1) + random.choice(first2) + " " + random.choice(last1) + random.choice(last2))
  print(temp)