#stting up number of available state
from random import randint

print ( '''
Note :Please note that you can only chose max. of 6 station if you want to distribute your orders randomly,
    if you try to chose more than 6 station for Random distribution, it will be automatically taken as 6
    for Round Robin you can chose as many as station you want
        ''')

nStation  = int(input("Please Enter the number of staiton available to be delivered: "))
print (
'''Please Select one of the following Strategy for order distribution: : 
    Enter 1 for Round Robin 
    Enter 2 for Random selection''')
strategy = int(input("Please enter: "))
nConsecutiveLoadToSameStation = int(input("Please enter the no. of consecutive order that must be enrouted to same station :  "))
failurePercentagOfDelivery = float(input("Please enter the failure percentage for orders which will be failed to directed to it's destination :  "))
nOrder = int(input("Please enter the number of total orders/load for this simulation run : "))
stationNumber = 1

#for failure
totalOrderDelivered = 0
ordersFailed = 0

#for data storage
listOrderDistributedPerStation = []
for i in range(nStation):
    listOrderDistributedPerStation.append(0)

#for random strategy
avgOrderPerStation = (nOrder / nStation)
dictRandomOrderDistributedPerStation = {}
if nStation <= 6:
    for i in range(nStation):
        dictRandomOrderDistributedPerStation.setdefault("Station"+str(i+1),0)
else:
    for i in range(6):
        dictRandomOrderDistributedPerStation.setdefault("Station"+str(i+1),0)

i=1
while i < (nOrder+1):
    #round robin
    if strategy == 1 :
        if i < (nOrder - nConsecutiveLoadToSameStation):
            totalOrderPerStation = listOrderDistributedPerStation[stationNumber - 1]
            totalOrderPerStation += nConsecutiveLoadToSameStation
            listOrderDistributedPerStation[stationNumber - 1] = totalOrderPerStation
            #update station number
            if stationNumber < nStation:
                stationNumber += 1
            else:
                stationNumber = 1
            #skipping these many orders as they are already assigned
            i += nConsecutiveLoadToSameStation
        else:
            totalOrderPerStation = listOrderDistributedPerStation[stationNumber - 1]
            totalOrderPerStation += (nOrder + 1 - i)
            listOrderDistributedPerStation[stationNumber - 1] = totalOrderPerStation
            break

    else: #random selection
        if nStation <= 6:
            destinationCenter = randint(1,nStation)
        else:
            destinationCenter = randint(1,6)
        if destinationCenter == 1 and dictRandomOrderDistributedPerStation["Station1"]<avgOrderPerStation :
                 dictRandomOrderDistributedPerStation["Station1"]+=1
                 #code to send to randomly chosen destination center
        elif destinationCenter == 2 and dictRandomOrderDistributedPerStation["Station2"]<avgOrderPerStation :
                 dictRandomOrderDistributedPerStation["Station2"]+=1
        elif destinationCenter == 3 and dictRandomOrderDistributedPerStation["Station3"]<avgOrderPerStation :
                 dictRandomOrderDistributedPerStation["Station3"]+=1
        elif destinationCenter == 4 and dictRandomOrderDistributedPerStation["Station4"]<avgOrderPerStation :
                 dictRandomOrderDistributedPerStation["Station4"]+=1
        elif destinationCenter == 5 and dictRandomOrderDistributedPerStation["Station5"]<avgOrderPerStation :
                 dictRandomOrderDistributedPerStation["Station5"]+=1
        elif destinationCenter == 6 and dictRandomOrderDistributedPerStation["Station6"]<avgOrderPerStation :
                 dictRandomOrderDistributedPerStation["Station6"]+=1
        i += 1

print('''
Result : 
''')

# Failure calculation
if strategy == 1:
        for i in range(len(listOrderDistributedPerStation)):
            # converting % into number
            failedDeliveryNo = listOrderDistributedPerStation[i] * (failurePercentagOfDelivery / 100)
            if failedDeliveryNo >= 1:
                sucessfulDeliveryNo = listOrderDistributedPerStation[i] - int(failedDeliveryNo)
                listOrderDistributedPerStation[i] = sucessfulDeliveryNo
                ordersFailed += int(failedDeliveryNo)
            totalOrderDelivered += listOrderDistributedPerStation[i]
            percentageWiseDelievry = float(listOrderDistributedPerStation[i] / nOrder) * 100
            print(
                "StationNumber" + str(i + 1) + " got " + "%.2f percent of total orders" % percentageWiseDelievry)
else:
        for i in range(len(dictRandomOrderDistributedPerStation)):
            # converting % into number
            failedDeliveryNo = dictRandomOrderDistributedPerStation["Station"+str(i+1)] * (failurePercentagOfDelivery / 100)
            if failedDeliveryNo >= 1:
                sucessfulDeliveryNo = dictRandomOrderDistributedPerStation["Station"+str(i+1)] - int(failedDeliveryNo)
                dictRandomOrderDistributedPerStation["Station"+str(i+1)] = sucessfulDeliveryNo
                ordersFailed += int(failedDeliveryNo)
            totalOrderDelivered += dictRandomOrderDistributedPerStation["Station"+str(i+1)]
            percentageWiseDelievry = float(dictRandomOrderDistributedPerStation["Station"+str(i+1)] / nOrder) * 100
            print("StationNumber" + str(i + 1) + " got " + "%.2f percent of total orders" % percentageWiseDelievry)

print(""
      "Total no. of Orders successfully delivered : "+ str(totalOrderDelivered))
print(""
      "Total no. of Orders failed to get delivered : "+ str(ordersFailed))