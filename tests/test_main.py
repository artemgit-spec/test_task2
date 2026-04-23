import pytest
from main import run


@pytest.mark.parametrize(
    "my_data",
    [
        [
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
    ],
)
def test_run(file_csv, my_data):
    result_list = run([file_csv])
    assert result_list == my_data
