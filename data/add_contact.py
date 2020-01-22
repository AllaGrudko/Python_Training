from model.contact import Contact
import random
import string

constant = [
    Contact (firstname="firstname1", lastname="lastname1", address="address1", home_phone="home_phone1",
             mobile_phone="mobile_phone1", work_phone="work_phone1", fax="fax1", email="email1", email2="email21",
             email3="email31", homepage="homepage1"),
    Contact (firstname="firstname2", lastname="lastname2", address="address2", home_phone="home_phone2",
             mobile_phone="mobile_phone2", work_phone="work_phone2", fax="fax2", email="email2", email2="email22",
             email3="email32", homepage="homepage2")
]

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", address="", home_phone="", mobile_phone="", work_phone="", fax="",
                    email="", email2="", email3="", homepage="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            address=random_string("address", 10), home_phone=random_string("home_phone", 10),
            mobile_phone=random_string("mobile_phone", 10), work_phone=random_string("work_phone", 10),
            fax=random_string("fax", 10), email=random_string("email", 10), email2=random_string("email2", 10),
            email3=random_string("email3", 10), homepage=random_string("homepage", 10))
    for i in range(2)
]
