# 책에서는 walk와 magic을 print로 출력하게 되었다.
# 하지만 이럴 경우 마지막엔 반드시 빈값이 리턴되기 때문에
# walk는
# I can walk
# None
# 이라고 출력 되는 증상을 return 으로 바꿔줌으로 고쳤다.

class Human():
    hp = 100
    name = "기본 이름"
    
    def walk(self):
        return "I can walk"
        
class Wizard(Human):
    def __init__(self, name):
        self.name = name
        
    def magic(self):
        return "magic"

my_char = Wizard("지존짱짱") 

print(my_char.name)
print("--")
print(my_char.hp)
print("--")
print(my_char.walk())
print("--")
print(my_char.magic())