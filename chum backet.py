import telebot
from my_token import token
from your_order import pay_orders

bot = telebot.TeleBot(token=token)
# url pictures from networks
start_url = "https://avatars.mds.yandex.net/i?id=7c381b79d88a6251df27313913a03560-5856211-images-thumbs&n=13"
menu_url = "https://avatars.mds.yandex.net/i?id=c1bb314ac16cd88817d3048d80d27531-4012553-images-thumbs&n=13"
pizza_url = "https://catherineasquithgallery.com/uploads/posts/2021-02/1614404404_54-p-pitstsa-na-temnom-fone-73.jpg"
beer_url = "https://avatars.mds.yandex.net/i?id=e101f5a5ea0ee3145a06110dc4c216db-5865731-images-thumbs&n=13"
slime_url = 'https://static.tildacdn.com/tild6465-3638-4266-b538-333333363161/photo.jpg'
are_you_sure_url = "https://www.nairaland.com/attachments/5222969_img20170423161958_jpeg99865bdc515da489e67dd9a45b3822a5"
order_success_url = 'https://avatars.mds.yandex.net/i?id=b19f281ac0a10da87edf0b93a03138ae-5268458-images-thumbs&n=13'
mistake_url = 'https://www.ajoure-men.de/wp-content/uploads/2017/01/YouTube-Tools.jpg'
pay_url = "https://www.dw4you.ru/image/catalog/icons/oplata.png"

my_order = []


@bot.message_handler(commands=['start', 'info'])
def start(message):
    start_keyboard = telebot.types.InlineKeyboardMarkup()
    Menu = telebot.types.InlineKeyboardButton(text='Меню', callback_data='Menu')
    start_keyboard.add(Menu)
    bot.send_photo(message.chat.id, start_url, caption="Вас приветствует сеть ресторанов Сhum_backet\n"
                                                       f"{message.from_user.first_name} к сожалению данный бот ничего не умеет и "
                                                       "написан для оттачивания моих навыков!!!",
                   reply_markup=start_keyboard)


@bot.callback_query_handler(func=lambda x: x.data)
def menu(callback):
    global my_order

    try:
        if callback.data == 'Menu':
            menu_board = telebot.types.InlineKeyboardMarkup()
            pizza = telebot.types.InlineKeyboardButton(text='pizza', callback_data='pizza')
            beer = telebot.types.InlineKeyboardButton(text='beer', callback_data="beer")
            slime = telebot.types.InlineKeyboardButton(text='slime', callback_data="slime")
            menu_board.add(pizza, beer, slime)
            bot.send_photo(callback.message.chat.id, menu_url, caption="Что желаете заказать ???",
                           reply_markup=menu_board)


        # PIZZA CODE

        elif callback.data == 'pizza':
            pizza_board = telebot.types.InlineKeyboardMarkup()
            one = telebot.types.InlineKeyboardButton(text='one', callback_data='one_pizza')
            two = telebot.types.InlineKeyboardButton(text='two', callback_data='two_pizza')
            three = telebot.types.InlineKeyboardButton(text='three', callback_data='three_pizza')
            back = telebot.types.InlineKeyboardButton(text='back_to_menu', callback_data='back_to_menu')
            pizza_board.add(one, two, three, back)
            bot.send_photo(callback.message.chat.id, pizza_url, caption="Укажите количество пицц",
                           reply_markup=pizza_board)


        elif callback.data == 'back_to_menu':
            menu_board = telebot.types.InlineKeyboardMarkup()
            pizza = telebot.types.InlineKeyboardButton(text='pizza', callback_data='pizza')
            beer = telebot.types.InlineKeyboardButton(text='beer', callback_data="beer")
            slime = telebot.types.InlineKeyboardButton(text='slime', callback_data="slime")
            menu_board.add(pizza, beer, slime)
            bot.send_photo(callback.message.chat.id, menu_url, caption="Что желаете заказать ???",
                           reply_markup=menu_board)

        elif callback.data in ['one_pizza', 'two_pizza', 'three_pizza']:
            my_order.append(callback.data)
            answer = telebot.types.InlineKeyboardMarkup()
            yes = telebot.types.InlineKeyboardButton(text='YES', callback_data='yes')
            no = telebot.types.InlineKeyboardButton(text='NO', callback_data='no_pizza')
            answer.add(yes, no)
            bot.send_photo(callback.message.chat.id, are_you_sure_url, caption=" Вы уверенены в заказе ???",
                           reply_markup=answer)

        elif callback.data == "no_pizza":
            pizza_board = telebot.types.InlineKeyboardMarkup()
            one = telebot.types.InlineKeyboardButton(text='one', callback_data='one_pizza')
            two = telebot.types.InlineKeyboardButton(text='two', callback_data='two_pizza')
            three = telebot.types.InlineKeyboardButton(text='three', callback_data='three_pizza')
            back = telebot.types.InlineKeyboardButton(text='back_to_menu', callback_data='back_to_menu')
            pizza_board.add(one, two, three, back)
            bot.send_photo(callback.message.chat.id, pizza_url, caption="Укажите количество пицц",
                           reply_markup=pizza_board)
            my_order.pop(-1)
        # Pay code
        elif callback.data == "yes":
            markup_order = telebot.types.InlineKeyboardMarkup()
            dop_order = telebot.types.InlineKeyboardButton(text="Да, я хочу заказать  что-то еще", callback_data='add')
            pay_order = telebot.types.InlineKeyboardButton(text="Перейти к оплате", callback_data='pay')
            markup_order.add(dop_order, pay_order)
            bot.send_photo(callback.message.chat.id, order_success_url,
                           caption="Поздравляем, ваш заказ оформлен", reply_markup=markup_order)

        elif callback.data == "add":
            menu_board = telebot.types.InlineKeyboardMarkup()
            pizza = telebot.types.InlineKeyboardButton(text='pizza', callback_data='pizza')
            beer = telebot.types.InlineKeyboardButton(text='beer', callback_data="beer")
            slime = telebot.types.InlineKeyboardButton(text='slime', callback_data="slime")
            menu_board.add(pizza, beer, slime)
            bot.send_photo(callback.message.chat.id, menu_url, caption="Что желаете заказать ???",
                           reply_markup=menu_board)

        elif callback.data == "pay":
            bot.send_photo(callback.message.chat.id, pay_url, caption=pay_orders(my_order))
            my_order = []


        # Code SMILE
        elif callback.data == 'slime':
            smile_board = telebot.types.InlineKeyboardMarkup()
            red = telebot.types.InlineKeyboardButton(text='red', callback_data='red_smile')
            blue = telebot.types.InlineKeyboardButton(text='blue', callback_data='blue_smile')
            yellow = telebot.types.InlineKeyboardButton(text='yellow', callback_data='yellow_smile')
            back = telebot.types.InlineKeyboardButton(text='back_to_menu', callback_data='back_to_menu')
            smile_board.add(red, yellow, blue, back)
            bot.send_photo(callback.message.chat.id, slime_url, caption="Укажите цвет вашего slime",
                           reply_markup=smile_board)

        elif callback.data in ['red_smile', 'blue_smile', 'yellow_smile']:
            my_order.append(callback.data)
            answer = telebot.types.InlineKeyboardMarkup()
            yes = telebot.types.InlineKeyboardButton(text='YES', callback_data='yes')
            no = telebot.types.InlineKeyboardButton(text='NO', callback_data='no_smile')
            answer.add(yes, no)
            bot.send_photo(callback.message.chat.id, are_you_sure_url, caption=" Вы уверенены в заказе ???",
                           reply_markup=answer)

        elif callback.data == 'no_smile':
            my_order.pop(-1)
            smile_board = telebot.types.InlineKeyboardMarkup()
            red = telebot.types.InlineKeyboardButton(text='red', callback_data='red_smile')
            blue = telebot.types.InlineKeyboardButton(text='blue', callback_data='blue_smile')
            yellow = telebot.types.InlineKeyboardButton(text='yellow', callback_data='yellow_smile')
            back = telebot.types.InlineKeyboardButton(text='back_to_menu', callback_data='back_to_menu')
            smile_board.add(red, yellow, blue, back)
            bot.send_photo(callback.message.chat.id, slime_url, caption="Укажите цвет вашего slime",
                           reply_markup=smile_board)


        # Code BEER

        elif callback.data == "beer":
            beer_board = telebot.types.InlineKeyboardMarkup()
            light = telebot.types.InlineKeyboardButton(text='light', callback_data='light_beer')
            dark = telebot.types.InlineKeyboardButton(text='dark', callback_data='dark_beer')
            white = telebot.types.InlineKeyboardButton(text='white', callback_data='white_beer')
            back = telebot.types.InlineKeyboardButton(text='back_to_menu', callback_data='back_to_menu')
            beer_board.add(light, dark, white, back)
            bot.send_photo(callback.message.chat.id, beer_url, caption="Выберите ваше beer\n"
                                                                       "!!! Чрезмерное употребление алкоголя вредит вашему здоровью !!!",
                           reply_markup=beer_board)

        elif callback.data in ['light_beer', 'dark_beer', 'white_beer']:
            my_order.append(callback.data)
            answer = telebot.types.InlineKeyboardMarkup()
            yes = telebot.types.InlineKeyboardButton(text='YES', callback_data='yes')
            no = telebot.types.InlineKeyboardButton(text='NO', callback_data='no_beer')
            answer.add(yes, no)
            bot.send_photo(callback.message.chat.id, are_you_sure_url, caption=" Вы уверенены в заказе ???",
                           reply_markup=answer)

        elif callback.data == 'no_beer':
            my_order.pop(-1)
            beer_board = telebot.types.InlineKeyboardMarkup()
            light = telebot.types.InlineKeyboardButton(text='light', callback_data='light_beer')
            dark = telebot.types.InlineKeyboardButton(text='dark', callback_data='dark_beer')
            white = telebot.types.InlineKeyboardButton(text='white', callback_data='callback.data')
            back = telebot.types.InlineKeyboardButton(text='back_to_menu', callback_data='back_to_menu')
            beer_board.add(light, dark, white, back)
            bot.send_photo(callback.message.chat.id, beer_url, caption="Выберите ваше beer\n"
                                                                       "!!!Чрезмерное употребление алкоголя вредит вашему здоровью!!!",
                           reply_markup=beer_board)

        else:
            bot.send_photo(callback.message.chat.id, mistake_url)

    except Exception as Ex:
        bot.send_photo(callback.message.chat.id, mistake_url, caption="Please check your networks")


bot.polling(non_stop=True)
