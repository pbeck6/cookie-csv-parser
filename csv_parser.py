"""
Module is useful for situations where csv parsing libraries are unavailable (csv, pandas, etc.).

Reads filename.csv and converts to an array that contains each entry as a nested array of strings

"""
import re

class CSVParser:

    def parse(self, filename: str="", header: bool=True) -> list[list[str]]:
        """
        Reads file, and adds each csv entry manually to list
        :param filename: CSV file location
        :param header: Set to strip header by default
        :return: Array of nested arrays of strings
        """

        try:
            with open(filename, "r") as csv_file:
                res = []
                for info in csv_file:
                    parsed_info = info.strip().split(",")
                    res.append(parsed_info)
                if header: self.strip_header(res)
                return res
        except:
            raise FileNotFoundError

    def strip_header(self, res: list) -> None:
        """
        Strips header columns from parsed list object
        :param res: Parsed CSV file
        :return: None, modifies in-place
        """

        try:
            del res[0]
            return
        except:
            raise IndexError if not res else TypeError

    def strip_time(self, res: list) -> None:
        """
        Strips time from timedate entries if they exist in parsed list object
        Uses regex WITHOUT using datetime module
        :param res: Parsed CSV file
        :return: None, modifies in-place
        """

        try:
            timedate_pattern = r"^(\d{4}-\d{2}-\d{2})T(\d{2}:\d{2}:\d{2}\+\d{2}:\d{2})$"
            for entry in res:
                for i, s in enumerate(entry):
                    if re.match(timedate_pattern, s):
                        entry[i] = s.split("T", 1)[0]
        except:
            raise TypeError

    def tabulate_matches(self, res: list, target: str, key_index: int) -> dict:
        """
        Uses Python dict to tabulate occurrences that match the target param
        :param res: Parsed CSV file
        :param target: Target string to match
        :key_index: Column with which to tabulate target matches
        :return: Key=set with key_index param, Value=# of occurrences of each key 
        """
        
        try:
            hashmap = {}
            for entry in res:
                if target in entry:
                    hashmap[entry[key_index]] = hashmap.get(entry[key_index], 0) + 1
            return hashmap
        except (IndexError, TypeError) as e:
            raise e
