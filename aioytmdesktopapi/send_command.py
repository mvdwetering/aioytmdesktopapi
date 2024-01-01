from .constants import RepeatType


class SendCommand:
    def __init__(
        self,
        request,
    ) -> None:
        self._request = request

    async def _send_command(self, command, value=None):
        data = {"command": command}
        if value:
            data["value"] = value
        await self._request("POST", "", data=data)

    async def show_lyrics_hidden(self):
        """Open hidden lyrics window to provide data"""
        await self._send_command("show-lyrics-hidden")

    async def track_play(self):
        """Play music"""
        await self._send_command("track-play")

    async def track_pause(self):
        """Pause music"""
        await self._send_command("track-pause")

    async def track_next(self):
        """Next track"""
        await self._send_command("track-next")

    async def track_previous(self):
        """Previous track"""
        await self._send_command("track-previous")

    async def track_thumbs_up(self):
        """Like current track"""
        await self._send_command("track-thumbs-up")

    async def track_thumbs_down(self):
        """Dislike current track"""
        await self._send_command("track-thumbs-down")

    async def player_volume_up(self):
        """Increase the player volume"""
        await self._send_command("player-volume-up")

    async def player_volume_down(self):
        """Decrease the player volume"""
        await self._send_command("player-volume-down")

    async def player_forward(self):
        """Forward 10 seconds"""
        await self._send_command("player-forward")

    async def player_rewind(self):
        """Rewind 10 seconds"""
        await self._send_command("player-rewind")

    async def player_repeat(self, repeat_mode: RepeatType):
        """Toggle NONE or ONE or ALL"""
        await self._send_command("player-repeat", repeat_mode)

    async def player_shuffle(self):
        """Shuffle queue"""
        await self._send_command("player-shuffle")

    async def player_add_library(self):
        """Add track to library"""
        await self._send_command("player-add-library")

    async def player_add_playlist(self, playlist_index):
        """Add track to playlist (Needs value: Playlist index)"""
        await self._send_command("player-add-playlist", playlist_index)

    async def player_set_seekbar(self, value):
        """Set value for seekbar (Needs value: 0 ~ Track duration)"""
        await self._send_command("player-set-seekbar", value)

    async def player_set_volume(self, value):
        """Set value for volume (Needs value: 0 ~ 100)"""
        await self._send_command("player-set-volume", value)

    async def player_set_queue(self, value):
        """Set index of queue to play track (Needs value: 0 ~ Queue length)"""
        await self._send_command("player-set-queue", value)
