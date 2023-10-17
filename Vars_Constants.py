# Module
# Description: This module keeps track of variables passing through the modules rather than parameters per module
#
nso_server = {
    'ip': '192.168.101.10',
    'username': 'admin',
    'password': 'admin',
    'port': '8080'
}
headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}
module = "tailf-ncs:devices/"
path = "tailf-ncs:devices/device?fields=name"
path2 = "tailf-ncs:devices/device"
path3 = "tailf-ncs:devices"
path4 = "tailf-ncs:devices/device="
path5 = "tailf-ncs:devices/authgroups"
device_list = "empty"
confirmed = False
ned_list = [{
    'id': 'empty'
}]
authgroup_list = [{
    'name': 'empty'
}]
new_device = {
    'ip': '1.1.1.1',
    'name': 'hostname',
    'authgroup': 'default',
    'ned': 'unknown',
    'protocol': 'telnet'
}
new_authgroup = {
    'groupName': 'NewGroup',
    'remoteName': 'username',
    'password': 'password',
    'secondPassword': ''
}

new_auth = ""
new_ned = ""
new_protocol = ""
delete_name = ""
protocol_list = ["ssh", "telnet"]
auth_pw = "!QAZ2wsx3edc"
auth_username = "NSO"
ned_type = ""
ned_id = ""
