#оновлений метод add_event (забрано роботу з файлами у інший клас, логіку з input/print також винесено у інший клас)
def add_event(self, path, title, description, date, participants):
        obj_date = Date()
        if not obj_date.validate_date(date):
            raise ValueError("Invalid date format.")

        self.title = title
        self.description = description
        self.date = date
        self.participant = participants

        day, month, year = date.split("-")
        file_path = path + f"/{day}-{month}-{year}/{date}.json"
        data = {
            "title": self.title,
            "description": self.description,
            "date": self.date,
            "participants": self.participant
        }
        self.file_manager.write_file(file_path, data)
        self._update_all_events_file(path, date, date, title)
# зроблено ті самі зміни, як у попередньому методі
 def update_event(self, path, date, updated_data):
        day, month, year = date.split("-")
        old_file_path = path + f"/{day}-{month}-{year}/{date}.json"

        event = self.file_manager.read_json(old_file_path)
        if not event:
            raise FileNotFoundError(f"Event with the date {date} does not exist.")

        old_date = event["date"]
        old_title = event["title"]

        if "title" in updated_data:
            event["title"] = updated_data["title"]

        if "description" in updated_data:
            event["description"] = updated_data["description"]

        if "date" in updated_data:
            new_date = updated_data["date"]
            new_day, new_month, new_year = new_date.split("-")
            new_file_path = path + f"/{new_day}-{new_month}-{new_year}/{new_date}.json"

            self.file_manager.move_file(old_file_path, new_file_path)
            event["date"] = new_date
            old_file_path = new_file_path

        if "participants" in updated_data:
            event["participants"] = updated_data["participants"]

        self.file_manager.write_json(old_file_path, event)

        new_title = event["title"]
        new_date = event["date"]
        self._update_all_events_file(path, old_date, new_date, new_title)


# метод output_event розділено на декілька простіших/спеціалізованих методів, а також логіку print/input і роботу з файлами винесено у інші класи
def display_events_by_year(self, path, year):
        all_events_path = path + "/all_events.txt"
        if not self.file_manager.file_exists(all_events_path):
            return "No events found."

        events = self.file_manager.read_file(all_events_path).splitlines()
        filtered_events = []

        for event in events:
            if event.strip():
                parts = event.split()
                if len(parts) > 0 and parts[0].endswith(year):
                    filtered_events.append(event)

        if not filtered_events:
            return "No events found for the specified year."

        return filtered_events

    def display_events_by_month(self, path, year, month):
        all_events_path = path + "/all_events.txt"
        if not self.file_manager.file_exists(all_events_path):
            return "No events found."

        events = self.file_manager.read_file(all_events_path).splitlines()
        filtered_events = []

        for event in events:
            if event.strip():
                parts = event.split()
                if len(parts) > 0 and parts[0][3:10] == f"{month}-{year}":
                    filtered_events.append(event)

        if not filtered_events:
            return "No events found for the specified month."

        return filtered_events

    def display_events_by_day(self, path, date):
        day, month, year = date.split("-")
        file_path = path + f"/{day}-{month}-{year}/{date}.json"

        if self.file_manager.file_exists(file_path):
            event_data = self.file_manager.read_file(file_path)
            try:
                event = self.file_manager.read_json(file_path)
                if event is None:
                    return "No event data found in the specified file."

                output = f"Title: {event['title']}\n"
                output += f"Description: {event['description']}\n"
                output += f"Date: {event['date']}\n"
                output += f"Participants: {', '.join(event['participants'])}\n"
                return output
            except ValueError:
                return "Error reading event data."
        else:
            return "No event found for the specified date."

    def display_events_by_period(self, path, start_date, end_date):
        all_events_path = path + "/all_events.txt"
        if not self.file_manager.file_exists(all_events_path):
            return "No events found."

        events = self.file_manager.read_file(all_events_path).splitlines()
        start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
        end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")

        filtered_events = []
        for event in events:
            if event.strip():
                parts = event.split()
                if len(parts) > 0:
                    event_date_str = parts[0]
                    try:
                        event_date_obj = datetime.strptime(event_date_str, "%d-%m-%Y")
                        if start_date_obj <= event_date_obj <= end_date_obj:
                            filtered_events.append(event)
                    except ValueError:
                        continue

        if not filtered_events:
            return "No events found for the specified period."

        return filtered_events
