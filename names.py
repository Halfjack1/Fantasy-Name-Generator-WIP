import random
def dwarf(gend):
  temp = random.randint(1,3)
  first1 = ["Ba","Brue","Zi","I","U","Kil","Bru","Ka","Gwoi","Fri","Thro","A","Du","Pi"]
  if gend.lower() == "m":
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
  temp = random.randint(3,6)
  if gend.lower() == "m":
    if temp == 3:
      #Rashemi
      first1 = ["Bori", "Faur", "Jan", "Kani", "Madis","Ral", "Shau", "Vladis"]
      first2 = ["vik", "gar", "dar", "thar", "lak", "mevik", "mar", "lak"]
      last1 = ["Cherg","Dyern", "Iltazy", "Murnyeth", "Stayan", "Ulmok"]
      last2 = ["oba", "ina", "ara", "ara", "oga", "ina"]
    elif temp == 4:
      #Damaran
      first1 = ["B","F","Gl","Grig","Ig","Iv","Kos", "M", "Or","Pav","Serg"]
      first2 = ["or", "odel", "ar", "or", "an", "or", "ef", "ival", "el", "el", "or"]
      last1 = ["Be","Che","Do","Ku","Ma","Neme","She","Sta"]
      last2 = ["rsk", "rnin", "tsk", "lenov", "rsk", "tsk", "mov", "rag"]
    elif temp == 5:
      #Chondathon
      first1 = ["Darv", "Dorn", "Even", "Gor","Ran"]
      first2 = ["in", "", "", "dur", "stag", "dal"]
      last1 = ["Amble", "Buck", "Dun", "Even", "Grey", "Tall"]
      last2 = ["crown","man","dragon","wood","castle","stag"]
    else:
      #Calashite
      first1 = ["As","Bard","Has","Khem","Mehm","Sud","Zash"]
      first2 = ["eir", "eid", "ed", "en", "eiman"]
      last1 = ["Bash","Dum","Jass","Khal","Pash","R"]
      last2 = ["a","ein","an","id","ar"]
  else:
    if temp == 3:
      #Rashemi
      first1 = ["Fye","Hul","Im","Im","Na","She","Tam","Yul"]
      first2 = ["varra", "marra", "mith", "zel", "varra", "varra", "mith", "dra"]
      last1 = ["Cherg","Dyern", "Iltazy", "Murnyeth", "Stayan", "Ulmok"]
      last2 = ["oba", "ina", "ara", "ara", "oga", "ina"]
    elif temp == 4:
      #Damaran
      first1 = ["Ale","Ka","Kate","Ma","Nata","Ta","Zo"]
      first2 = ["thra", "ra", "rnin", "ra", "li", "na", "ra"]
      last1 = ["Be","Che","Do","Ku","Ma","Neme","She","Sta"]
      last2 = ["rsk", "rnin", "tsk", "lenov", "rsk", "tsk", "mov", "rag"]
    elif temp == 5:
      #Chondathon
      first1 = ["Esv", "Arve", "Jhess", "Kerr","Lure", "Mir", "Row", "Shandr", "Tess"]
      first2 = ["ene", "ele", "ail", "i", "an", "ele"]
      last1 = ["Amble", "Buck", "Dun", "Even", "Grey", "Tall"]
      last2 = ["crown","man","dragon","wood","castle","stag"]
    else:
      #Calashite
      first1 = ["At","Ceid","Ham","Jasm","Meil","Zash","Seip"]
      first2 = ["ala","il","a","al","ora","eida"]
      last1 = ["Bash","Dum","Jass","Khal","Pash","R"]
      last2 = ["a","ein","an","id","ar"]
  temp = (random.choice(first1) + random.choice(first2) + " " + random.choice(last1) + random.choice(last2))
  print(temp)

def kobold():
  first1 = ["Mee","Ka","Za","Ze","Mo","Ro","Ta","U","I","Ga","Sni","Ho"]
  first2 = ["po","shak","kak","lo","klak","rak","rtos","lax","v","k","x"]
  temp = random.choice(first1) + random.choice(first2)
  print(temp)