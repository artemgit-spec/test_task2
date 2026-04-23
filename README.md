# test-task
скрипт для обработки csv-файла

Скрипт читает один или несколько CSV-файлов с информацией о брендах, моделях устройств, цене и рейтинге.  
На основе входных данных можно построить отчет — вычислить средний балл для бренда.

Для запуска использовать команды:
python main.py --files students1.csv --report average
python main.py --files products1.csv products2.csv --report average
python main.py --files D:\путь к файлу\products1.csv D:\путь к файлу\products2.csv --report average
где:
--files - список CVS-файлов для анализа 
--report - тип отчета. 
На данный момент поддерживается тип:
    average - расчет среднего балла по студентам.

Пример получаемых данных:
name,brand,price,rating
iphone 15 pro,apple,999,4.9
galaxy s23 ultra,samsung,1199,4.8
redmi note 12,xiaomi,199,4.6
iphone 14,apple,799,4.7
galaxy a54,samsung,349,4.2

Пример отчета:
brand      rating
-------  --------
samsung       4.5
xiaomi        4.6
apple         4.8


Структура проекта:
├── handler_list.py  # класс Handler (чистая логика)
├── parse_script.py  # класс ParseLine (обработка командной строки)
├── main.py          # CLI, вывод результата
├── README.md
├── requirements.txt
└── tests 
        ├── test_handler.py  # тесты для Handler
        └── test_main.py     # тесты run()
