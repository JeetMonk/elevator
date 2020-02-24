import os
import json
import time
from elevator_class import Elevator

cwd = os.getcwd()
open(cwd+'/A.txt', 'a').close()
open(cwd+'/B.txt', 'a').close()
open(cwd+'/C.txt', 'a').close()
open(cwd+'/reqeust.txt', 'a').close()

################################# FUNCTIONS #################################


def initialElevatorFile(elevatorObject):
    outputDict = {'name': elevatorObject.elevator_name, 'current at floor': elevatorObject.current_floor, 'action': 'idle', 'moving to floor': None, 'reuqested floors': []}
    outputJson = json.dumps(outputDict)
    fe = open(cwd+'/'+elevatorObject.elevator_name+'.txt','w')
    fe.write(outputJson)
    fe.close()
    return


def elevatorCurrentStatus(fileNameFullPath):
    fe = open(fileNameFullPath,'r')
    contents = fe.read()
    fe.close()
    return json.loads(contents)


def monitorElevators():
    elevator_monitor = {'elevators': []}
    elevator_monitor['elevators'].append(elevatorCurrentStatus(cwd+'/A.txt'))
    elevator_monitor['elevators'].append(elevatorCurrentStatus(cwd+'/B.txt'))
    elevator_monitor['elevators'].append(elevatorCurrentStatus(cwd+'/C.txt'))
    #for item in elevator_monitor:
    #print(item)
    return elevator_monitor


def receiveRequest(input_reqeust):
    print("Received input request: {}".format(input_reqeust))
    fp = open(cwd+'/reqeust.txt','a+')
    fp.write(json.dumps(input_reqeust)+"\n")
    fp.close()
    return


def weightCandidate(elevatorObject, at_floor, reqeusted_direction):
    candidateWeight = 0
    if elevatorObject.moving_direction == 'idle':
        candidateWeight += 1
    if elevatorObject.current_floor == 0:
        candidateWeight += 1
    if elevatorObject.current_floor <= at_floor:
        candidateWeight += 1
    if elevatorObject.current_floor == at_floor:
        candidateWeight += 1
    if elevatorObject.moving_direction == reqeusted_direction:
        candidateWeight += 1
    if elevatorObject.moving_direction == reqeusted_direction and reqeusted_direction == 'going up' and elevatorObject.current_floor <= at_floor:
        candidateWeight += 10
    if elevatorObject.moving_direction == reqeusted_direction and reqeusted_direction == 'going down' and elevatorObject.current_floor >= at_floor:
        candidateWeight += 10
    if elevatorObject.moving_direction != reqeusted_direction and reqeusted_direction == 'going down' and elevatorObject.current_floor > at_floor:
        candidateWeight += 1
    if elevatorObject.moving_direction != reqeusted_direction and reqeusted_direction == 'going up' and elevatorObject.current_floor < at_floor:
        candidateWeight += 1
    return candidateWeight


def assignTaks(line):
    reqeusted_direction = 'going up' if line['at_floor'] < line['target_floor'] else 'going down' if line['at_floor'] > line['target_floor'] else 'idle'
    weightA = weightCandidate(elevatorA, line['at_floor'], reqeusted_direction)
    weightB = weightCandidate(elevatorB, line['at_floor'], reqeusted_direction)
    weightC = weightCandidate(elevatorC, line['at_floor'], reqeusted_direction)
    if weightA >= weightB and weightA >= weightC:
        elevatorA.request_floor(line['at_floor'])
        elevatorA.request_floor(line['target_floor'])
    elif weightB > weightA and weightB >= weightC:
        elevatorB.request_floor(line['at_floor'])
        elevatorB.request_floor(line['target_floor'])
    else:
        elevatorC.request_floor(line['at_floor'])
        elevatorC.request_floor(line['target_floor'])
    return


if __name__ == '__main__':
    ## build elevators
    elevatorA = Elevator(num_floors=9, starting_floor=0, elevator_name='A')
    initialElevatorFile(elevatorA)
    elevatorB = Elevator(num_floors=9, starting_floor=0, elevator_name='B')
    initialElevatorFile(elevatorB)
    elevatorC = Elevator(num_floors=9, starting_floor=0, elevator_name='C')
    initialElevatorFile(elevatorC)

    while True:
        print()
        time.sleep(2)
        ## read reqeust and assign tasks
        rqeusted_lines = open(cwd+'/reqeust.txt','r').readlines()
        for line in rqeusted_lines[::-1]: # process lines in reverse order
            print("line:", line)
            assignTaks(json.loads(line))
            del rqeusted_lines[-1]  # remove the [last] line
        open(cwd+'/reqeust.txt', 'w').writelines(rqeusted_lines)

        ## operating elevators
        elevatorA.travel()
        elevatorB.travel()
        elevatorC.travel()