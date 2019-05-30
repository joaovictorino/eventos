class AccountIntegration():
    def validateLogin(self, userIdentification, token):
        pass
        
    def getAccountInfo(self, userIdentification):
        passz
        

class AccountInfo(object):
    def __init__(self, uid, name, email, profilePic, extra = None):
        self.uid = uid
        self.name = name
        self.email = email
        self.profilePic = profilePic
        self.extra = extra
