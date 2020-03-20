import smtplib
import unittest
from unittest import TestCase
from unittest.mock import Mock
from send_inspiration import main
import logging
mock = Mock()
m = mock.Mock()


class Sending_email(unittest.TestCase):
    def setUp(self):
        self.emails = []

    def test_get_contacts(self, *args):
        for i in self.emails:
            self.assertTrue(i == main(), 'Incorrect')
        s = 'thato thato.thupudi@umuzi.org'
        self.assertEqual(s.split(), ['thato', 'thato.thupudi@umuzi.org'])
        with self.assertRaises(TypeError):
            s.split(2)
            self.assertEqual(len(s.emails), 2)
            self.assertEqual(s.emails[0].frm, 'thato.thupudi@umuzi.org')
            self.assertEqual(s.emails[0].to, ['thatothupudi@gmail.com'])
            self.assertEqual(
                s.emails[0].msg, "Here's an ispiration quote for you!!!!")
            self.assertEqual(m.get_contacts) == False
    # def test_get_contacts(self):
    #     names = send_inspiration('To', 'From', 'Subject')
    #     self.assertEqual('thato','MY_ADDRESS', 'message') == True

    def tearDown(self):
        self.emails = None


if __name__ == '__main__':
    unittest.main()
