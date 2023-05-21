from aiogram import Dispatcher, types

async def set_main_menu(dp: Dispatcher):
    # Создаем список с командами для кнопки menu
    main_menu_commands = [
        types.BotCommand(command='/start', description='Начать работу'),
        types.BotCommand(command='/pay', description='Страница оплаты'),
        types.BotCommand(command='/contacts', description='Контакты и страницы авторов'),
        types.BotCommand(command='/reviews', description='Отзывы клиентов')
    ]
    await dp.bot.set_my_commands(main_menu_commands)