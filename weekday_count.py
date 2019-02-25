import datetime as dt


t_start_date = dt.date(2018, 10, 1)
t_end_date = dt.date(2018, 12, 31)


def weekday_count(*, start_date, end_date):
    """docstring sample"""
    day_range = [start_date + dt.timedelta(days=i) for i in range((end_date - start_date).days + 1)]
    wdays = ['mo', 'di', 'mi', 'do', 'fr', 'sa', 'so']
    amount_days = {k: len(list(filter(lambda x: x.weekday() == k, day_range))) for k, v in enumerate(wdays)}
    return amount_days


if __name__ == '__main__':
    print(weekday_count(start_date=t_start_date, end_date=t_end_date))
