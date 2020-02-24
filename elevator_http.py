import sys
import requests
import json
import re
from starlette.applications import Starlette
from starlette.responses import UJSONResponse
import uvicorn
import os
import elevator_server as elev


async def monitorElevator(request):
    returnDict = elev.monitorElevators()
    return UJSONResponse(returnDict)


async def requireElevator(request):
    #print("request:",request)
    body = await request.json()
    #print("RDS http interface received the post body:\n{}\n".format(body))
    #outputJson = rdp.responseDataParser(body)
    #outputDict = json.loads(outputJson)
    elev.receiveRequest(body)
    returnDict = {'status': 'Press button succeeded.', 'monitor elevators': 'Please check monitor API for all elevators status'}
    return UJSONResponse(returnDict)

app = Starlette()
app.add_route("/monitor-elevator", monitorElevator, methods=["GET"])
app.add_route("/require-elevator", requireElevator, methods=["POST"])

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5000)