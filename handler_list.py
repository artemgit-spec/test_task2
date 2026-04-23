import abc


class HandlerABC(abc.ABC):

    @abc.abstractmethod
    def func_report():
        pass


class Handler(HandlerABC):

    def __init__(self, file, report):
        self.file: list = file
        self.report: str = report

    def func_report(self) -> list:  # обрабатывает данные и возвращает готовый список
        if self.report == "clickbait":
            list_stats: list = []
            stats: list = ["views", "likes", "avg_watch_time"]
            for i in self.file:
                if float(i["ctr"]) > 15 and int(i["retention_rate"]) < 40:
                    list_stats.append(i)
            list_stats = sorted(list_stats, key=lambda k: k["ctr"], reverse=True)

            list_stats = [
                {key: value for key, value in i.items() if key not in stats}
                for i in list_stats
            ]

            return list_stats
