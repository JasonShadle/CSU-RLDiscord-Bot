class Roles:
    def __init__(self, message):
        # change this if need a different path
        self.fileName = "roles.txt"
        self.user = message.author
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
                    if ((str(line)).lower() == (str(self.roleString)).lower() and (str(line)).lower() == str(role.name).lower()):
                        exists = True
                        self.role = role
                        if role in self.user.roles:
                            self.hasRole = True
        if (not exists):
            self.error = True            
        else:
            return(self.role)

    def toggle(self, name):
        delete = False
        with open(self.fileName,'r') as file:
            for line in file:
                line = line.splitlines()[0]
                if name == line:
                    delete = True
        # deleting from the file
        if delete:
            # read file because 'w' will clear it
            infile = open(self.fileName, 'r').readlines()
            with open(self.fileName, 'w') as outfile:
                for line in infile:
                    if name != line.splitlines()[0]:
                        outfile.write(line)
        # writing to file
        else:
            with open(self.fileName, 'a') as file:
                file.write(name + '\n')
        return delete
    def getHasRole(self):
        return self.hasRole
    
    def getError(self):
        return self.error

    def getRole(self):
        return self.role