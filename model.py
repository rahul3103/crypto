import os
import datetime
from peewee import Model, PostgresqlDatabase, CharField, DateTimeField,\
    DoubleField, TextField, BigIntegerField
from playhouse.postgres_ext import BinaryJSONField
from playhouse.db_url import connect
from playhouse.shortcuts import model_to_dict
import settings

if os.environ.get('DATABASE_URL'):
    db = connect(os.environ.get('DATABASE_URL'))
else:
    db = PostgresqlDatabase(
        settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASS,
        host=settings.DB_HOST,
    )


class BaseModel(Model):
    class Meta:
        database = db

    def to_dict(self, exclude=[]):
        return model_to_dict(self, recurse=False, exclude=exclude)


class Crypto(BaseModel):
    coin = CharField()
    trade_values = BinaryJSONField(default={})
    cdate = DateTimeField(default=datetime.datetime.now)
