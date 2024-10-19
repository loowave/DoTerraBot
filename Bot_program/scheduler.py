from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from messages import daily_messages


# Function to send the scheduled messages
async def send_daily_message(user_id: int, day: int):
    await daily_messages[day-1](user_id)


# Schedule messages for the next 10 days
def schedule_messages_for_10_days(user_id: int, hour: int, apscheduler: AsyncIOScheduler):
    for day in range(1, 11):
        send_time = datetime.now() + timedelta(days=day)
        send_time = send_time.replace(hour=hour, minute=0, second=0, microsecond=0)
        apscheduler.add_job(send_daily_message, 'date', run_date=send_time, args=[user_id, day])