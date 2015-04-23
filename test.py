# Test module

from constants import *

def displayTree(Gid):
    r_API = getChild(str(Gid))
    if r_API[0]: # Did the API exit successfully?
        W = []   # Prepare a list.
        walkOG(r_API[1],Gid,W)  # Order the list of OGs.
    else:
        return(r_API[1])

    bfr = ""
    for r_item in W:
        bfr += printOG(r_item) + '\n'
    return bfr
        
def deleteTree(Gid):
    r_API = getChild(str(Gid))
    if r_API[0]: # Did the API exit successfully?
        W = []   # Prepare a list.
        walkOG(r_API[1],Gid,W)  # Order the list of OGs.
    else:
        print r_API[1]

    # Reverse the order and delete.
    W.reverse()
    for r_item in W:
        testDelete(r_item["Id"]["Value"])

def testDelete(Gid):
    r_API = delete(str(Gid))
    if r_API[0]: # Did the API exit successfully?
        print 'OG Deleted'
    else:
        print r_API[1]

def testAdd(OGid,name,locale,groupID,lgtype):
    r_API = create(str(OGid),name,locale,groupID,lgtype)
    if r_API[0]: # Did the API exit successfully?
        displayTree(OGid)
    else:
        print r_API[1]

#Gid = 1244
#testAdd(OGid=Gid,name='Chesterville',locale='en-US',groupID='cvl',lgtype='Container')
