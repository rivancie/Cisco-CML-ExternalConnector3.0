# This function gets the initial information needed to fill drop-downs and fill in variables used
import Vars_Constants
import requests



def GetList():
    url = f"http://{Vars_Constants.nso_server['ip']}:{Vars_Constants.nso_server['port']}/restconf/data/{Vars_Constants.path}"
    device_url = f"http://{Vars_Constants.nso_server['ip']}:{Vars_Constants.nso_server['port']}/restconf/data/{Vars_Constants.module}"

    ned_url = f"http://{Vars_Constants.nso_server['ip']}:{Vars_Constants.nso_server['port']}/restconf/data/tailf-ncs:devices/ned-ids/ned-id?fields=id"
    authgroup_url = f"http://{Vars_Constants.nso_server['ip']}:{Vars_Constants.nso_server['port']}/restconf/data/tailf-ncs:devices/authgroups/group?fields=name"

    # This section gets the entire device listing active on the NSO instance

    response = requests.get(url, headers=Vars_Constants.headers,
                            auth=(Vars_Constants.nso_server['username'], Vars_Constants.nso_server['password']),
                            verify=False)

    if response.status_code == 200:
        response = requests.get(url, headers=Vars_Constants.headers,
                                auth=(Vars_Constants.nso_server['username'], Vars_Constants.nso_server['password']),
                                verify=False).json()
        Vars_Constants.device_list = response['tailf-ncs:device']

    # This section gets the list of available NEDS on this instance of NSO
    response1 = requests.get(ned_url, headers=Vars_Constants.headers,
                             auth=(Vars_Constants.nso_server['username'], Vars_Constants.nso_server['password']),
                             verify=False).json()
    Vars_Constants.ned_list = response1['tailf-ncs:ned-id']

    # This section gets the list of available AuthGroups on NSO
    response2 = requests.get(authgroup_url, headers=Vars_Constants.headers,
                             auth=(Vars_Constants.nso_server['username'], Vars_Constants.nso_server['password']),
                             verify=False).json()
    Vars_Constants.authgroup_list = response2['tailf-ncs:group']