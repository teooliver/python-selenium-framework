from mimesis import Person, Address, Text


# how to generate valid and invalid fields?
class TestUser:
    person = Person()
    address = Address()
    text = Text()

    username = person.username()
    first_name = person.first_name()
    last_name = person.last_name()
    email = person.email()
    fake_address = address.address()
    password = person.password()
    website = "www.xxxxxxxx.com"
    phone_number = person.telephone()
    message = text.sentence()


test_user = TestUser()
test_user2 = TestUser()