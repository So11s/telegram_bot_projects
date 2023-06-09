from aiogram import Bot
from aiogram.types import BotCommand


async def set_main_menu(bot: Bot):
    main_menu_commands = [BotCommand(command='/start',
                                     description='Начало работы бота'),
                          BotCommand(command='/help',
                                     description='Справка по работе бота'),
                          BotCommand(command='/support',
                                     description='Поддержка')]
    await bot.set_my_commands(main_menu_commands)
