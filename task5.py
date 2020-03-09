class1 = int(input ('how many students'))
class2 = int(input('how many students'))
class3 = int(input('how many students'))

if class1 % 2 == 0:
    desk1 = int(class1 / 2)
elif class1 % 2 == 1 :
    desk1 = int(class1 / 2 + 1)

if class2 % 2 == 0:
    desk2 = int(class2 / 2)
elif class2 % 2 == 1:
    desk2 = int(class2 / 2 + 1)

if class3 % 2 == 0:
    desk3 = int(class3 / 2)
elif class3 % 2 == 1:
    desk3 = int(class3 / 2 + 1)

result = (desk1 + desk2 + desk3)
print(result)    


 

 






