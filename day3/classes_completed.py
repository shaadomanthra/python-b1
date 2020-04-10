## working with classes and objects

# define class
class school():
# define methods
  def maths(self):
    print ("I am from maths class")

  def english(self):
    print ("I am from english, & my school name is " + self.name)

  def science(self, topic):
    print ("I am from science, & todays topic is " + topic)

# create object   
mySchool = school()
# invoke methods
mySchool.maths()

mySchool.name = "Glindale Academy"
mySchool.english()

mySchool.science("Newtons Laws")


  
