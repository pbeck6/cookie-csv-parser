"""
Unit tests for CSVParser class as used with Most Active Cookie, output to parser-tests.log
"""

import unittest, logging
from csv_parser import CSVParser

class TestCSVParser(unittest.TestCase):
    """
    Class to test MostActiveCookie, inherited from unittest module
    """

    @classmethod
    def setUpClass(cls):
        """
        Runs before test to set logging parameters
        """
        logger = logging.getLogger(__name__)
        FORMAT = "%(asctime)s %(module)s %(levelname)s: %(message)s"
        logging.basicConfig(
            filename="mac-tests-log.log",
            format=FORMAT,
            level=logging.INFO,
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        logger.info("Starting test...")
        
    @classmethod
    def tearDownClass(cls):
        """
        Runs after test to wrap up log
        """
        logging.getLogger(__name__).info("Test complete.\n")

    def setUp(self):
        """
        Prepare test fixture, create instance of CSVParser class
        """
        self.csvp = CSVParser()

    def test_invalid_file(self):
        """
        Tests parse() function raising correct error when file not found
        """
        # Invalid filename
        with self.assertRaises(FileNotFoundError): self.csvp.parse("okie_log.csv")
        # Empty filename
        with self.assertRaises(FileNotFoundError): self.csvp.parse()

    def test_valid_file(self):
        """
        Tests parse() for proper function
        """
        self.assertIsInstance(self.csvp.parse("cookie_log.csv"), list)

    def test_invalid_list(self):
        """
        Tests strip_header() and strip_time() function raising error when lists are invalid
        """
        # Invalid type
        with self.assertRaises(TypeError): self.csvp.strip_header(46)
        with self.assertRaises(TypeError): self.csvp.strip_time(46)
        with self.assertRaises(TypeError): self.csvp.strip_header("somestring")
        # Empty list
        with self.assertRaises(IndexError): self.csvp.strip_header([])

    def test_valid_list(self):
        """
        Tests strip_header() and strip_time() for proper function
        """
        original = [["name", "ipaddress"],["eb1432fa21", "192.0.0.0"]]
        expected = [["eb1432fa21", "192.0.0.0"]]
        self.csvp.strip_header(original)
        self.assertEqual(original, expected)

        original = [["eb1432fa21", "2020-11-11T30:30:30+30:30"]]
        expected = [["eb1432fa21", "2020-11-11"]]
        self.csvp.strip_time(original)
        self.assertEqual(original, expected)

    def test_invalid_tabulate(self):
        """
        Tests tabulate_matches() function for parameter errors
        """
        # Missing params
        with self.assertRaises(TypeError): self.csvp.tabulate_matches([])
        with self.assertRaises(TypeError): self.csvp.tabulate_matches([], "")
        # Incorrect param type
        with self.assertRaises(TypeError): self.csvp.tabulate_matches(46, "", 46)
        with self.assertRaises(TypeError): self.csvp.tabulate_matches(["dog"], "dog", "cat")
        with self.assertRaises(IndexError): self.csvp.tabulate_matches(["dog"], "dog", 999)

    def test_valid_tabulate(self):
        """
        Tests tabulate_matches() for proper function
        """
        res = [
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-09"],
            ["5UAVanZf6UtGyKVS", "2018-12-09"],
            ["AtY0laUfhglK3lC7", "2018-12-09"],
            ["SAZuXPGUrfbcn5UA", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-08"],
            ["fbcn5UAVanZf6UtG", "2018-12-08"],
            ["4sMM2LxV07bPJzwf", "2018-12-07"]
        ]
        expected = {
            "AtY0laUfhglK3lC7" : 2,
            "SAZuXPGUrfbcn5UA" : 1,
            "5UAVanZf6UtGyKVS" : 1
        }
        self.assertEqual(self.csvp.tabulate_matches(res, "2018-12-09", 0), expected)


if __name__ == "__main__":
    unittest.main()
