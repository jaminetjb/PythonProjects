# This program takes in a text file made from a text based form of the VCU Online Transcrit and calculates one's science GPA


# File Format:
# The file should have the following 3 line format
# Line 1: <Course Department Code>  <course number> <Course title>  <Letter Grade>
# Line 2: <Number of credits the course was>
# Line 3: <Quality points from the course i.e. (letter gradee value)*(number of credits)

# Goal of the code is to have total number of credits in the denominator and the total number of quality points in the numberator
# That way, if someone has completed A's in all courses, then the results will be 4.0

transcipt = open('scienceGPA.txt', 'r')

qp = 0 #quality points
cred = 0 #credits
counter = 0

for line in transcipt:

    counter = counter + 1
    if counter == 4:
        counter = 1

    if counter == 2:
        cred = cred + float(line)
    if counter == 3:
        qp = qp + float(line)

gpa = qp / cred

print "Your science GPA is ", gpa