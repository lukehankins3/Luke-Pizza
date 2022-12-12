# In this program, you will create an instance of a route for flight from 
# Las Vegas to Los Angeles. You will then process the file - reservations.csv
# to process reservations for this flight only. Since the capacity of the flight
# is 190 and there are 191 reservation requests, the last passenger cannot get a
# reservation on the flight. Review flight1.JPG and flight2.JPG to see the first
# two passenger print out information and the last two passengers printout
# information.


import csv
import FlightClass as fc

routes = {
           'Route1':{
                    'flightNo':'1340','RouteName':'DFW to LAX','Seats':210
                    },
            'Route2':{
                    'flightNo':'1189','RouteName':'ATL to DEN','Seats':225
                    },
            'Route3':{
                    'flightNo':'4322','RouteName':'CLT to MCO','Seats':175
                    },
            'Route4':{
                    'flightNo':'3211','RouteName':'LAS to LAX','Seats':190
                    },
            'Route5':{
                    'flightNo':'4355','RouteName':'JFK to IAH','Seats':190
                    },
        }

for n in routes:
        if routes[n]['flightNo'] == 3211:
                route = fc.Route(routes[n]['flightNo'],routes[n]['RouteName'],routes[n]['Seats'])


#open the reservation.csv file in read mode
infile = open('reservations.csv','r')

# create a csv object from the file object from the step above
# and ignore the header row

csvfile = csv.reader(infile,delimiter=',')
next(csvfile)

#use a for loop to iterate through each record in the reservation file

    # check if the flight is 3211. If it is, create a reservation instance. If the flight is full
    # print out the error message as shown in the jpeg picture
    # NOTE: after creating each reservation instance, remember to call the update seat count method to
    # reduce the number of available seats by 1

for record in csvfile:
        if record[1] == 3211:
                route = fc.Reservation(record)
                if route.get_status() == True:
                        route.update_seat_count()
                        print("Passenger Name:" + route.get_name())
                        print("Passenger Class:" + route.get_class())
                        print("Passenger Seat No.:" + route.get_seatno())
                else:
                        print("*********ERROR**********")
                        print("Passenger Name:" + route.get_name())
                        print("unable to complete reservation, flight is full")
                        print("************************")



    # Print out the name, class and seat number for each passenger as shown in the pic flights1.JPG
    
    


