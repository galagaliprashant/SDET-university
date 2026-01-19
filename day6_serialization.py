import json 
import yaml 

#now i include the network configuration in python dictionary
router_config = {
    "hostname": "Nokia_SR_7750",
    "ip_address": "10.0.0.1",
    "interfaces": ["eth0", "eth1", "eth2"],
    "is_active": True
}

# now i want to convert this python dictionary to json and i converted python only readable to universal readable format
json_payload = json.dumps(router_config, indent=4)
print(json_payload) 
