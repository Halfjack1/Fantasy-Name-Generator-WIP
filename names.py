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

def goblinoid(gend):
  first1 = ["Ut", "Mor", "Krev", "Oza", "Drak", "Az"]
  if gend.lower() == "M":
    first2 = ["char", "korz", "lek", "luc", "kor", "kral"]
  else:
    first2 = ["cha", "kora", "le", "lua", "ra"]
  last1 = ["I", "Irta","Kee", "Be", "Caba", "Ery", "Fo", "Na", "O", "Ru"]
  last2 = ["llish", "na", "zac", "go", "lig", "llus", "tulk","rgath", "grok","kwurm"]
  temp = random.choice(first1) + random.choice(first2) + " " + random.choice(last1) + random.choice(last2)
  print(temp)

def elf(gend):
  first1 = ["A","Ae","Keyl","Aran","Be","Ber","Car","Dru","Eni","Er","Galin","Had","He","Im","Ivel","Lauc","Mind","Pael","Per","Quar","Riard","Rol","Sovel","Tham","Sil"]
  if gend.lower() == "m":
    first2 = ["dran","lar","mil","nis","ust","iro","ric","rian","alis","rdan","evan","ndan","arai","ian","meral","lios","artis","ias","en","ion","on","iss","ior"]
  else:
    first2 = ["drie","lthaea","strianna","ndraste","ntinua","thrynna","rel","elynn","silia","losial","elenia","riele","eth","nairra","aqui","astra","aphia"]
  last1 = ["Ama","Gala","Holi","Ilphel","Lia","Meli","Nai","Sian"," Xilo"]
  last2 = ["kiir","stacia","nodel","mion","don","amne","lo","scient"]
  temp = (random.choice(first1) + random.choice(first2) + " " + random.choice(last1) + random.choice(last2))
  print(temp)

def halfling(gend):
  if gend.lower() == "m":
    first1 = ["Alton","Ander","Cade","Corrin","Eldon","Errich","Finnan","Garret","Lindal","Lyle","Merric","Milo","Osborn","Perrin","Reed","Roscoe","Wellby"]
  else:
    first1 = ["Andry", "Bree", "Callie", "Cora", "Euphemia","Jillian", "Kithri", "Lavinia", "Lidda", "Merla", "Nedda", "Paela","Portia", "Seraphina", "Shaena", "Trym", "Vani", "Verna"]
  last1 = ["Brush","Good","Green","High-","hill","Tea","Thorn","Toss","Under"]
  last2 = ["gather","barrel","bottle","hill","topple","leaf","gage","cobble","bough"]
  temp = (random.choice(first1) + " " + random.choice(last1) + random.choice(last2))
  print(temp)

def dragonborn(gend):
  first1 = ["Arjh", "Balas", "Bhar", "Don", "Gh", "Hesk", "Kr", "Medr", "Meh", "Nad", "Pandj", "Patr","Rhog", "Sham", "Shed", "Tarh", "Tor", "Akr", "B", "D", "Farid", "Har", "Flav", "Jher", "K", "Kor", "Mish", "N", "Perr", "S", "Surin", "Thav", "Uadj"]
  if gend.lower() == "m":
    first2 = ["an", "ar", "ash", "aar", "esh", "an", "iv", "ash", "en", "arr", "ed","in", "ar", "ash", "inn", "un", "inn"]
  else:
    first2 = ["a", "iri", "aar", "eh", "ann", "ilar", "i", "ava", "inn", "ann", "ala", "a", "ora", "a", "a", "it"]
  last1 = ["Clethtin", "Daar", "Del", "Drache", "Fenken", "Kerr", "Kimba", "Linxaka", "Mya", "Nori", "Ophin", "Prexi", "Shesten", "Turnu", "Verthi", "Yar"]
  last2 = ["thiallor", "dendrian", "mirev", "dandion", "kabradon", "hylon", "tuul", "sendalor", "stan", "xius", "shtalajiir", "jandilin", "deliath", "roth", "sathurgiesh", "jerit"]
  temp = (random.choice(first1) + random.choice(first2) + " " + random.choice(last1) + random.choice(last2))
  print(temp)

def dragon(gend):
  first1 = ["Clethtin", "Daar", "Del", "Drache", "Fenken", "Kerr", "Kimba", "Linxaka", "Mya", "Nori", "Ophin", "Prexi", "Shesten", "Turnu", "Verthi", "Yar"]
  temp1 = random.choice(first1)
  first2 = ["Clethtin", "Daar", "Del", "Drache", "Fenken", "Kerr", "Kimba", "Linxaka", "Mya", "Nori", "Ophin", "Prexi", "Shesten", "Turnu", "Verthi", "Yar"]
  if temp1 in first2:
    first2.remove(temp1)
  first3 = ["cl", "ch", "d", "k", "k", "d", "ch", "k", "g", "k", "dr", "sh", "dr", "cl", "dr", "ch", "d"]
  if gend.lower() == "m":
    first4 = ["an", "ar", "ash", "aar", "esh", "an", "iv", "ash", "en", "arr", "ed","in", "ar", "ash", "inn", "un", "inn"]
  else:
    first4 = ["a", "iri", "aar", "eh", "ann", "ilar", "i", "ava", "inn", "ann", "ala", "a", "ora", "a", "a", "it"]
  temp = temp1 + random.choice(first2).lower() + random.choice(first3) + random.choice(first4)
  print(temp)