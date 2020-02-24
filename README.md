# elevator
Elevator server with API functionality to receive requests (simulate pressing button)


## manual guide

### Running Project.
This project contains mainly two conponents which need to run.
    1. Http server
    2. Elevator server

#### 1. Start up HTTP server (runs at backend)
> python3 elevator_http.py &
This will start http server and run on localhost.

#### 2. Start elevator server
> python3 elevator_server.py
This will keep displaying status of all three elevators status and populating on the main console.


### Interact with Elevators
After above two conponents started, there are two API's to interact with the elevators.
    1. elevator monitor API
    2. request elevators API

Postman can be used to call above two API's in order to interact with the elevators


#### 1. Elevator monitor
> GET http://localhost:5000/monitor-elevator
This will receive json data feedback as the status of the three elevators

#### 2. Elevator request
> POST http://localhost:5000/require-elevator
  body: {"at_floor": 0, "target_floor": 6}
This will simulate "press floor button", i.e. passanger just needs to press which floor he wants to go, then the server will take the rest and assign an elevator for him.
As above API, the passenger is at floor-0 and he wants to go floor-6.
