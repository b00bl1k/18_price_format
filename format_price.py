import sys


def format_price(price):
    try:
        price = float(price)
    except ValueError:
        return None
    except TypeError:
        return None

    if price.is_integer():
        price_str = "{0:,.0f}".format(price)
    else:
        price_str = "{0:,.2f}".format(price)

    return price_str.replace(",", " ")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Argument error.\nUsage: python format_price.py <value>")
    formatted_price = format_price(sys.argv[1])
    if formatted_price:
        print(formatted_price)
    else:
        sys.exit("Invalid value")
