import time
from celery import shared_task


@shared_task(queue='default') #1
def slow_task():
    print('Started task, processing...')
    time.sleep(120)
    print('Finished Task')
    return True

slow_task.delay() #2