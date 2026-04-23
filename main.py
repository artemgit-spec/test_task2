import csv
from tabulate import tabulate
from parse_script import func_parse
from handler_list import Handler


def run(file) -> list:  # читает файл и возвращает список данных
    my_list_prod: list = []

    for f in file:
        with open(f, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            my_list_prod.extend(reader)
    return my_list_prod


def main():
    args = func_parse()
    try:
        result_run = run(args.files)
        class_handler = Handler(result_run, args.report)
        print_result = tabulate(class_handler.func_report(), headers="keys")
    except FileNotFoundError:
        print_result = "Нет нужных файлов"
    finally:
        print(print_result)
        print(type(class_handler.func_report()))


if __name__ == "__main__":
    main()
