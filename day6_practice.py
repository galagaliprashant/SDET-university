import json
import yaml

#now i am wrirting the human readable yaml format

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

print(type(yaml_string))

#now i am printing the human readabel
print(yaml_string)

#now i am converting the Yaml to python (desrialisation)

python_dict = yaml.safe_load(yaml_string)
print(python_dict)

router_config = python_dict['router']
print(type(router_config))

json_payload = json.dumps(router_config, indent=4)
print(json_payload)
print(type(json_payload))

