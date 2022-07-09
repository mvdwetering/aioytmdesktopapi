import logging
from typing import Dict, Optional

import aiohttp

from .player import Player
from .send_command import SendCommand
from .track import Track
from .errors import RequestError, Unauthorized

logger = logging.getLogger(__name__)


class YtmDesktop:
    """Control a YouTube Music Desktop app instance."""

    def __init__(
        self,
        clientsession,
        host: str,
        password: Optional[str] = None,
    ) -> None:
        self._host = host
        self._password = password
        self._clientsession = clientsession

        # API endpoints
        self.player = None
        self.track = None
        self.send_command = SendCommand(self.request)

    @property
    def host(self):
        return self._host

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.close()

    async def initialize(self):
        await self.update()

    async def close(self):
        pass

    async def update(self):
        response = await self.request("get", "")
        if response:
            self.player = Player(response["player"], self.request)
            self.track = Track(response["track"], self.request)

    async def request(self, method: str, path: str, data: Optional[Dict] = None):
        """Make a request to the API."""

        if self._clientsession.closed:
            # Avoid runtime errors when connection is closed.
            # This solves an issue when Updates were scheduled and HA was shutdown
            return None

        url = f"http://{self._host}:9863/query{path}"

        try:
            logger.debug("%s, %s, %s" % (method, url, data))

            headers = {"Content-Type": "application/json"}
            if self._password:
                headers["Authorization"] = f"Bearer {self._password}"

            async with self._clientsession.request(
                method, url, json=data, headers=headers
            ) as resp:
                logger.debug("%s, %s" % (resp.status, await resp.text("utf-8")))
                if resp.status == 400:
                    raise Unauthorized("{}: {}".format(resp.status, resp.text))
                if resp.status != 200:
                    raise RequestError("{}: {}".format(resp.status, resp.text))
                return await resp.json(content_type="text/json")
        except aiohttp.client_exceptions.ClientError as err:
            raise RequestError(
                "Error requesting data from {}: {}".format(self._host, err)
            ) from None
