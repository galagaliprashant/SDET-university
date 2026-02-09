import json 
import yaml 

#human written YAML code 
yaml_string = """
router:
  hostname: Nokia_SR_7750
  ip_address: 10.0.0.1
  interfaces:
    - eth0
    - eth1
    - eth2
  is_active: true
"""

#convert this YAML to python dictionary 
config_data = yaml.safe_load(yaml_string)
print(json.dumps(config_data, indent=4)) # here i am priting the python dictionary in json format 

#now i am converting the python dictionary to json


