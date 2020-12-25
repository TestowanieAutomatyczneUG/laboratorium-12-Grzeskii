import unittest
from assertpy import *
from src.sample.random_user import RandomUser


class TestRandomUser(unittest.TestCase):

    def setUp(self):
        self.temp = RandomUser()

    def test_get_random_user(self):
        assert_that(self.temp.get_random_user()).contains('gender', 'name')

    def test_get_multiple_users(self):
        assert_that(self.temp.get_multiple_users(25)).is_length(25)

    def test_get_multiple_users_wrong_args(self):
        assert_that(self.temp.get_multiple_users).raises(TypeError).when_called_with("osiem")

    def test_get_random_user_gender(self):
        data = self.temp.get_random_user_gender("male")
        assert_that(data["gender"]).is_equal_to("male")

    def test_get_random_user_gender_wrong_args(self):
        assert_that(self.temp.get_random_user_gender).raises(ValueError).when_called_with(42)

    def tearDown(self):
        self.temp = None


if __name__ == "__main__":
    unittest.main()
