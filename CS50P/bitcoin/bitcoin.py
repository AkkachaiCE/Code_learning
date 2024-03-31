import sys
import requests

#while True:
try:
    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)

    elif float(sys.argv[1]) == False:
        print("Command-line argument is not a number")
        sys.exit(1)

    else:
        #get request
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = r.json()
        rate_float_usd = data["bpi"]["USD"]["rate_float"]
        amount = rate_float_usd * float(sys.argv[1])
        print(f"${amount:,.4f}")

except requests.RequestException:
    ...
