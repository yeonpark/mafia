import random
import csv
class mafia: #마피아들이 가지고 있어야 하는 특성들
	
	#surname = ["Park", "Kim", "Lee", "Choi", "Kwon"]
	#sex1 = ["Male", "Female"]
	def __init__(self):
		self.surname = ["Park", "Kim", "Lee", "Choi", "Kwon"]
		self.sex1 = ["Male", "Female","Unknown"]

	def personal_info(self):
		self.name = random.choice(self.surname)
		self.age = random.randint(1,100)
		self.sex = random.choice(self.sex1)

def make_mafia():
	a = mafia()
	a.personal_info()
	return a.name, str(a.age), a.sex

f=open("mafia.csv", "w", newline='')
makewrite = csv.writer(f)
for i in range(10):
	makewrite.writerow(make_mafia())
	
f.close()
