class Coin:
    def __init__(self, symbol, name, rank, price, day_change, hour_change, cap):
        self.__symbol = symbol
        self.__name = name
        self.__rank = rank
        self.__price = price
        self.__day_change = day_change
        self.__hour_change = hour_change
        self.__cap = cap

    def get_symbol(self):
        return self.__symbol

    def get_name(self):
        return self.__name

    def get_rank(self):
        return self.__rank

    def get_price(self):
        return self.__price

    def get_day_change(self):
        return self.__day_change

    def get_hour_change(self):
        return self.__hour_change

    def get_cap(self):
        return self.__cap

# id, symbol, name, nameid,	rank, price_usd, percent_change_24h, percent_change_1h, percent_change_7d, price_btc, market_cap_usd, volume24, volume24a, csupply, tsupply, msupply
# 0,    1,      2,     3,     4,       5,            6,                  7,                 8,              9,          10,            11,      12,       13,      14,     15
