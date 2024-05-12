############################# CSV Files ###########################

import csv

# Example 1 Write a CSV file

with open("users_info/users.csv", "w", newline='') as users_data:
    csv_writer_data = csv.writer(users_data)

    # row 1 ->>>> table heading
    csv_writer_data.writerow(["User Name", "User Id", "Status"])

    # row 2 ->>>> first row of user data
    csv_writer_data.writerow(["col555", 111, "online"])


# Example 2 Read a CSV file

with open("users_info/users.csv") as users_data:
    csv_writer_data = csv.reader(users_data)
    # print(list(csv_writer_data))

    for data_row in csv_writer_data:
        print("iterator")
        print(data_row)
