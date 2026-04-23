import argparse


# команда для парсинга
def func_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("--files", nargs="*")
    parser.add_argument("--report", choices=["clickbait"])
    return parser.parse_args()
