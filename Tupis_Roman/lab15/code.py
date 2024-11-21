#У цьому прикладі метод порушує принцип KISS та DRY, оскільки містить зайву складність і дублювання.
# Зайва вкладеність умов, через що метод стає важко читабельним.
# Дублювання логіки для різних типів клієнтів.


def calculate_discount(price, customer_type):
    if customer_type == "regular":
        if price > 100:
            return price * 0.9  # 10% знижка
        else:
            return price
    elif customer_type == "vip":
        if price > 100:
            return price * 0.8  # 20% знижка
        else:
            return price * 0.9  # 10% знижка
    else:
        return price



#Відокремимо обчислення знижки в окремий метод і зменшимо дублювання.
def get_discount_rate(price, customer_type):
    discount_rates = {
        "regular": 0.9 if price > 100 else 1,
        "vip": 0.8 if price > 100 else 0.9
    }
    return discount_rates.get(customer_type, 1)

def calculate_discount(price, customer_type):
    return price * get_discount_rate(price, customer_type)

