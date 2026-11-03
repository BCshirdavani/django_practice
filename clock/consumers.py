import asyncio
import json
from datetime import datetime
from zoneinfo import ZoneInfo

from channels.generic.websocket import AsyncWebsocketConsumer


class ClockConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

        try:
            while True:
                current_time = datetime.now(
                    ZoneInfo("America/Los_Angeles")
                ).strftime("%H:%M:%S")

                await self.send(text_data=json.dumps({
                    "time": current_time
                }))

                await asyncio.sleep(1)

        except asyncio.CancelledError:
            raise
        except OSError:
            # Connection was lost
            pass