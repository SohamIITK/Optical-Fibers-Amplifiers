import numpy as np

n = 1.5 # Refractive index of core
l = 1.55e-6 # Wavelength in metres

print (" Incase of wavelength lambda =", l *1e6 , "\mu m")

a = 5e-6 # Radius of core

loop = 1 #To keep count of allowed angles of incidence

# Just keep the range of for loopbig enough . Loop terminates
#at theta_max = 14.1 degrees
# Change theta_max as per your own calculations
# I'll try to improve this code to include that calculation as well
for i in range (1 ,15) :
    theta = np . arcsin ( i * l /(2* a * n ) ) # arcsin calculates in radian
    
    b = 2* np . pi * n * np . sin ( theta ) / l
    
    if theta *180/ np . pi > 14.1:     #For terminating the loopbreak
        break
    
    print ("For m =", i , " theta in degrees is", theta *180/ np . pi )
    
    
    print (" Beta ", loop , " = ",b /1e6 , " times 10^6 ")
    loop = loop + 1
    print()