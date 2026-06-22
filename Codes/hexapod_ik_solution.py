import math as m #for the trigonometric functions

def check_triangle_existence(a,b,c):
    '''For checking if the given point is ever accessible or not'''
    flag=100
    if(c>(a+b)):
        return 1
    elif((b+c)<a):
        return 1
    elif((c+a)<b):
        return 1
    else:
        return 0


def inverse_kinematics(x, y, z):
    #to take an input of cartesian coordinates and output the angles alpha,beta and gamma if possible
    if(z==0):
        #solving the issues of atan() which cannot produce the output if z==0 and x>0;
        alpha_rad=(m.pi)/2
    elif(z==0 and x<0):
        #solving the issues of atan() which cannot produce an output when z==0 and x<0
        alpha_rad=(-(m.pi))/2
    else:
        #can be understood from the top view
        alpha_rad=(m.atan(x/z))
    #converting the radians to degrees for outputting purposes
    alpha=round(m.degrees(alpha_rad),2)
    
    #getting the position of the end of the coxa's arm in order to reduce the variables in the coming equations
    x2=(8.05)*(m.sin(alpha_rad))
    y2=0
    z2=(8.05)*(m.cos(alpha_rad))

    #Getting the distance that has to covered by the femur and tibia

    dist=(((x-x2)**2)+((y-y2)**2)+((z-z2)**2))**(1/2)
    s=(22.6+14.8+dist)/2 #semi-perimeter
    print("The s and distance and alpha are",s,dist,alpha)
    print(x,y,z)
    test=check_triangle_existence(dist,14.8,22.6)

    #print("alpha=",alpha,"    x2=",x2,"     z2=",z2,"   dist=",dist,"   s==",s,sep=' ')
    beta_rad=2*(m.acos(((s*(s-22.6))/(14.8*dist))**(1/2)))
    gamma_rad=m.radians(180)-2*(m.acos(((s*(s-dist))/(334.48))**(1/2)))
    beta=round(m.degrees(beta_rad),2)
    gamma=round(m.degrees(gamma_rad),2)
    theta=m.asin(-y/dist)
    theta=round(m.degrees(theta),2)
    #theta=m.atan(abs(y)/(((x-x2)**2+(z-z2)**2)**(1/2)))
    beta=90+beta-theta

    if(test>0 or beta<0 or beta>180 or gamma<0 or gamma>180):
        print("Sorry not possible to reach")
        print("α (alpha) =",alpha,"°","  β (beta) =",beta,"°","   γ (gamma)=",gamma,"°")
        print("-----------------------32")
        
    else:
        #Using trigonometric formulas to find the angles beta and gamma 
        #Final Printing
        
        print("α (alpha) =",alpha,"°","  β (beta) =",beta,"°","   γ (gamma)=",gamma,"°")
        print("------------------------")
        return [alpha,round(beta,2),gamma]
        
   

def test_inverse_kinematics():
    #to run the test cases
    #       TEST 1 
    #typical reachable point {(10.0, 5.0, -10.0)} (since distance to the point is < 25)
    #inverse_kinematics(14.1421,0,42.4264)
    
    # inverse_kinematics(28.2842,0,28.2842)
    # inverse_kinematics(27.9214,1,28.6471)
    # inverse_kinematics(27.5378,2,29.0308)
    # inverse_kinematics(27.1293,3,29.4393)
    # inverse_kinematics(26.6904,4,29.8781)
    # inverse_kinematics(26.2132,5,30.3553)
    # inverse_kinematics(25.6853,6,30.8832)
    # inverse_kinematics(25.0862,7,31.4824)
    # inverse_kinematics(24.3755,8,32.1931)
    # inverse_kinematics(23.4493,9,33.1193)
    
    # inverse_kinematics(18.9771,9,37.5914)
    # inverse_kinematics(18.0509,8,38.5176)
    # inverse_kinematics(17.3402,7,39.2283)
    # inverse_kinematics(16.7411,6,39.8275)
    # inverse_kinematics(16.2132,5,40.3553)
    # inverse_kinematics(15.736,4,40.8326)
    # inverse_kinematics(15.2971,3,41.2714)
    # inverse_kinematics(14.8886,2,41.6799)
    # inverse_kinematics(14.505,1,42.0635)
    # inverse_kinematics(14.1421,0,42.4264)

    # print("The top point is :")

    


    # inverse_kinematics(21.2132,10,35.3553)

    Points =[[17.67705743504021, 17.67705743504021, -9.99953245453118], [17.430096358412758, 17.74318833692322, -9.000139934173214], [17.166981821869598, 17.814225139201646, -8.001508331965208], [16.887340427966095, 17.889107167932657, -7.000180499489936], [16.588912359698398, 17.97093781045842, -5.999986619821387], [16.263360378063815, 18.0559531391428, -4.9996483546571895], [15.902680577600321, 18.152696490621352, -4.001178477340751], [15.492256016531867, 18.261379117809334, -3.0032063660415798], [15.006927750291181, 18.393755912354347, -1.9976685140016883], [10.20148892429223, 19.680667218345576, -3.0005592889606234], [9.793934151192728, 19.790425393386823, -3.999483207535407], [9.434267303458807, 19.88643310871791, -5.000345362615562], [9.106601507967204, 19.973374484823644, -5.9994088746736285], [8.806630820419779, 20.05255509948879, -7.001217811133753], [8.527341670332593, 20.128216042821812, -7.999852247530271], [8.267771881750457, 20.199066132048802, -8.999555274192218], [8.019264264000974, 20.264682192260675, -10.000497755463941]]
    Angles=[]

    for i in range(len(Points)):
        Angles.append(inverse_kinematics(Points[i][0],Points[i][1],Points[i][2]))
        
        
    print(Angles)

    #       TEST 2
    # very close to base {(1.0, 1.0, -1.0)} (since the distance to this point is <<25)
    #print("TEST 2 - Very Close To Base (1.0,1.0,-1.0) \n")
    #inverse_kinematics(1.0, 1.0, -1.0)
    #print("\n\n")
    
    #       TEST 3
    # Near max extension {(5.0, -24.0, 0.0)} (since the distance to this point is ~25)
    #print("TEST 3 - Near max extension (5.0, -24.0, 0.0) \n")
    #inverse_kinematics(30.0, 30.0, 0.0)
    #print("\n\n")


    #       TEST 4
    # 	Unreachable (distance > 25 units)	{(20.0, 20.0, -10.0)} (since the distance to this point is >25)
    #print("TEST 4 - Unreachable (20.0, 20.0, -10.0) \n")
    #inverse_kinematics(20.0, 20.0, -10.0)
    #print("\n\n")

    #       TEST 5
    # Foot deeply below base {(5.0, -10.0, 0.0)}()
    #print("TEST 5 - Foot deeply below base (5.0, -10.0, 0.0)\n")
    #inverse_kinematics(5.0, -10.0, 0.0)
    #print("\n\n")

    #TEST FOR FINDING COORDINATES------------

    #print("Code 20,0,20")
    #inverse_kinematics(20.0, 0.0, 0.0)
    #print("\n\n")


    

    

#final calling the TESTING FUNCTION

test_inverse_kinematics()