f = open("my_full_data.txt")
fd = f.read()
data = eval(fd)
f.close()
file = open("my_full_data.txt", "w")


def start_stop():
    '''Accepts a command from the user and calls the required function with the supplied argument.
    Be sure to end the work with the stop command'''

    try:
        result = input("fill up command")
        if "COURSE" in result:
            result_cours = course(result)
            return result_cours
        elif "EXCHANGE" in result:
            result_exchange = exchange(result)
            return result_exchange
        elif result == "STOP":
            raise AssertionError
    except AssertionError:
        file.write(str(data))
        file.close()
        return "SERVICE STOPPED"


def course(result: str) -> tuple or str:
    '''The function returns the exchange rate or says that the wrong currency was entered'''

    if result == "COURSE USD":
        return str(f'rate {data["usd"]}'), str(f'availible {data["available_usd"]}')
    elif result == "COURSE UAH":
        return str(f'rate {data["uah"]}'), str(f'availible {data["available_uah"]}')
    else:
        return f'INVALID CURRENCY {result.split(" ")[-1]}'


def exchange(result: str) -> str:
    '''Function to exchange currency'''
    currency_amount = result.split(" ")[-1]
    exchange_uah = float(currency_amount) / data["usd"]
    exchange_usd = float(currency_amount) * data["uah"]
    if "EXCHANGE UAH" in result:
        if data["available_usd"] >= float(currency_amount) / data["usd"]:
            data["available_usd"] = data["available_usd"] - exchange_uah
            data["available_uah"] = data["available_uah"] + float(currency_amount)
            return f'USD {exchange_uah},RATE {1 / data["usd"]}'
        else:
            return f' UNAVAILABLE, REQUIRED BALANCE USD {float(currency_amount) / data["usd"]}, AVAILABLE {data["available_usd"]}'
    elif "EXCHANGE USD" in result:
        if data["available_uah"] >= float(currency_amount) * data["uah"]:
            data["available_uah"] = data["available_uah"] - exchange_usd
            data["available_usd"] = data["available_usd"] + float(currency_amount)
            return f'UAH {exchange_usd}, RATE {data["uah"]}'
        else:
            return f' UNAVAILABLE, REQUIRED BALANCE UAH {float(currency_amount) * data["uah"]}, AVAILABLE {data["available_uah"]}'


if __name__ == "__main__":
    print(start_stop())
    print(start_stop())
    print(start_stop())
    print(start_stop())
    # file.write(str(data))
