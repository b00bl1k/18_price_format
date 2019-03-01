import re
import sys


def format_price(price):
    if isinstance(price, (int, float)) or \
            (isinstance(price, str) and
             re.match(r"\d+(\.\d+)?", price)):
        price = float(price)
    else:
        raise ValueError("Invalid value")

    if price.is_integer():
        price_str = "{0:,.0f}".format(price)
    else:
        price_str = "{0:,.2f}".format(price)

    return price_str.replace(",", " ")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Argument error.\nUsage: python format_price.py <value>")
    print(format_price(sys.argv[1]))
