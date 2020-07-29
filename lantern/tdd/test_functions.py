import  unittest
from unittest.mock import patch

from functions import fun
from functions import return_boolean_value
from functions import parse_response



class TestFunc(unittest.TestCase):

    def test_return_1_func(self):
        expected_res = fun()
        self.assertEquals(expected_res, 1)

class TestBooleanFunction(unittest.TestCase):

    def test_return_boolean_value_function(self):
        self.assertTrue(return_boolean_value(2))

class TestTesrDownSetUp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("From Setup Class")
    @classmethod
    def tearDownClass(cls):
        print("From Tear Down Class")

    def setUp(self):
        self.list_ = [1,2]
        print("From set up")

    def tearDown(self):
        print("from tear down")

    def test_assert_true(self):
        print("I am test")
        print(self.list_)
        self.list_.append(3131313)
        self.assertTrue("a")

    def test_assert_false(self):
        print(self.list_)
        self.list_.append(1)
        print("I am test 2")
        self.assertFalse("")

    @patch("functions.call_to_different_service")
    def test_parse_response(self, mock):
        def return_mock():
            return "NEW"
        mock.return_value = return_mock()
        excepted = parse_response()
        self.assertEqual(excepted, "OK")

#class NumbersTest(unittest.TestCase):
#
#    def test_even(self):
#        for i in range(0,6):
#            with self.subTest(i=i):
#                self.assertEqual(i % 2, 0)




