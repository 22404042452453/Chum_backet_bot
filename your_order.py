
def pay_orders(order):
    text = ''
    prices = {"one_pizza" : "1.99$",
             "two_pizza": "3.5$",
             "three_pizza": "4.99$",
              "light_beer": "2$",
              "dark_beer" : "4$",
              "white_beer": "3.5$",
              'red_smile' : "2$",
              'blue_smile': "3$",
              'yellow_smile': "4$" }
    total_price = 0
    for i in order:
        total_price += float(prices.get(i).replace("$",''))
        text += f"{i} по цене {prices.get(i)}\n"
    total_price = f"К оплате {total_price}$"
    text = text + '\n' + total_price
    return text

