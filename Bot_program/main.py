import asyncio
import logging

import handlers
from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.redis import RedisJobStore
from apschedulermiddleware import SchedulerMiddleware
from logging.handlers import TimedRotatingFileHandler
from logging import Formatter

# create handler
handler = TimedRotatingFileHandler(filename='runtime.log', when='D', interval=1, backupCount=90, encoding='utf-8', delay=False)

# create formatter and add to handler
formatter = Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logging.basicConfig(level=logging.DEBUG, handlers=[handler])

jobstores = {
    'default': RedisJobStore(
        jobs_key='apscheduler.jobs',
        run_times_key='apscheduler.run_times',
        host='localhost',
        port=6379,
        db=1,  # Use Redis database 1 for job store
    )
}

scheduler = AsyncIOScheduler(jobstores=jobstores)

BOT_TOKEN = ''
bot = Bot(token=BOT_TOKEN)

async def main():
    scheduler.start()
    handlers.dp.update.middleware.register(SchedulerMiddleware(scheduler))
    try:
        await handlers.dp.start_polling(bot)
    finally:
        await handlers.dp.storage.close()
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())