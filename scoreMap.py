import mysql.connector
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

cnx = mysql.connector.connect(user="1hvINACOm5", password="k1mStgnUk3", host="remotemysql.com", database="1hvINACOm5",port="3306")

cursor = cnx.cursor()

query = ("SELECT PositionX,PositionY,IsHome FROM AppStatistic")

cursor.execute(query)
PositionXList = []
PositionYList = []
IsHomeList = []

for(PositionX,PositionY,IsHome) in cursor:
    PositionXList.append(PositionX)
    PositionYList.append(PositionY)
    IsHomeList.append(IsHome)

cursor.close()

cnx.close()

#for x in range (len(PositionXList)):
#    PositionXList[x] = PositionXList[x] - (PositionXList[x] + PositionXList[x])
print(PositionXList)
for y in range (len(PositionYList)):
    PositionYList[y] = PositionYList[y] - (PositionYList[y] + PositionYList[y])
print(PositionYList)
plt.plot()
for i in range (len(IsHomeList)):
    if (IsHomeList[i] == 1):
        plt.scatter(PositionXList[i],PositionYList[i], c = "b")
    else:
        plt.scatter(PositionXList[i],PositionYList[i], c = "orange")

plt.show()
plt.savefig('shots.png',transparent = True)

img = Image.open("shots.png")
img.thumbnail((1000,350))
background = Image.open("background.jpg")
background.thumbnail((1000,300))

background.paste(img, (-50,-40), img)
background.save('scoreMap.png',"PNG")
