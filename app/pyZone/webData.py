from flask import Markup

def getTicker(user):
    pass

def getNav(role):
    if (role == "Admin"):
        navr =  Markup('<nav><ul><li class="active"><a href="#">Home</a></li><li><a href="#">Client</a></li><li><a href="#">Users</a></li><li><a href="#">Brief</a> </li><li><a href="#">Jobs</a></li><li><a href="#">Tasks</a></li><li><a href="#">Contact</a></li><li><a href="#">About</a></li>')
    if (role == "Manager"):
        navr =  Markup('<nav><ul><li class="active"><a href="#">Home</a></li></li><li><a href="#">Brief</a> </li><li><a href="#">Jobs</a></li><li><a href="#">Tasks</a></li><li><a href="#">Contact</a></li><li><a href="#">About</a></li>')
    if (role == "Project"):
        navr =  Markup('<nav><ul><li class="active"><a href="#">Home</a></li><li><a href="#">Jobs</a></li><li><a href="#">Tasks</a></li><li><a href="#">Contact</a></li><li><a href="#">About</a></li>')
    if (role == "Worker"):
        navr =  Markup('<nav><ul><li class="active"><a href="#">Home</a></li><li><a href="#">Tasks</a></li><li><a href="#">Contact</a></li><li><a href="#">About</a></li>')
    if (role == "Admin"):
        navr =  Markup('<nav><ul><li class="active"><a href="#">Home</a></li><li><a href="#">Client</a></li><li><a href="#">Users</a></li><li><a href="#">Brief</a> </li><li><a href="#">Jobs</a></li><li><a href="#">Tasks</a></li><li><a href="#">Contact</a></li><li><a href="#">About</a></li>')
    return navr

def getlatest(user):
    pass

def getlisting(user):
    pass

def getStats(user):
    return [3,6,8,7,9]

def getRprt(user):
    return [5,4,4,7,4]


def getPageDetail(usr, rle):
    nav = getNav(rle)
    topBlock = getlatest(usr)
    botBlock = getlisting(usr)
    stats = getStats(usr)
    rprt = getRprt(usr)
    ticker = getTicker(usr)
    return [nav, topBlock, botBlock, stats, rprt, ticker ]