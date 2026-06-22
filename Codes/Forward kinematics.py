#TESTING
import math as m

coxa=8.05
femur=14.8
tibia=22.6

lists=[[45.0, 140.02, 120.8], [44.49, 144.5, 123.15], [43.94, 149.06, 125.37], [43.35, 153.71, 127.46], [42.71, 158.42, 129.4], [42.01, 163.2, 131.21], [41.22, 168.02, 132.87], [40.31, 172.89, 134.4], [39.21, 177.84, 135.81], [27.4, 179.26, 141.22], [26.33, 174.61, 140.6], [25.38, 169.71, 139.66], [24.51, 164.67, 138.44], [23.71, 159.54, 136.96], [22.96, 154.41, 135.25], [22.26, 149.31, 133.33], [21.59, 144.28, 131.23]];

list2=[]

for i in range(len(lists)):
     
    alpha=lists[i][0]
    beta=lists[i][1]-90
    gamma=lists[i][2]


    x1=(coxa+femur*abs((m.cos(beta*(m.pi/180))))+tibia*(m.cos((gamma-beta)*(m.pi/180))))*abs(m.sin(alpha*(m.pi/180)))
    z1=(coxa+femur*abs(m.cos(beta*(m.pi/180)))+tibia*(m.cos((gamma-beta)*(m.pi/180))))*abs(m.cos(alpha*(m.pi/180)))
    y1=femur*(m.sin(beta*(m.pi/180)))-tibia*(m.sin((gamma-beta)*(m.pi/180)))



   # print("coxa = ",coxa," femur = ",femur*abs((m.cos(beta*(m.pi/180))))," tibia = ",tibia*(m.cos((gamma-beta)*(m.pi/180))))
    list2.append([x1,z1,y1])


print(list2)