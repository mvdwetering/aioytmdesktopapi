# YouTube Music Desktop Remote Control API

Async IO API package for [YouTube Music Desktop app](https://ytmdesktop.app/).

## Installation

```bash
python3 -m pip install aioytmdesktopapi
```

## Contents

This package contains the `YtmDesktop` class which represents the API.
Check the [API documentation](https://github.com/ytmdesktop/ytmdesktop/wiki/Remote-Control-API) to see what functionality is available and how to use it.


## Example usage

Check `example.py` for a runnable example.

```python

async with aiohttp.ClientSession() as session:
    async with YtmDesktop(session, "192.168.1.123", password="PASSWORD") as ytmdesktop:
        # Initialize first before using any of the functionality
        await ytmdesktop.initialize()

        # Print status of some attributes
        print(f"{ytmdesktop.player.has_song=}")
        print(f"{ytmdesktop.player.is_paused=}")
        print(f"{ytmdesktop.track.author=}")
        print(f"{ytmdesktop.track.title=}")
        print(f"{ytmdesktop.track.album=}")

        # Pause the current track
        await ytmdesktop.send_command.track_pause()
        # Call `.update()` to update the internal state of the API with the state of the actual player instance
        await ytmdesktop.update()
        # Print updated state
        print(f"{ytmdesktop.player.is_paused=}")

        time.sleep(2)

        # Play the current track
        await ytmdesktop.send_command.track_play()
        # Call `.update()` to update the internal state of the API with the state of the actual player instance
        await ytmdesktop.update()
        # Print updated state
        print(f"{ytmdesktop.player.is_paused=}")
```
