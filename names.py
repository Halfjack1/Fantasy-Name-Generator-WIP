def dwarf():
  temp = randint(1,3)
  first1 = ["Ba","Brue","Zi","I","U","Kil","Bru","Ka","Gwoi","Fri","Thro","A","Du","Pi"]
  if gend = "M":
    first2 = ["ri","nain", "li","nor","fur","lmal","van","krad","ghal","mral","gnon","rlag","kel"]
  else:
    first2 = ["rdu","narv","tur","znar","kar","da","ri","rvil","kat","rim","ged","ndin"]
  if temp < 3:
    last1 = ["Stone","Steel","Dusk","Battle","Boulder","Brawn","Forge","Stout","Hard","Fire","Frost"]
    last2 = ["shield","blade","hammer","shoulder","anvil","hand","axe","beard","fist"]
  else:
    last1 = ["Troll","Dragon","Orc","Goblin","Gnoll","Drow"]
    last2 = ["killer","slayer","breaker"]
  print(random.choice(first1)+random.choice(first2))
