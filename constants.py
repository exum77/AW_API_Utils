# Constant values for the API

import requests, json

HOST = 'https://as420.awmdm.com'
APIKEY = 'A8qzeuhVSLgphAUde2X6Pe+s/Ogi3fNOR69KkMApqTU='
USER = 'ATLANTAWIFI\TExum'
PSWD = 'J$1jolly'
CONTENT = 'application/json'
SECURITYPIN = '1111'

HEAD = {'aw-tenant-code': APIKEY, 'content-type': CONTENT}
PAYLOAD = {'SecurityPIN': SECURITYPIN}

# OG - Implement getchild from AW API
def getChild(parentID):
    url = HOST + '/API/v1/system/groups/' + parentID + '/getchild'
    r = requests.get(url,headers=HEAD,auth=(USER,PSWD))
    # Look for success
    if r.status_code == 200:
        children = r.json()
        return True,children
    else:
    # Anything other than 200 we fail out and display error text    
        return False,r.text

# OG - Implement create from API
def create(OGid,name,locale,groupID,lgtype):
    url = HOST + '/API/v1/system/groups/' + OGid + '/creategroup'
    payload = PAYLOAD.copy()
    payload["Name"] = name
    payload["Locale"] = locale
    payload["LocationGroupType"] = lgtype
    payload["GroupID"] = groupID
    r = requests.post(url,headers=HEAD,data=json.dumps(payload),auth=(USER,PSWD))
    # Look for success
    if r.status_code == 200:
        return True,r.text
    else:
    # Anything other than 200 we fail out and display error text    
        return False,r.text    

# OG - Implement delete from API
def delete(OGid):
    url = HOST + '/API/v1/system/groups/' + OGid + '/delete'
    r = requests.delete(url,headers=HEAD,data=json.dumps(PAYLOAD),auth=(USER,PSWD))
    # Look for success
    if r.status_code == 200:
        return True,r.text
    else:
    # Anything other than 200 we fail out and display error text    
        return False,r.text    

# Display all OG information. Indent to represent nested OGs.
def printOG(r_item):
    tabs = 0
    if r_item.has_key("LgLevel"):
        tabs = int(r_item["LgLevel"])
    return tabs * '  ' + r_item["Name"] + ' - u' + r_item["Users"] + ' a' + r_item["Admins"] + ' d' + r_item["Devices"] + ' ' + str(r_item["Id"]["Value"])

# Use recursion to walk the OGs. Return ordered list of ordered OGs.
def walkOG(r,OGid,W):
    for r_item in r:
        if r_item["Id"]["Value"] == OGid:
            W.append(r_item)
        if r_item.has_key("ParentLocationGroup"):
            Pid = r_item["ParentLocationGroup"]["Id"]["Value"]
            if Pid == OGid:
                walkOG(r,r_item["Id"]["Value"],W)
