import requests


def fetch_birthdays(month, department):
    url = f'http://127.0.0.1:5000/birthdays?month={month}&department={department}'
    response = requests.get(url)
    return response.json()


def fetch_anniversaries(month, department):
    url = f'http://127.0.0.1:5000/anniversaries?month={month}&department={department}'
    response = requests.get(url)
    return response.json()


if __name__ == "__main__":
    month = input("Enter the month (e.g., 06): ")
    department = input("Enter the department (e.g., Finance or Information%20Technology: ")
    report_type = input("Enter the report type (Birthdays or Anniversaries): ").lower()

    print(f"Report for {department} department for {month} month fetched.")

    if report_type == "birthdays":
        print(f"Birthdays Report for {department} department for {month}:")
        report = fetch_birthdays(month, department)
        print (f'Total:{report['total']}')
        for employee in report['employees']:
            print(f"Name: {employee['Name']}, Birthday: {employee['Birthday']}")
    elif report_type == "anniversaries":
        print(f"Anniversaries Report for {department} department for {month}:\n")
        report = fetch_anniversaries(month, department)
        print (f'Total:{report['total']}')
        for employee in report['employees']:
            print(f"Name: {employee['Name']}, Hiring Date: {employee['Hiring Date']}")
    else:
        print("Invalid report type. Please choose between Birthdays or Anniversaries.")
        exit()

