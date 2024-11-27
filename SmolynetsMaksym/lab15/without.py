def process_data(datas):
    result = []
    for item in datas:
        if isinstance(item, str):
            result.append(item.lower())
        elif isinstance(item, int):
            result.append(item * 2)
        else:
            result.append(None)
    return result


data = ['Hello', 5, 10, 'World', 3.5]
processed = process_data(data)
print(processed)