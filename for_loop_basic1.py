#Basic - Print all integers from 0 to 150.
for basic in range(151):
    print(basic)

# Multiples of Five - Print all the multiples of 5 from 5 to 1,000
for basic in range(5,1000, 5):
    print(basic)

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for basic in range(1,100,):
    if basic % 10 == 0:
        print("coding dojo")
    elif basic % 5 == 0:
        print("coding")
    else:
        print(basic)

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
final_sum = 0
for basic in range(1, 500000, 2):
    final_sum += basic
print(final_sum)


#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
for basic in range(2018,0,-4):
    print(basic)


#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3
for basic in range(lowNum, highNum+1,):
    if basic % mult == 0:
        print(basic)
