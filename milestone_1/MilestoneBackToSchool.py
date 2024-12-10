#MilestoneBackToSchool

#receiving the equasion
eq = input("Enter your quadratic equasion: ")

#format - eq = 5x^2 +4x +    (-10) =  0

#stripping excesive characters 
eq = eq.replace(" ", "").replace("=0", "").replace("(", "").replace(")", "")

#replacing to perform split
eq = eq.replace("x^2", "xsq").replace("x+", "x1")
a_part, rest = eq.split("xsq")
b_part, c_part = rest.split("x1")

#extracting values
a = float(a_part) if a_part else 1   
b = float(b_part) if b_part else 1 
c = float(c_part)

#checking the values
print ("Your values are:", a, b, c)

#solving the equasion
x1 = (-b + ((b**2) - 4*a*c)**0.5)/(2*a)
x2 = (-b - ((b**2) - 4*a*c)**0.5)/(2*a)

#printing the result
print ("Your x are:", x1, "and", x2)