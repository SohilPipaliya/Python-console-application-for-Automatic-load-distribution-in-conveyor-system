# Console-application-for-Automatic-load-distribution-in-conveyor-system
This is my first try to make small console application in Python to build following logic:

Here how it goes:
1) A user firstly is requested to set up the number of available destinations (0-n) 
2) A user then is requested to set up the destination selection strategy (one of the following 2)  
    o   Round robin (1,2,3,..n, 1,2,3,…,n , … ) 
    o   Random (select a destination randomly with the same probability weight for destination)  
3) A user then is requested to choose the number of consecutive loads that upon arrival to decision point must get the same destination selected.
4) A user then is requested to choose a percentage of failure for load to be diverted into its destination.
5) A user finally is requested to choose the number of loads, that the application should select a destination for.
6) Afterwards the console should print out all the reached destination numbers according to the input specified by user, and print out for every destination number the percentage of loads that have reached it.
