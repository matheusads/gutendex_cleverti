from app.database.mongo_engine_con import connect_mongo, disconnect_mongo


def on_application_startup():
    connect_mongo()


def on_application_shutdown():
    disconnect_mongo()
