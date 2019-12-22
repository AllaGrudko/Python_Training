from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, address=None, home_phone=None, mobile_phone=None, work_phone=None,
                 fax=None, email=None, email2=None, email3=None, homepage=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.firstname is None or
                self.firstname == other.firstname) and (self.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize