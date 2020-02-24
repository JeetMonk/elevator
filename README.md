# elevator
Elevator server with API functionality to receive requests (simulate pressing button)


## manual guide

### Running Project.
This project contains mainly two conponents which need to run. <br>
1. Http server <br>
2. Elevator server <br>

#### 1. Start up HTTP server (runs at backend)
> python3 elevator_http.py & <br>

This will start http server and run on localhost. <br>

#### 2. Start elevator server
> python3 elevator_server.py <br>

This will keep displaying status of all three elevators status and populating on the main console. <br>


### Interact with Elevators
After above two conponents started, there are two API's to interact with the elevators. <br>
1. elevator monitor API <br>
2. request elevators API <br> <br>

Postman can be used to call above two API's in order to interact with the elevators. <br>


#### 1. Elevator monitor
GET http://localhost:5000/monitor-elevator <br>

This will receive json data feedback as the status of the three elevators <br>

#### 2. Elevator request
POST http://localhost:5000/require-elevator <br>

body: {"at_floor": 0, "target_floor": 6} <br>

This will simulate "press floor button", i.e. passanger just needs to press which floor he wants to go, then the server will take the rest and assign an elevator for him. <br>

As above API, the passenger is at floor-0 and he wants to go floor-6. <br>
