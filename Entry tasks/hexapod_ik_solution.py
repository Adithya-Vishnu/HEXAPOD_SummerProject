import math as m #for the trigonometric functions
import random

# x=random.randint(0,14)#randint basically gives a random variable between provided integers 
# y=random.randint(0,14)#random.randrange(start, stop, step) Like range(), but returns a random number from the sequence.
# z=random.randint(0,14)#random.uniform(a, b) Returns a random float between a and b.
# #random.random() Returns a random floating-point number between 0 and 1.

array=[]
solution=[]

for i in range(0,5):
    x=random.randint(0,14)#randint basically gives a random variable between provided integers  
    y=random.randint(0,14)#random.randrange(start, stop, step) Like range(), but returns a random number from the sequence.
    z=random.randint(0,14)#random.uniform(a, b) Returns a random float between a and b.
    array.append((x,y,z))


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
    x2=5*(m.sin(alpha_rad))
    y2=0
    z2=5*(m.cos(alpha_rad))

    #Getting the distance that has to covered by the femur and tibia

    dist=(((x-x2)**2)+((y-y2)**2)+((z-z2)**2))**(1/2)
    s=(10+15+dist)/2 #semi-perimeter

    test=check_triangle_existence(dist,10,15)

    #print("alpha=",alpha,"    x2=",x2,"     z2=",z2,"   dist=",dist,"   s==",s,sep=' ')
    
    if(test>0):
        print("Sorry not possible to reach")
    else:
        #Using trigonometric formulas to find the angles beta and gamma 

        beta_rad=2*(m.acos(((s*(s-15))/(10*dist))**(1/2)))
        gamma_rad=m.radians(180)-2*(m.acos(((s*(s-dist))/(150))**(1/2)))
        beta=round(m.degrees(beta_rad),2)
        gamma=round(m.degrees(gamma_rad),2)

        #Final Printing
        
        print("α (alpha) =",alpha,"°","  β (beta) =",beta,"°","   γ (gamma)=",gamma,"°")   
        solution.append((alpha,beta,gamma))
   

def test_inverse_kinematics():
    #to run the test cases
    #       TEST 1 
    #typical reachable point {(10.0, 5.0, -10.0)} (since distance to the point is < 25)
    print("TEST 1 - Typical Reachable Point (10.0,5.0,-10.0) \n")
    inverse_kinematics(10.0, 5.0, -10.0)
    print("\n\n")


    #       TEST 2
    # very close to base {(1.0, 1.0, -1.0)} (since the distance to this point is <<25)
    print("TEST 2 - Very Close To Base (1.0,1.0,-1.0) \n")
    inverse_kinematics(1.0, 1.0, -1.0)
    print("\n\n")
    
    #       TEST 3
    # Near max extension {(5.0, -24.0, 0.0)} (since the distance to this point is ~25)
    print("TEST 3 - Near max extension (5.0, -24.0, 0.0) \n")
    inverse_kinematics(5.0, -24.0, 0.0)
    print("\n\n")


    #       TEST 4
    # 	Unreachable (distance > 25 units)	{(20.0, 20.0, -10.0)} (since the distance to this point is >25)
    print("TEST 4 - Unreachable (20.0, 20.0, -10.0) \n")
    inverse_kinematics(20.0, 20.0, -10.0)
    print("\n\n")

    #       TEST 5
    # Foot deeply below base {(5.0, -10.0, 0.0)}()
    print("TEST 5 - Foot deeply below base (5.0, -10.0, 0.0)\n")
    inverse_kinematics(5.0, -10.0, 0.0)
    print("\n\n")

    print("Random variables testing")
    print(array.pop())
    inverse_kinematics(x,y,z)
    print("\n\n")
    print("x = ",x," : y =",y," : z =",z)
    print(array)
    print(solution)




#final calling the TESTING FUNCTION

test_inverse_kinematics()



with open("data.txt", "w") as f:
    f.write("Hello, this is the INPUT set.")
    f.write(str(array))


with open("solution.txt", "w") as g:
    g.write("Hello, this is the OUTPUT set.")
    g.write(str(solution))
