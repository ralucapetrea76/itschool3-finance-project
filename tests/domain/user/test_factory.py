import unittest
import uuid

from domain.user.factory import UserFactory, InvalidUsername
from domain.user.user import User


class UserFactoryTestCase(unittest.TestCase):
    def test_it_creates_user_if_the_username_is_between_6_and_20_chars(self):
        username = "between-6-20"
        factory = UserFactory()

        actual_user = factory.make_new(username)

        self.assertEqual(username, actual_user.username)
        self.assertEqual(User, type(actual_user))

    def test_it_raises_exception_if_the_username_is_bellow_6_chars(self):
        username = "below"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should have at least 6 characters or maximum 20 characters",
            str(context.exception),
        )

    def test_it_rasises_exception_if_the_username_is_above_20_chars(self):
        username = "above"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "Username should have at least 6 characters or maximum 20 characters",
            str(context.exception),
        )


    def test_it_creates_a_user_if_the_username_has_valid_chars(self):
        username = "raluca"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "User is valid", str(context.exception)
        )


    def test_if_raises_exception_if_the_username_has_invalid_chars(self):
        username = "raluca+"
        factory = UserFactory()

        with self.assertRaises(InvalidUsername) as context:
            factory.make_new(username)

        self.assertEqual(
            "User is not valid", str(context.exception)
        )



if __name__ == "__main__":
    unittest.main()
