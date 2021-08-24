from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import radiate.models as models

from radiate.types.radiate.parameter.withdraw import WithdrawParameter
from radiate.types.radiate.storage import RadiateStorage


async def on_withdraw(
    ctx: HandlerContext,
    withdraw: Transaction[WithdrawParameter, RadiateStorage],
) -> None:
    amount = withdraw.parameter.amount
    streamID = withdraw.parameter.streamId
    
    stream = (await models.Stream.filter(stream_id=streamID))[0]
    stream.remaining_balance -= int(amount)
    if stream.remaining_balance == 0:
        stream.is_active = False
    await stream.save()

    history = models.History(
        stream = stream,
        timestamp = withdraw.data.timestamp,
        amount = amount
    )
    await history.save()


    