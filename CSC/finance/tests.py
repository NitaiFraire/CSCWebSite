from django.test import TestCase
from django.contrib.auth.models import User
from finance.models import Total, Entry, Egress

class FinanceTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="niga", email=None, password=None)
        self.total = Total(total=1000.00)
        self.total.save()
    
    def test_add_amount_to_total(self):
        total = Total.objects.filter(pk=self.total.id).values('total')
        print(f"Total inicial: {total[0]['total']}")

        self.entry = Entry.objects.create(
            user_id=self.user1,
            amount=250.99,
            description="Test"
        )

        totalFinal = Total.objects.filter(pk=self.total.id).values('total')
        print(f"Total final: {totalFinal[0]['total']}")

    def test_substract_amount_to_total(self):
        total = Total.objects.filter(pk=self.total.id).values('total')
        print(f"Total inicial: {total[0]['total']}")

        self.egress = Egress.objects.create(
            user_id=self.user1,
            amount=10.00,
            description="Test"
        )

        totalFinal = Total.objects.filter(pk=self.total.id).values('total')
        print(f"Total final: {totalFinal[0]['total']}")
