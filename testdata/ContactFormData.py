

# use @dataclass ?
from testdata.TestUser import TestUser


class ContactFormData:

    user = TestUser()

    test_contact_form_data = [
        {
            "type": "good",
            "first_name": "test",
            "last_name": "test",
            "email": "t@t.tcom",
            "phone_number": "XXXX-XXXX",
            "website_url": "xxx.rixxo.test",
            "message": "testing test",
        },
        {
            "type": "bad",
            "first_name": "test",
            "last_name": "test",
            "email": "t@t",
            "phone_number": "XXX",
            "website_url": "xxx.rixxo.test",
            "message": "testing test",
        },
        {
            "type": "empty",
            "first_name": "",
            "last_name": "",
            "email": "",
            "phone_number": "",
            "website_url": "",
            "message": "",
        },
        {
            "type": "good_data_dont_test_yet",
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "phone_number": user.phone_number,
            "website_url": user.website,
            "message": user.message,
        }
    ]
