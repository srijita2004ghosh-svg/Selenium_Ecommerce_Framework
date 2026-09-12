import csv
import os


class CSVReader:

    @staticmethod
    def read_login_data():
        project_root = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        csv_path = os.path.join(
            project_root,
            "test_data",
            "login_data.csv"
        )

        with open(csv_path, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)