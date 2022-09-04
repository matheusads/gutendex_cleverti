from functools import partial

from app.settings import settings
from mongoengine import connect, disconnect

connect_mongo = partial(connect, host=settings.MONGO_URI)
disconnect_mongo = disconnect
