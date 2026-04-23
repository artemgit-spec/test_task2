import pytest
from handler_list import Handler


@pytest.mark.parametrize(
    "filter, my_data",
    [
        (
            "clickbait",
            [
                {
                    "title": "Секрет который скрывают тимлиды",
                    "ctr": "25.0",
                    "retention_rate": "22",
                }
            ],
        ),
    ],
)
def test_func_report(list_data_file, filter, my_data):
    th = Handler(list_data_file, filter)
    result = th.func_report()
    assert result == my_data
