from tortoise import Model, fields
from enum import IntEnum

class TokenType(IntEnum):
    TEZ = 0
    FA12 = 1
    FA2 = 2


class Stream(Model):
    id = fields.IntField(pk=True)
    stream_id = fields.CharField(max_length=10000)
    sender = fields.CharField(max_length=36)
    receiver = fields.CharField(max_length=36)
    deposit = fields.DecimalField(decimal_places=18, max_digits=32)
    rate_per_second = fields.DecimalField(decimal_places=18, max_digits=32)
    remaining_balance = fields.DecimalField(decimal_places=18, max_digits=32)
    start_time = fields.DatetimeField()
    stop_time = fields.DatetimeField()
    created_on = fields.DatetimeField()
    is_active = fields.BooleanField(default=True)
    token = fields.IntEnumField(enum_type=TokenType)

class History(Model):
    id = fields.IntField(pk=True)
    stream = fields.ForeignKeyField('models.Stream', 'history')
    timestamp = fields.DatetimeField()
    amount = fields.DecimalField(decimal_places=18, max_digits=32)