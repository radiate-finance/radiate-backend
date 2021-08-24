from typing import Optional

from dipdup.models import OperationData, Origination, Transaction
from dipdup.context import HandlerContext

import radiate.models as models

from radiate.types.radiate.parameter.cancel_stream import CancelStreamParameter
from radiate.types.radiate.storage import RadiateStorage


async def on_cancel(
    ctx: HandlerContext,
    cancel_stream: Transaction[CancelStreamParameter, RadiateStorage],
) -> None:
    streamID = str(cancel_stream.parameter.__root__)
    
    stream = (await models.Stream.filter(stream_id=streamID))[0]
    stream.is_active = False
    await stream.save()