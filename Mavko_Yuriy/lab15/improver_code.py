# Методи add_event, update_event, і output_event мають значний обсяг коду, який складно читати та підтримувати.
# Перевірка існування директорій і створення директорій повторюється.
# Обробка дати для розподілу на день, місяць і рік часто дублюється.
# Занадто багато відповідальносте, метод add_event відповідає і за збір даних, і за збереження файлів.
# Великий обсяг логіки у if умовах: update_event має складну структуру з багатьма вкладеними умовами.
# Порушення принципу DRY (Don't Repeat Yourself): Логіка роботи з файлами (запис/видалення) дублюється.
# Непослідовний стиль іменування, назви змінних англійською, іноді скорочені, що ускладнює читання.

def add_event(self, path_to_auth,  title = None, description = None, date = None, participant = None):
    if title == None and description == None and date == None and participant == None:
        self.title = input("Enter title\n")
        self.description = input("Enter description\n")
        while not validate_date(self.date):
            self.date = input("Enter date (dd-mm-yyyy)\n")
        num = int(input("Enter the number of participants\n"))
        for i in range(0, num):
            value = input(f"Enter {i+1} participant\n")
            self.participant.append(value)
    else:
        self.title = title
        self.description = description
        self.date = date
        self.participant = participant
    data = {
        "title": self.title,
        "description": self.description,
        "date": self.date,
        "participants": self.participant
    }

    day, month, year = self.date.split("-")

    year_dir = f"{path_to_auth}/{year}"
    os.makedirs(year_dir, exist_ok=True)
    with open(os.path.join(year_dir, f"all_events_{year}.txt"), 'a') as year_file:
        year_file.write(f"{self.date} {self.title}\n")

    month_dir = os.path.join(year_dir, f"{month}")
    os.makedirs(month_dir, exist_ok=True)
    with open(os.path.join(month_dir, f"all_events_{month}.txt"), "a") as month_file:
        month_file.write(f"{self.date} {self.title}\n")

    day_dir = os.path.join(month_dir, f"{day}")
    os.makedirs(day_dir, exist_ok=True)
    path = os.path.join(day_dir, f"{self.date}.json")
    with open(path, 'w', encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def update_event(self, path_to_auth):
    d = ""
    while not validate_date(d):
        d = input("Enter the date (dd-mm-yyyy) of the event you want to change\n")
    day, month, year = d.split("-")
    path_to_json = f"{path_to_auth}/{year}/{month}/{day}/{d}.json"
    check_title = ""
    if os.path.exists(path_to_json):
        with open(path_to_json) as file:
            data = json.load(file)
        origin_data = data.copy()
        new_data = data.copy()
    else:
        pass
    if os.path.exists(path_to_json):
        with open(path_to_json) as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
        check_title = data["title"]
        num = 0
        while num != 5:
            print("Enter a number if you want to change the")
            print("1 - title,")
            print("2 - description")
            print("3 - date,")
            print("4 - participants,")
            print("and 5 if you want to exit the data change")
            num = int(input())
            if num == 1:
                new_title = input("Enter the new title\n")
                new_data["title"] = new_title
            elif num == 2:
                new_description = input("Enter the new description\n")
                new_data["description"] = new_description
            elif num == 3:
                new_date = ""
                while not validate_date(new_date):
                    new_date = input("Enter the new date (dd-mm-yyyy)\n")
                new_data["date"] = new_date
            elif num == 4:
                new_participants = []
                num_participants = int(input("Enter the number of participants\n"))
                for i in range(0, num_participants):
                    value = input(f"Enter {i+1} the participant\n")
                    new_participants.append(value)
                new_data["participants"] = new_participants
        if d == new_data["date"]:
            if check_title == data["title"]:
                with open(path_to_json, 'w', encoding="utf-8") as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=4)
            else:
                with open(path_to_json, 'w', encoding="utf-8") as json_file:
                    json.dump(data, json_file, ensure_ascii=False, indent=4)
                path_to_delete = f"{path_to_auth}/{year}/{month}/all_events_{month}.txt"
                line_to_delete = f"{day}-{month}-{year} {check_title}"
                lines = []
                with open(path_to_delete, 'r') as file:
                    lines = file.readlines()
                with open(path_to_delete, 'w') as file:
                    for line in lines:
                        if line.strip() != line_to_delete.strip():
                            file.write(str(line))

                with open(path_to_delete, 'a') as file:
                    file.write(f'{day}-{month}-{year} {data['title']}\n')

                path = f"{path_to_auth}/{year}/all_events_{year}.txt"
                with open(path, 'r') as file:
                    lines = file.readlines()
                with open(path, 'w') as file:
                    for line in lines:
                        if line.strip() != line_to_delete.strip():
                            file.write(line)

                with open(path, 'a') as file:
                    file.write(f'{day}-{month}-{year} {data['title']}\n')
        else:
            path_to_delete_year = f"{path_to_auth}/{year}/all_events_{year}.txt"
            line_to_delete = f"{day}-{month}-{year} {origin_data["title"]}"
            lines = []
            with open(path_to_delete_year, 'r') as file:
                lines = file.readlines()
            with open(path_to_delete_year, 'w') as file:
                for line in lines:
                    if line.strip() != line_to_delete.strip():
                        file.write(str(line))
            path_to_delete_month = f"{path_to_auth}/{year}/{month}/all_events_{month}.txt"
            lines = []
            with open(path_to_delete_month, 'r') as file:
                lines = file.readlines()
            with open(path_to_delete_month, 'w') as file:
                for line in lines:
                    if line.strip() != line_to_delete.strip():
                        file.write(str(line))
            path_to_delete_day_file = f"{path_to_auth}/{year}/{month}/{day}/{day}-{month}-{year}.json"
            with open(path_to_delete_day_file, 'r') as file:
                data = json.load(file)
            title = data.get('title', 'nothing')
            if os.path.exists(path_to_delete_day_file):
                os.remove(path_to_delete_day_file)
            else:
                print("Error deleting a file")
            self.add_event(path_to_auth, new_data["title"], new_data["description"], new_data["date"], new_data["participants"])
    else:
        print("There is no such event")

def output_event(self, path_to_auth):
    print("Enter 1 if you want to display all events of a certain year")
    print("Enter 2 if you want to display all events of a particular month")
    print("Enter 3 if you want to display all events of a particular day")
    print("Enter 4 if you want to display all events for a specific time period")
    num = int(input())
    if num == 1:
        year = int(input("Enter the year\n"))
        if os.path.isdir(f"{path_to_auth}/{year}"):
            with open(f"{path_to_auth}/{year}/all_events_{year}.txt", 'r') as file:
                for line in file:
                    print(line.strip())
                number = int(input("Enter 1 if you want to view a specific event or any other number if not\n"))
                if number == 1:
                    date = ""
                    while not validate_date(date):
                        date = input("Enter date (dd-mm-yyyy)\n")
                    d, m, y = date.split("-")
                    path = f"{path_to_auth}/{y}/{m}/{d}/{date}.json"
                    if os.path.exists(path):
                        with open(path) as file:
                            data = json.load(file)
                            print(json.dumps(data, indent=4))
                    else:
                        print("There is no such event")
                else:
                    pass #якщо введена люба інша цифра то вихід
        else:
            print(f"You have no events planned for {year}")
    elif num == 2:
        year = int(input("Enter the year\n"))
        month = int(input("Enter the month\n"))
        if month < 10:
            month = "0" + f"{month}"
        if os.path.isdir(f"{path_to_auth}/{year}/{month}"):
            with open(f"{path_to_auth}/{year}/{month}/all_events_{month}.txt", 'r') as file:
                for line in file:
                    print(line.strip())
                number = int(input("Enter 1 if you want to view a specific event or any other number if not\n"))
                if number == 1:
                    date = ""
                    while not validate_date(date):
                        date = input("Enter date (dd-mm-yyyy)\n")
                    d, m, y = date.split("-")
                    path = f"{path_to_auth}/{y}/{m}/{d}/{date}.json"
                    if os.path.exists(path):
                        with open(path) as file:
                            data = json.load(file)
                            print(json.dumps(data, indent=4))
                    else:
                        print("There is no such event")
                else:
                    pass #якщо введена люба інша цифра то вихід
        else:
            print(f"You have no events planned for {month}-{year}")
    elif num == 3:
        date = ""
        while not validate_date(date):
            date = input("Enter date (dd-mm-yyyy)\n")
        day, month, year = date.split("-")
        if os.path.isdir(f"{path_to_auth}/{year}/{month}/{day}"):
            path = f"{path_to_auth}/{year}/{month}/{day}/{day}-{month}-{year}.json"
            if os.path.exists(path):
                with open(path) as file:
                    data = json.load(file)
                    print(json.dumps(data, indent=4))
            else:
                print("There is no such event")
        else:
            print(f"You have no events planned for {year}-{month}-{day}")

    #elif number 4 doesn`t work
    elif num == 4:
        start_date = ""
        end_date = ""
        while not validate_date(start_date):
            start_date = input("Enter start date (dd-mm-yyyy)\n")
        while not validate_date(end_date):
            end_date = input("Enter end date (dd-mm-yyyy)\n")

