#creating two lists - one for each club
extravenza = []
tez = []

#taking in student ids in the list

extravenza = [1,2,3,5]
tez = [2,8,9]

#joining all ids in another list

all_students = extravenza + tez

#removing duplicates from the student list

all_students = list(set(all_students))

#print number of students who participated in at least one club

print(len(all_students))