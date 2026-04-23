import pytest
import csv


@pytest.fixture
def file_csv(tmp_path):
    data = [
        {
            "title": "Секрет который скрывают тимлиды",
            "ctr": "25.0",
            "retention_rate": "22",
            "views": "254000",
            "likes": "8900",
            "avg_watch_time": "2.5",
        },
        {
            "title": "Дедлайн подкрался незаметно",
            "ctr": "10.0",
            "retention_rate": "70",
            "views": "25600",
            "likes": "670",
            "avg_watch_time": "7.5",
        },
    ]
    csv_file = tmp_path / "stats1.csv"
    with open(csv_file, "w", newline="", encoding="utf-8") as file:
        write_file = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "ctr",
                "retention_rate",
                "views",
                "likes",
                "avg_watch_time",
            ],
        )
        write_file.writeheader()
        write_file.writerows(data)
    return csv_file


@pytest.fixture
def list_data_file(file_csv):
    list_prod = []
    with open(file_csv, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        list_prod.extend(reader)
    return list_prod
