import pytest
import os
from validate_request import ValidateRequest

class TestValidation:
    def setup(self):
        self.data_1 = {
            "phone_number": "2056023104",
            "message": "Hello!",
            "sms_token": os.environ['SMS_TOKEN']
        }

        self.data_2 = {
            "phone_number": "2056023104",
            "message": "Hello!",
            "sms_token": 'lol'
        }

        self.validation = ValidateRequest()

    def test_run(self):
        assert self.validation.run(self.data_1)
        assert not self.validation.run(self.data_2)

    def test_valid_keys(self):
        assert self.validation.valid_keys(['phone_number', 'message', 'sms_token'])
        assert not self.validation.valid_keys(['name', 'text_message', 'lol'])

    def test_valid_phone_number(self):
        assert self.validation.valid_phone_number('3034345603')
        assert not self.validation.valid_phone_number('3034sdf603')
        assert not self.validation.valid_phone_number('30343456033')
        assert not self.validation.valid_phone_number('')

    def test_valid_token(self):
        assert self.validation.valid_token(os.environ['SMS_TOKEN'])
        assert not self.validation.valid_token('sa;dlkgjasl;dfj3409')

    def test_valid_message(self):
        assert self.validation.valid_message('Hello')
        assert not self.validation.valid_message('')
