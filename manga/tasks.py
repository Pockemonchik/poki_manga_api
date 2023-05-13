from time import sleep
from celery import shared_task
import datetime


@shared_task()
def celery_task():
    print("task exec")
    sleep(4)  # Simulate expensive operation(s) that freeze Django
    print("test celery task--------------------------------------------------------------")
    return True
