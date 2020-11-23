class demo :
	# pass #using for empty class
	#constructor
	#*args mean we want to provide list
	#**kwargs mean we want to provide distionatry
	def __init__(self,*args):
		print("constructor",args)
class add:
	def __init__(self,x=1,y=2):
		#__ use for make atribute private 
		self.__x=x
		self.__y=y
	def setter(self,x=9,y=8):
		self.x=x
		self.y=y
	def gatter(self):
		return self.x,self.y,self.__x,self.__y
	def name(self,*args):
		return all
		

demo1=demo();
demo2=demo();
demo3=demo();
demo1.name="nish"
demo2.name="prajapat"
demo3.name="unaffected"
print(demo1.name)
print(demo2.name)
print(demo3.name)

#__ make atribute private

add=add(2,3)
#  print(add._x,add.__y) error bcz y is private
#gatter and setter
add.setter(2,3)
print(add.gatter())
#default perameter consturctore
add.setter();
print(add.gatter())
#all perameter
demo3=demo('name','nish')