"""Python CSV Sample codes
"""
import csv
from collections import OrderedDict
from typing import List

SUBJECTS_LENGTH = 3


def load_csvfile(filepath: str) -> List[OrderedDict]:
    result = []
    with open(file=filepath, mode="r") as csvfp:
        reader = csv.DictReader(csvfp)
        for row in reader:
            result.append(row)
    return result


def save_csvfile(filepath: str, fieldnames: list, records: List[dict]):
    with open(file=filepath, mode="w") as csvfp:
        writer = csv.DictWriter(csvfp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


class Student:
    name: str
    math: int = 0
    eng: int = 0
    korean: int = 0
    total: int = 0
    avg: float = 0.0

    def to_dict(self) -> dict:
        return self.__dict__.copy()

    @classmethod
    def fields(cls) -> list:
        fieldnames = list(cls.__annotations__.keys())  # pylint: disable=no-member
        return fieldnames.copy()

    def _calculate_total(self):
        self.total = self.math + self.eng + self.korean

    def _calculate_avg(self):
        if self.total > 0:
            self.avg = float(self.total) / SUBJECTS_LENGTH

    def set_data(self, name: str, math: str, eng: str, korean: str):
        self.name = name
        self.math = int(math)
        self.eng = int(eng)
        self.korean = int(korean)
        self._calculate_total()
        self._calculate_avg()


def main():
    """Show basic usage of the CSV package
    Load sample csv file and Save test csv file.
    """
    sample_students = load_csvfile("sample.csv")

    csv_recoreds = []
    student = Student()
    for member in sample_students:
        student.set_data(**member)
        csv_recoreds.append(student.to_dict())

    fieldnames = Student.fields()
    save_csvfile(
        filepath="test_result.csv", fieldnames=fieldnames, records=csv_recoreds
    )


if __name__ == "__main__":
    main()
