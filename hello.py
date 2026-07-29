class person:
    def __init__(self,name,age):
      self.name = name
      self.age = age

    def getName(self):
       return self.name
    def getAge(self):
       return self.age

p1= person("bob",22)

print(p1.getName())
print(p1.getAge()) 
