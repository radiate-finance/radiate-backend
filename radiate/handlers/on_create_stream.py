from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import radiate.models as models

from radiate.types.radiate.parameter.create_stream import CreateStreamParameter
from radiate.types.radiate.storage import RadiateStorage, TokenItem, TokenItem1


async def on_create_stream(
    ctx: HandlerContext,
    create_stream: Transaction[CreateStreamParameter, RadiateStorage],
) -> None:
    sender = create_stream.data.sender_address
    # temp = await models.Stream()
    id = str((await models.Stream.filter().count()))
    receiver = create_stream.storage.streams[id].receiver
    startTime = create_stream.storage.streams[id].startTime
    stopTime = create_stream.storage.streams[id].stopTime
    ratePerSecond = create_stream.storage.streams[id].ratePerSecond
    deposit = create_stream.storage.streams[id].deposit
    createdOn = create_stream.data.timestamp
    remainingBalance = deposit
    token = models.TokenType.TEZ
    if create_stream.parameter.token == TokenItem:
        token = models.TokenType.FA12
    elif create_stream.parameter.token == TokenItem1:
        token = models.TokenType.FA2
    
    stream = models.Stream(
        stream_id = id,
        sender = sender,
        receiver = receiver,
        deposit = deposit,
        start_time = startTime,
        stop_time = stopTime,
        created_on = createdOn,
        rate_per_second = ratePerSecond,
        remaining_balance = remainingBalance,
        token = token,
        is_active = True,
    )
    await stream.save()
