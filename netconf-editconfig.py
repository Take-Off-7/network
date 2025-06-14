from ncclient import manager
from router_info import router


config_template = open("/Users/Opeyemi/Network/ios_config.xml").read()

netconf_config = config_template.format(interface_name = "GigabitEthernet2", interface_desc = "TakeOff was here")

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"]) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)



