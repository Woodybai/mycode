class Employee:
    def __init__(self, lastname, firstname=None):
        self.lastname = lastname
        self.firstname = firstname

    def __str__(self):
        if self.firstname:
            return "%s %s" % (self.firstname, self.lastname)
        else:
            return self.lastname
