from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, ControlNumber

class AccountTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user('user', email="6574657547", password="Aryaa,,,34343")
        self.control_number = ControlNumber('2090039469', False)
        self.control_number.save()
    
    def link_user_profile(self):
        profile = Profile.objects.create(user_id=self.user1.id)
        profile.phone="1234567891"
        profile.gender="M"
        profile.first_last_name="javi"
        profile.control_number_id=self.control_number
        profile.birthday="2020-01-19"
        profile.semester="4"
        profile.save()

        ControlNumber.objects.filter(pk=profile.control_number_id).update(
                is_active=True
        )
