import pytest as pytest
from app.settings import settings
from mongoengine import connect, disconnect


@pytest.fixture(scope="function", autouse=True)
def create_mongo_connection(request):
    host = settings.MONGO_URI.replace("morotech", "")
    database = connect("test", host=host)

    def finalizer():
        database.drop_database("test")
        disconnect()

    request.addfinalizer(finalizer)
