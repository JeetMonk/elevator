import json
import os

cwd = os.getcwd()

class Elevator(object):

    # Initializes a new Elevator object
    def __init__(self, num_floors, starting_floor, elevator_name):
        # Get name of the elevator
        self.elevator_name = elevator_name        
        # Total number of floors accessible by the elevator
        self.num_floors = num_floors
        # Current floor number
        self.current_floor = starting_floor
        # An unordered set of floor numbers that have been requested
        self.requested_floors = set()
        # An ordered list of floors that have been visited
        self.visited_floors = []
        # Number of floors traveled since the elevator was started
        self.num_floors_traveled = 0
        # moving directiong
        self.moving_direction = 'na'
        self.action = 'idle'
        
    # Registers a request to visit a specific floor
    def request_floor(self, floor):
        self.requested_floors.add(floor)

    # Computes number of floors passed when traveling from the current floor to
    # the given floor (including the given floor itself)
    def get_floor_difference(self, floor):
        #print("floor:",floor)
        return abs(self.current_floor - floor)

    # Travels to the given floor to pick up or drop off passengers
    def visit_floor(self, floor):
        self.num_floors_traveled += self.get_floor_difference(floor)
        self.current_floor = floor
        self.visited_floors.append(self.current_floor)
        
        if self.current_floor in self.requested_floors:
            if self.moving_direction == 'idle' or self.moving_direction == 'going up' or self.moving_direction == 'going down':
                self.moving_direction = 'opening door'
            elif self.moving_direction == 'opening door':
                self.moving_direction = 'load and unload'
            elif self.moving_direction == 'load and unload':
                self.moving_direction = 'closing door'
            else:
                #self.moving_direction = 'idle'
                self.requested_floors.discard(self.current_floor)
                if len(self.requested_floors) != 0:
                    closest_floor = min(self.requested_floors, key=self.get_floor_difference)
                    if self.current_floor > closest_floor:
                        self.moving_direction = 'going down'
                    elif self.current_floor < closest_floor:
                        self.moving_direction = 'going up'
                else:
                    self.moving_direction = 'idle'

    # Starts elevator and travels computed route according to current requests
    def travel(self):
        elevatorDict = {}
        if len(self.requested_floors) != 0:
            closest_floor = min(self.requested_floors, key=self.get_floor_difference)
            #print("closest_floor {}".format(closest_floor))
            if self.current_floor > closest_floor:
                self.moving_direction = 'going down'
                next_floor = self.current_floor - 1
            elif self.current_floor < closest_floor:
                self.moving_direction = 'going up'
                next_floor = self.current_floor + 1
            else:
                next_floor = self.current_floor
            self.visit_floor(next_floor)
        else:
            self.moving_direction = 'idle'
            
        ## for monitor
        if len(self.requested_floors) != 0:
            closest_floor = min(self.requested_floors, key=self.get_floor_difference)
        else:
            closest_floor = None      
        elevatorDict = {'name': self.elevator_name, 'current at floor': self.current_floor, 'action': self.moving_direction, 'moving to floor': closest_floor, 'reuqested floors': list(self.requested_floors)}
        elevatorJson = json.dumps(elevatorDict)
        fe = open(cwd+'/'+self.elevator_name+'.txt','w')
        fe.write(elevatorJson)
        fe.close()
        print(elevatorDict)