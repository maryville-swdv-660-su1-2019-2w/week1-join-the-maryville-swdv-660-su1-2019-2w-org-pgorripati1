#Pardhu Gorripati
import colorise
import random_name

colorList = ['purple', 'red', 'green', 'cyan', 'blue', 'yellow']

for eachColor in colorList:
    colorise.set_color(eachColor)
    print('\n',random_name.generate_name())
        
colorise.set_color()
input("Press ENTER to continue!")


 