
from datetime import datetime, timedelta

DATE_FORMAT = "%d-%m-%Y"


def parse_date(date_text):
    try:
        return datetime.strptime(date_text.strip(), DATE_FORMAT).date()
    except ValueError:
        raise ValueError(
            "Invalid date. Please enter the date as DD-MM-YYYY."
        )


def parse_subjects(subject_text):
    subjects = [
        subject.strip()
        for subject in subject_text.split(",")
        if subject.strip()
    ]

    if not subjects:
        raise ValueError("At least one subject is required.")

    seen = set()

    for subject in subjects:
        if subject.lower() in seen:
            raise ValueError(f"Duplicate subject: {subject}.")
        seen.add(subject.lower())

    return subjects


def parse_holidays(holiday_text):
    if not holiday_text.strip() or holiday_text.lower() == "none":
        return set()

    holidays = set()

    for date_text in holiday_text.split(","):
        holidays.add(parse_date(date_text))

    return holidays


def generate_timetable(subjects, start_date, holidays):
    timetable = []
    current_date = start_date

    for subject in subjects:

        while current_date.weekday() == 6 or current_date in holidays:
            current_date += timedelta(days=1)

        entry = {
            "subject": subject,
            "date": current_date.strftime(DATE_FORMAT),
            "weekday": current_date.strftime("%A")
        }

        timetable.append(entry)
        current_date += timedelta(days=1)

    return timetable


def print_timetable(timetable):
    print("\nEXAMINATION TIMETABLE")
    print("-" * 40)

    for entry in timetable:
        print(
            f"{entry['subject']} : "
            f"{entry['date']} ({entry['weekday']})"
        )

    print("-" * 40)


def main():
    print("EXAMINATION TIMETABLE GENERATOR")

    try:
        subject_text = input("\nEnter your subjects: ")
        subjects = parse_subjects(subject_text)

        start_text = input("Enter start date (DD-MM-YYYY): ")
        start_date = parse_date(start_text)

        holiday_text = input("Enter holidays (or none): ")
        holidays = parse_holidays(holiday_text)

        timetable = generate_timetable(
            subjects, start_date, holidays
        )

        print_timetable(timetable)

    except ValueError as error:
        print("\nError:", error)


if __name__ == "__main__":
    main()
