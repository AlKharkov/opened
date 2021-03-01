def big_data(*data, key=lambda x: x[0]):
    new_data = list()
    for user in data:
        idd, date, email = user
        day, month, year = date.split('-')
        new_data.append(
            (idd, date, email, f'{email.split("@")[0].capitalize()}{day[0]}{month[-1]}{year[-1]}'))
    return sorted(new_data, key=key)
