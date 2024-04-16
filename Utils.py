def formatDate(date):

    split_date = date.split('-')
    day = split_date[2]
    month = split_date[1]
    year = split_date[0]
    formatted_date = f'{day}.{month}.{year}'
    
    return formatted_date