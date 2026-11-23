import unittest

from app import app


class IndexTest(unittest.TestCase):
    def test_index_served(self):
        r = app.test_client().get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn("GoodDeeds", r.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()