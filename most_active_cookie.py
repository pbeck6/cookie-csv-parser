"""
Most Active Cookie
Last Modified: Dec 3, 2021

Command line program to parse a CSV file and display a list of most active cookie(s) for the
specified date.

Run with `$ python most_active_cookie.py filename.csv -d YYYY-MM-DD`
"""

import argparse, logging
from csv_parser import CSVParser


class MostActiveCookie:
    def parse_cli(self) -> object:
        """
        Parses cli for file name and date
        :return: Namespace object with arguments
        """

        parser = argparse.ArgumentParser(description="Find the most active cookie from a csv file.")
        parser.add_argument("filename", type=str, help="CSV Filename")
        parser.add_argument("-d", "--date", type=str, help="Date to search for most active cookie (YYYY-MM-DD)", required=True)

        args = parser.parse_args()
        return args

    def main(self) -> None:
        """
        Converts CSV to array
        Strips time from timedate in resulting array, leaving only date
        Tabulates cookie occurrences, displays most active cookie(s)
        """
        logging.basicConfig(
            format="%(asctime)s %(module)s %(levelname)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            handlers=[logging.FileHandler("mac-log.log"), logging.StreamHandler()],
        )

        try:
            args = self.parse_cli()
        except:
            logging.exception("Incorrect syntax (invalid or missing args)")

        cp = CSVParser()
        parsed_array = cp.parse(args.filename)
        cp.strip_time(parsed_array)
        
        # In CSV file, assumes cookie name is held in column 0 (zero-indexed)
        hashmap = cp.tabulate_matches(parsed_array, args.date, 0)

        most_active = max(hashmap.values())
        res = [keys for keys, values in hashmap.items() if values == most_active]
        
        for item in res: print(item)


if __name__ == "__main__":
    MostActiveCookie().main()
    