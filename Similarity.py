import numpy as np
values_the_same = False
totalmultiplier = 0
between = False
exactly = False

#subject we want to classify
subject = input("enter the name of the test subject")

#number of training data entries:
num = int(input("how many data entries would you like to make?"))
#array to store training data
data = [[None]*2 for i in range(num)]
#ratios of training data:
multipliers = [[None] for i in range(num)]

#input for num number of training data values:
for i in range(0, num):
    #2 features for each data input:
    value = float(input("enter first value of subject " + str(i + 1)))
    valuetwo = float(input("enter secondvalue of subject " + str(i + 1)))
    #store feature values in 2d array:
    data[i][0] = value
    data[i][1] = valuetwo
    currentvalueone = data[i][0]
    currentvaluetwo = data[i][1]
    #this is the ratio between the two current features it describes the realtionship between the two features:
    currentmultiplier = currentvalueone / currentvaluetwo
    #store ratios in array
    multipliers[i] = currentmultiplier

#list ratios in order of size
multipliers.sort()

#array to store percentiles of ratios
percentiles = [None]*101


for i in range(101):
    percentiles[i] = np.percentile(multipliers, (i)*1)

def enter():
    #enter feature values for unlabeled data
    first = float(input("enter first value"))
    second = float(input("enter second value"))
    #ratio for unlabeled data
    m = first / second    

    similarity = 0
    similarityl = 0
    similarityu = 0
    percentile = 0
    percentilel = 0
    percentileu = 0
    
    global percentiles
    
    #find correct percentile range:
    for i in range(101):
        #decision tree:
        if i != 101:
                if m >= percentiles[i] and m <= percentiles[i + 1] :
                    percentilel = i*1
                    percentileu = (i + 1)*1
                    if i*1 <= 50 and (i+1)*1 <= 50:
                        similarityl = 100 - (50 - ((i)*1))
                        similarityu = 100 - (50 - ((i+1)*1))
                    if i*1 >= 50 and (i + 1)*10 >= 50:
                        similarityl = 100 - (((i)*1) - 50)
                        similarityu = 100 - (((i + 1)*1) - 50)
                if m == percentiles[i]:
                    percentile = i
                    if i != 0 or i != 100:
                        if i*1 <= 50:
                            similarity = 100 - (50 - (i*1))
                        if i*1 >= 50:
                            similarity = 100 - ((i*1) - 50)  
                    if i == 0 or i == 100:
                        similarity = 100
                
              
    print(str((similarityl + similarityu)/2) + "% similarity to a " + subject)

    enter()

enter()




        
