from ncclient import manager


router = {"host": "ios-xe-mgmt-latest.cisco.com", "port": "10000", 
          "username": "developer", "password": #(your_password_goes_here)
         }

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()



