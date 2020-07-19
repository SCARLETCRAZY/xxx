

bot_token = '1356809982:AAEnCcj_QuQE3tOGqTLKncQqqhHTZlJjYjU' # токен бота
LOGIN_BOT = '@snus_pvl_bot' # логин бота
CHANNEL_ID = 1245689 # id канала куда будет отсылаться информация, ид без -100 в начале (например: 124873248)

admin_id = 691058046 # id админа

LOGIN_ADMIN = '@snus_sup' # тг логин спамера, нужен для информации

QIWI_NUMBER = '+77711739551'    # номер киви
QIWI_TOKEN = 'b61884d5c31961bc81a8344ba7bdd301'            # токен киви


PERCENT_SPAM = 0.0  # Процент спамеру (0.5 = 50%) #не работает в версии без спамеров
PERCENT_OWN = 1.0   # Процент вам (0.5 = 50%)

main_bd = '/home/TiredCat/Admin bot/main.db'


info = 'Информация\n' \
'Telegram поддержки @snus_pvl' \

text_purchase = '❕ Вы выбрали: ' \
                '{name}\n\n' \
                '{info}\n\n' \
                '💠 Цена: {price} тенге\n' \
                '💠 Товар: {amount}\n' \
  '💠 Введите ваш адрес после оплаты' \


replenish_balance = '➖➖➖➖➖➖➖➖➖➖➖\n' \
                    '💰 Пополнение баланса\n\n' \
                    '🥝 Оплата киви: \n\n' \
                    '👉 Номер  {number}\n' \
                    '👉 Комментарий  {code}\n' \
                    '👉 Сумма  от 1 до 2000 тенге\n' \
                    '➖➖➖➖➖➖➖➖➖➖➖\n' \

profile = '🧾 Профиль\n\n' \
          '❕ Ваш id - {id}\n' \
          '❕ Ваш логин - {login}\n' \
          '❕ Дата регистрации - {data}\n\n' \
          '💰 Ваш баланс - {balance} тенге'
