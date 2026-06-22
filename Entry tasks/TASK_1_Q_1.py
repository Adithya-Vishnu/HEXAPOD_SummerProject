import math as m #for the trigonometric functions

xₕ=(float(input("Enter the value of xₕ : ")))
yₕ=(float(input("Enter the value of yₕ : ")))

x1=(float(input("Enter the value of X₁ : ")))
y1=(float(input("Enter the value of Y₁ : ")))

x2=(float(input("Enter the value of X2 : ")))
y2=(float(input("Enter the value of Y2 : ")))

coxa=float(input("Enter the length fo the coxa : "))
femur=float(input("Enter the length fo the femur : "))
tibia=float(input("Enter the length fo the tibia : "))

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
    x2=coxa*(m.sin(alpha_rad))
    y2=0
    z2=coxa*(m.cos(alpha_rad))

    #Getting the distance that has to covered by the femur and tibia

    dist=(((x-x2)**2)+((y-y2)**2)+((z-z2)**2))**(1/2)
    s=(abs(femur)+abs(tibia)+abs(dist))/2 #semi-perimeter

    test=check_triangle_existence(abs(dist),abs(femur),abs(tibia))

    print(f'''dist={dist} femur={femur} tibia={tibia}''')

    #print("alpha=",alpha,"    x2=",x2,"     z2=",z2,"   dist=",dist,"   s==",s,sep=' ')
    
    if(test>0):
        return 0
    else:
        
        #Using trigonometric formulas to find the angles beta and gamma 

        beta_rad=2*(m.acos(((s*(s-tibia))/(femur*dist))**(1/2)))
        gamma_rad=m.radians(180)-2*(m.acos(((s*(s-dist))/(150))**(1/2)))
        beta=round(m.degrees(beta_rad),2)
        gamma=round(m.degrees(gamma_rad),2)

        #2.5
        # Final Printing
        
        print("α (alpha) =",alpha,"°","  β (beta) =",beta,"°","   γ (gamma)=",gamma,"°")   
        return 1
   
if((inverse_kinematics(xₕ-x1,yₕ-y1,0)==1) and(inverse_kinematics(x2-xₕ,yₕ-y2,0)==1) ):
    print("Handshake possible")
else:
    print("sorry handshake not possible") 
