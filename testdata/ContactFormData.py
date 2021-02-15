class ContactFormData:
    test_bad_contact_form_data = [{
        "first_name": "test",
        "last_name": "test",
        "email": "t@t.tcom",
        "phone_number": "XXXX-XXXX",
        "website_url": "xxx.rixxo.test",
        "message": "testing test",
    }]

    test_good_contact_form_data = [{
        "first_name": "test",
        "last_name": "test",
        "email": "t@t.tcom",
        "phone_number": "XXXX-XXXX",
        "website_url": "xxx.rixxo.test",
        "message": "testing test",
    }]

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
            "email": "t@t.tcom",
            "phone_number": "XXXX-XXXX",
            "website_url": "xxx.rixxo.test",
            "message": "testing test",
        }]
