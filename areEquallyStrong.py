def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    if yourLeft > yourRight:
        if friendsLeft > friendsRight:
            if friendsLeft == yourLeft and yourRight == friendsRight:
                return True
        elif friendsLeft < friendsRight:
            if friendsRight == yourLeft and yourRight == friendsLeft:
                return True
    elif yourLeft < yourRight:
        if friendsLeft < friendsRight:
            if friendsLeft == yourLeft and yourRight == friendsRight:
                return True
        elif friendsLeft > friendsRight:
            if friendsRight == yourLeft and yourRight == friendsLeft:
                return True
    else:
        if yourLeft == friendsLeft and yourRight == friendsRight:
            return True
    return False
