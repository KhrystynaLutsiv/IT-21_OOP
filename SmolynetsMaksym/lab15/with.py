def process_data(datas):
    return [
        item.lower() if isinstance(item, str) else item * 2 if isinstance(item, int) else None
        for item in datas
    ]


data = ['Hello', 5, 10, 'World', 3.5]
processed = process_data(data)
print(processed)