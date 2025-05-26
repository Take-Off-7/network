from ncclient import manager


router = {"host": "sbx-nxos-mgmt.cisco.com", "port": "22", "username": "admin", "password": #(your_password_goes_here)
         }

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print('*' * 50)
        print(capability)
    m.close_session()


