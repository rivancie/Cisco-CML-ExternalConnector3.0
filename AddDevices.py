# This module creates a separate pop up input box for adding devices into NSO inventory

import GetDeviceList
import requests
import json
import Vars_Constants
from tkinter import *
import ast
import GlobalVar

GV = GlobalVar
V = Vars_Constants

def findNED():
    for ned in V.ned_list:
        if V.ned_type in str(ned):
            V.ned_id = str(ned['id'])
    print(V.ned_id)

def addDevice():
    # This function gets the user input items for adding devices and making the restconf call to NSO


    findNED()
    V.new_ned = V.ned_id
    V.new_device['name'] = GV.global_node_hostname
    V.new_device['ip'] = str(GV.global_node_address)
    V.new_device['ned'] = V.ned_id
    V.new_device['authgroup'] = V.new_auth['name']
    V.new_device['protocol'] = "telnet"
    V.confirmed = TRUE

    device_payload = {
        'device': {
            'name': V.new_device['name'],
            'address': V.new_device['ip'],
            'authgroup': V.new_device['authgroup'],
            'device-type': {
                'cli': {
                    'ned-id': V.new_device['ned'],
                    "protocol": V.new_device['protocol']
                }
            },
            'state': {
                'admin-state': 'unlocked'
            }
        }
    }
    print(device_payload)
    # Send the POST request to add the device to NSO
    add_device_url = f"http://{Vars_Constants.nso_server['ip']}:{Vars_Constants.nso_server['port']}/restconf/data/{Vars_Constants.path3}"
    print(add_device_url)
    response = requests.post(f'{add_device_url}', headers=Vars_Constants.headers,
                                auth=(Vars_Constants.nso_server['username'], Vars_Constants.nso_server['password']),
                                data=json.dumps(device_payload), verify=False)
    # Check the response status code
    if response.status_code == 201:
        print(f"Device '{Vars_Constants.new_device['name']}' added successfully to NSO.")
        GetDeviceList.GetList()
    else:
        print(f"Error: Unable to add device to NSO. Status code: {response.status_code}")