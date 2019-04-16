
class Roles:
    def __init__(self, message, client):
        # change this if need a different path
        self.fileName = "roles.txt"
        self.message = message
        self.client = client
        self.user = message.author
        self.id = message.author.id
        self.userPerms = message.author.guild_permissions
        self.role = ''
        self.roleString = message.content.split(' ')[1]
        self.error = False
        self.hasRole = False
        self.checkRole()

    def checkRole(self):
        exists = False
        with open(self.fileName,'r') as file:
            # loop every line in the file
            for line in file:
                line = line.splitlines()[0]
                # loop through all permissions of the server
                for role in self.user.guild.roles:
                    # if the names are equal
                    # TODO: try to do if (line in role)
                    if (str(line)).lower() == (str(role.name)).lower():
                        exists = True
                        self.role = role
                        if role in self.user.roles:
                            self.hasRole = True
        if (not exists):
            self.error = True            
        else:
            return(self.role)

    def checkError(self):
        return self.error

    def getHasRole(self):
        return self.hasRole
    
    def getError(self):
        return self.error

    def getRole(self):
        return self.role
