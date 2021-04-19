class sport :
	def __init__(self, material, pitch, olympics) :
		self.material = material #matériel utilisé dans ce sport
		self.pitch = pitch #type de terrain s'il y en a un
		self.olympics = olympics #oui ou non

class team (sport): #sport collectif
	def attribute(self,nbr_p,place):
		self.nbr_p=nbr_p #nombre de joueurs par équipe
		self.place=place #type d'endroit où on joue (int/ext...)

	def __str__(self) :
		return("This is a team sport of " +str(self.nbr_p)+ " players per team, and you play it " +str(self.place)+".")

# #On teste un objet dans la sous-classe team :
# volley=team("ball", "parquet", "yes")
# volley.attribute(6,"inside")
# print(volley)


class solo (sport): #sport individuel
	def attribute (self, sensationnal, beginner_age) :
		self.sensationnal=sensationnal #sport à sensations ?
		self.beginner_age = beginner_age #à quel âge peut on commencer ce sport ?

	def __str__(self) :
		return ("You can start this solo sport at " +str(self.beginner_age)+ ". Is it sensationnal ? " +str(self.sensationnal)+ ".")

# #On teste un objet dans la sous-classe solo
# horseriding=solo("horse", "arena", "yes")
# horseriding.attribute("Sometimes yes", 6)
# print(horseriding)
