#--------------------------------------------------------------------------------------------------------------------
#Libraries
import matplotlib.pyplot as plt
import random 
#--------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------
#Handmade Functions
def GenerateWithDistributions(numbers,distributions,size):
    
    random_number = random.choices(numbers, weights = (distributions), k=size)
    return random_number
#--------------------------------------------------------------------------------------------------------------------



#--------------------------------------------------------------------------------------------------------------------
#taking inputs
Ordinary_Customers = int(input("Enter the number of ordinary customers to be served: "))
Distinguished_Customers = int(input("Enter the number of Distinguished customers to be served: "))
total_customers = Ordinary_Customers + Distinguished_Customers
x = int(input ("Enter number of tellers(1 or 2): "))
n = int(input("Enter number of runs: "))
print()
#--------------------------------------------------------------------------------------------------------------------



#One Teller
if x == 1:
    for i in range(n):
        print()
    #--------------------------------------------------------------------------------------------------------------------
        #initializing arrays for Ordinary
        Const_time_between_arrivals_O = [0,1,2,3,4,5]
        prob_time_between_arrivals_O = [0.09,0.17,0.27,0.20,0.15,0.12]
        time_between_arrivals_O = GenerateWithDistributions(Const_time_between_arrivals_O,prob_time_between_arrivals_O,Ordinary_Customers)
        time_between_arrivals_O[0] = 0

        Const_service_time_O = [1,2,3,4]
        prob_service_time_O = [0.20,0.40,0.28,0.12]
        service_time_O = GenerateWithDistributions(Const_service_time_O,prob_service_time_O,Ordinary_Customers)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #initializing arrays for Distinguished
        Const_time_between_arrivals_D = [1,2,3,4]
        prob_time_between_arrivals_D = [0.1,0.2,0.3,0.4]
        time_between_arrivals_D = GenerateWithDistributions(Const_time_between_arrivals_D,prob_time_between_arrivals_D,Distinguished_Customers)
        time_between_arrivals_D[0] = 0

        Const_service_time_D = [1,2,3,4]
        prob_service_time_D = [0.10,0.30,0.38,0.22]
        service_time_D = GenerateWithDistributions(Const_service_time_D,prob_service_time_D,Distinguished_Customers)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting average service time of teller
        total_service_time = service_time_D + service_time_O
        average_service_time = sum(total_service_time)/len(total_service_time)
        print ("Average service time of teller: ",average_service_time)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting average waiting time for ordinary queue
        #getting arrival time from minute 0
        arrival_time_O = [0] * Ordinary_Customers

        for i in range(1,Ordinary_Customers):
            arrival_time_O[i] = arrival_time_O[i-1] + time_between_arrivals_O[i]

        #getting waiting time
        waiting_time_O = [0] * Ordinary_Customers

        for i in range(1,Ordinary_Customers):
            waiting_time_O[i] = (arrival_time_O[i-1] + service_time_O[i-1]) - arrival_time_O[i]
            if waiting_time_O[i] < 0:
                waiting_time_O[i] = 0
                
        #Calculating average
        average_waiting_time_O = sum(waiting_time_O)/len(waiting_time_O)
        print("Average waiting time for ordinary customers: ",average_waiting_time_O)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting average waiting time for distinguished queue
        #getting arrival time from minute 0
        arrival_time_D = [0] * Distinguished_Customers

        for i in range(1,Distinguished_Customers):
            arrival_time_D[i] = arrival_time_D[i-1] + time_between_arrivals_D[i]

        #getting waiting time
        waiting_time_D = [0] * Distinguished_Customers

        for i in range(1,Distinguished_Customers):
            waiting_time_D[i] = (arrival_time_D[i-1] + service_time_D[i-1]) - arrival_time_D[i]
            if waiting_time_D[i] < 0:
                waiting_time_D[i] = 0
                
        #Calculating average
        average_waiting_time_D = sum(waiting_time_D)/len(waiting_time_D)
        print("Average waiting time for distinguished customers: ",average_waiting_time_D)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting ordinary maximum queue length
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting distinguished maximum queue length
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting probability of ordinary customer to wait in the queue
        waited_customers_O = 0
        for i in range(Ordinary_Customers):
            if waiting_time_O[i] != 0:
                waited_customers_O += 1
        
        prob_of_waiting_O = waited_customers_O/len(waiting_time_O)
        print("Probability of ordinary customer to wait: ",prob_of_waiting_O)
    #--------------------------------------------------------------------------------------------------------------------

        
        
    #--------------------------------------------------------------------------------------------------------------------
        #getting probability of destinguished customer to wait in the queue
        waited_customers_D = 0
        for i in range(Distinguished_Customers):
            if waiting_time_D[i] != 0:
                waited_customers_D += 1
        
        prob_of_waiting_D = waited_customers_D/len(waiting_time_D)
        print("Probability of distinguished customer to wait: ",prob_of_waiting_D)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting portion of idle time        
        total_arrival_time = [0] *(total_customers)
        total_time_between_arrivals = time_between_arrivals_D + time_between_arrivals_O
        total_waiting_time = waiting_time_D+waiting_time_O
        
        for i in range(1,len(total_arrival_time)):
            total_arrival_time[i] = total_arrival_time[i-1] + total_time_between_arrivals[i]
        
        idle_time = (total_arrival_time[total_customers-1]+total_service_time[total_customers-1]+total_waiting_time[total_customers-1]) - sum(total_service_time)
        
        if idle_time < 0:
            idle_time = 0

        print ("Total time in minutes of teller idility: ",idle_time)
        print ("Portion of teller idility: ",idle_time/(arrival_time_O[Ordinary_Customers-1]+service_time_O[Ordinary_Customers-1]+waiting_time_O[Ordinary_Customers-1]))
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
    #Graphing
    #Frequency of service time ordinary
    plt.hist(service_time_O, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of service time for Ordinary')
    plt.show()
        
    #Frequency of service time Distinguished
    plt.hist(service_time_D, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of service time for Distinguished')
    plt.show()



    #Frequency of inter-arrival time ordinary
    plt.hist(time_between_arrivals_O, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of inter-arrival time for Ordinary')
    plt.show()

    #Frequency of inter-arrival time Distinguished
    plt.hist(time_between_arrivals_D, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of inter-arrival time for Distinguished')
    plt.show()



    #Frequency of waiting time ordinary
    plt.hist(waiting_time_O, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of waiting time for Ordinary')
    plt.show()
        
    #Frequency of waiting time Distinguished
    plt.hist(waiting_time_D, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of waiting time for Distinguished')
    plt.show()
    #--------------------------------------------------------------------------------------------------------------------





#Two Tellers
elif x == 2:
    for i in range(n):
        print()
    #--------------------------------------------------------------------------------------------------------------------
        #initializing arrays for Ordinary
        Const_time_between_arrivals_O = [0,1,2,3,4,5]
        prob_time_between_arrivals_O = [0.09,0.17,0.27,0.20,0.15,0.12]
        time_between_arrivals_O = GenerateWithDistributions(Const_time_between_arrivals_O,prob_time_between_arrivals_O,Ordinary_Customers)
        time_between_arrivals_O[0] = 0

        Const_service_time_O = [1,2,3,4]
        prob_service_time_O = [0.20,0.40,0.28,0.12]
        service_time_O = GenerateWithDistributions(Const_service_time_O,prob_service_time_O,Ordinary_Customers)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #initializing arrays for Distinguished
        Const_time_between_arrivals_D = [1,2,3,4]
        prob_time_between_arrivals_D = [0.1,0.2,0.3,0.4]
        time_between_arrivals_D = GenerateWithDistributions(Const_time_between_arrivals_D,prob_time_between_arrivals_D,Distinguished_Customers)
        time_between_arrivals_D[0] = 0

        Const_service_time_D = [1,2,3,4]
        prob_service_time_D = [0.10,0.30,0.38,0.22]
        service_time_D = GenerateWithDistributions(Const_service_time_D,prob_service_time_D,Distinguished_Customers)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting average service time of teller 1
        average_service_time_T1 = sum(service_time_O)/len(service_time_O)
        print ("Average service time of teller 1: ",average_service_time_T1)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting average service time of teller 2
        average_service_time_T2 = sum(service_time_D)/len(service_time_D)
        print ("Average service time of teller 2: ",average_service_time_T2)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting average waiting time for ordinary queue
        #getting arrival time from minute 0
        arrival_time_O = [0] * Ordinary_Customers

        for i in range(1,Ordinary_Customers):
            arrival_time_O[i] = arrival_time_O[i-1] + time_between_arrivals_O[i]

        #getting waiting time
        waiting_time_O = [0] * Ordinary_Customers

        for i in range(1,Ordinary_Customers):
            waiting_time_O[i] = (arrival_time_O[i-1] + service_time_O[i-1]) - arrival_time_O[i]
            if waiting_time_O[i] < 0:
                waiting_time_O[i] = 0
                
        #Calculating average
        average_waiting_time_O = sum(waiting_time_O)/len(waiting_time_O)
        print("Average waiting time for ordinary customers: ",average_waiting_time_O)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting average waiting time for distinguished queue
        #getting arrival time from minute 0
        arrival_time_D = [0] * Distinguished_Customers

        for i in range(1,Distinguished_Customers):
            arrival_time_D[i] = arrival_time_D[i-1] + time_between_arrivals_D[i]

        #getting waiting time
        waiting_time_D = [0] * Distinguished_Customers

        for i in range(1,Distinguished_Customers):
            waiting_time_D[i] = (arrival_time_D[i-1] + service_time_D[i-1]) - arrival_time_D[i]
            if waiting_time_D[i] < 0:
                waiting_time_D[i] = 0
                
        #Calculating average
        average_waiting_time_D = sum(waiting_time_D)/len(waiting_time_D)
        print("Average waiting time for distinguished customers: ",average_waiting_time_D)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting ordinary maximum queue length
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting distinguished maximum queue length
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting probability of ordinary customer to wait in the queue
        waited_customers_O = 0
        for i in range(Ordinary_Customers):
            if waiting_time_O[i] != 0:
                waited_customers_O += 1
        
        prob_of_waiting_O = waited_customers_O/len(waiting_time_O)
        print("Probability of ordinary customer to wait: ",prob_of_waiting_O)
    #--------------------------------------------------------------------------------------------------------------------

        
        
    #--------------------------------------------------------------------------------------------------------------------
        #getting probability of destinguished customer to wait in the queue
        waited_customers_D = 0
        for i in range(Distinguished_Customers):
            if waiting_time_D[i] != 0:
                waited_customers_D += 1
        
        prob_of_waiting_D = waited_customers_D/len(waiting_time_D)
        print("Probability of distinguished customer to wait: ",prob_of_waiting_D)
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting portion of idle time of T1
        T1_idle_time = (arrival_time_O[Ordinary_Customers-1]+service_time_O[Ordinary_Customers-1]+waiting_time_O[Ordinary_Customers-1]) - sum(service_time_O)
        if T1_idle_time < 0:
            T1_idle_time = 0

        print ("Total time in minutes of T1 idility: ",T1_idle_time)
        print ("Portion of T1 idility: ",T1_idle_time/(arrival_time_O[Ordinary_Customers-1]+service_time_O[Ordinary_Customers-1]+waiting_time_O[Ordinary_Customers-1]))
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
        #getting portion of idle time of T2
        T2_idle_time = (arrival_time_D[Distinguished_Customers-1]+service_time_D[Distinguished_Customers-1]+waiting_time_D[Distinguished_Customers-1]) - sum(service_time_D)
        if T2_idle_time < 0:
            T2_idle_time = 0

        print ("Total time in minutes of T2 idility: ",T2_idle_time)
        print ("Portion of T2 idility: ",T2_idle_time/(arrival_time_D[Distinguished_Customers-1]+service_time_D[Distinguished_Customers-1]+waiting_time_D[Distinguished_Customers-1]))
    #--------------------------------------------------------------------------------------------------------------------



    #--------------------------------------------------------------------------------------------------------------------
    #Graphing
    #Frequency of service time ordinary
    plt.hist(service_time_O, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of service time for Ordinary')
    plt.show()
        
    #Frequency of service time Distinguished
    plt.hist(service_time_D, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of service time for Distinguished')
    plt.show()



    #Frequency of inter-arrival time ordinary
    plt.hist(time_between_arrivals_O, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of inter-arrival time for Ordinary')
    plt.show()

    #Frequency of inter-arrival time Distinguished
    plt.hist(time_between_arrivals_D, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of inter-arrival time for Distinguished')
    plt.show()



    #Frequency of waiting time ordinary
    plt.hist(waiting_time_O, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of waiting time for Ordinary')
    plt.show()
        
    #Frequency of waiting time Distinguished
    plt.hist(waiting_time_D, bins=20)
    plt.xlabel('Minutes')
    plt.ylabel('Customers')
    plt.title('Frequency of waiting time for Distinguished')
    plt.show()
    #--------------------------------------------------------------------------------------------------------------------

    


else:
    print ("wrong input !!!")