# CiscoCMLExternalConnector3.0
This program allows a user to connect to an existing lab in Cisco Modeling Labs and adds the ability for the nested virtual routers and switches to connect to the external network of the CML server whether its physical or virtual.  In order for this functionality to be successful, the underlying physical network of the CML server needs to be pre-configured.  This program will build the specific configs per device and append those configs to the start config file of the device; thus, requiring the lab to be halted in order to append the configs.  The user can optionally add the backend management devices to the existing lab in order to connect externally rather than manually add. Option1 which leverages the default pre-built bridge0 adapter will allow the inside devices to connect to the same subnet as the CML server -- user must ensure that the addressing range provided does not conflict with the DHCP/local subnet of the CML server.  Option2 leverages a user created bridge adapter within CentOS -- user must ensure that the addressing range provided does not conflict with the DHCP/local subnet of the specified VLAN.  Additionally, the bridge adapters can be configured to support 802.1q tagging and specific VLAN number to assign.  This can be useful to leverage a single dedicated NIC on the CML server to support multiple VLANs.

Enhancements as of SEP2023
- added optional Cisco NSO auto onboarding in config updates workflow
- added DHCP addressing option versus static addressing

# NOTE
MAC OS seems to have uncovered a bug in Tkinter GUI drop down.  Work in progress.
