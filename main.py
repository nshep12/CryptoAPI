import Coin
import requests
import csv
import json

# I spent way too much time banging my head against openweather to understand why their json output is formatted the way it is.

def get_file_name():
    print("\nWelcome to CoinBox!\n")
    file_name = (input("What is the file name you wish to process? "))
    return file_name


def get_data():
    url = "https://api.coinlore.net/api/tickers/"
    coin_data = requests.get(url).json()
    json_string = json.dumps(coin_data)
    with open('json_data.json', 'w') as outfile:
        outfile.write(json_string)


def json_to_csv():
    with open('json_data.json') as json_file:
        data = json.load(json_file)
    name = data["data"]
    write_file = open('file.csv', 'w', newline='')
    csv_writer = csv.writer(write_file)
    count = 0
    for i in name:
        if count == 0:
            header = i.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(i.values())

    # write_file.close()


def load_class(file):
    main_list = []

    # Read CSV file
    with open(file, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for row in reader:
            symbol = row[1]
            name = row[2]
            rank = row[4]
            price = row[5]
            day_change = row[6]
            hour_change = row[7]
            cap = row[10]

            coin = Coin.Coin(symbol, name, rank, price, day_change, hour_change, cap)
            main_list.append(coin)
    return main_list


def full_report(coin_list):
    for coin in coin_list:
        print("----------\nCoin: " + coin.get_name() + "\nRank: " + coin.get_rank() + "\nPrice: " + coin.get_price() + "\nCap: " + coin.get_cap())


def percent_change_1_hour(main_list):
    biggest = 0
    change_list = []
    for coin in main_list:
        change = float(coin.get_hour_change())
        if change > biggest:
            change_list.clear()
            biggest = change
            change_list.append(coin)
        elif change == biggest:
            change_list.append(coin)

    for i in change_list:
        print(f"{i.get_name()} had the biggest change in the last hour of {i.get_hour_change()}%\n")


def percent_change_24_hour(main_list):
    biggest = 0
    change_list = []
    for coin in main_list:
        change = float(coin.get_day_change())
        if change > biggest:
            change_list.clear()
            biggest = change
            change_list.append(coin)
        elif change == biggest:
            change_list.append(coin)

    for i in change_list:
        print(f"{i.get_name()} had the biggest change in the last 24 hours of {i.get_day_change()}%\n")


def main():
    get_data(), json_to_csv()
    file = get_file_name()

    main_list = load_class(file)

    count = len(main_list)
    list_count = str(count)

    while True:
        print("Welcome to the CoinBox!")
        response = (input("What would you like to do?\n1. Full list report (" + list_count + " items)" + "\n2. Biggest change in the last hour\n3. Biggest change in the last 24 hours\n4. Exit\n"))

        if response == "1":
            full_report(main_list)
        elif response == "2":
            percent_change_1_hour(main_list)
        elif response == "3":
            percent_change_24_hour(main_list)
        else:
            print("Thank you, goodbye!")
            return

        another = input("\nWould you like to view the file again? (y/n) ")
        if another != "y":
            print("Thank you, goodbye!")
            break


main()

# API_Key = 'c476e14a89ac64b8609bf8cb6d811d1b'

# city = input("Enter a city: ")

# url = "http://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+city


# get data, write to file

# weather_data = requests.get(url).json()
# json_string = json.dumps(weather_data)

#
# read_json = json.loads(json_string)
#
# print(json_string)
#
# pprint(weather_data)
# pprint(coin_data)



# read_file = r'C:\Users\Nick\Desktop\FinalProject\json_data.json'
# out_file = r"C:\Users\Nick\Desktop\FinalProject\file.csv"

# read_json_string = json.loads(json_string)
#
# print(read_json_string)


# df = pd.read_json(r'C:\Users\Nick\Desktop\FinalProject\json_data.json')
# df.to_csv(r'C:\Users\Nick\Desktop\FinalProject\file.csv', index=None)

# open json file convert to csv

# for i in weather_data:
#     weather_dict = {"a": weather_data[0]}
# weather_dict.append("a": weather_data[0])
# file = open("file.csv", "w")
# csvfile = csv.writer(file)
# csvfile.writerow(weather_data[0].keys())
# for row in weather_data:
#     weather_data.writerow(row.values())
# file.close()




