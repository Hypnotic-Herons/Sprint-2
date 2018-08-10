import unittest
from django.test import TestCase
from django.urls import reverse
from HRIT.models import Computer


class ComputerListTest(TestCase):

    def test_list_computers(self):
        new_computer = Computer.objects.create(
            manufacturer="Dell",
            make="Inspiron",
            purchase_date="2018-07-20"
        )

        # Issue a GET request.
        # 'reverse' is used to generate a URL for a given view. The main advantage is that you do not hard code routes in your code.
        response = self.client.get(reverse('HRIT:computers'))

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 1 computer.
        # The key 'computer_list' comes from the ComputerViewModel where we said context_object_name = 'computer_list'
        self.assertEqual(len(response.context['computer_list']), 1)

        # Is this stuff in the content of the body?
        # .encode converts from unicode to utf-8
        # example:
        # If the string is: pythön!
        self.assertIn(new_computer.manufacturer.encode(), response.content)

