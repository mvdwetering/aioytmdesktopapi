#!/usr/bin/env python3

import argparse
import logging
import asyncio
import time
import aiohttp

from aioytmdesktopapi import YtmDesktop


async def main(args):

    async with aiohttp.ClientSession() as session:
        async with YtmDesktop(session, args.host, password=args.password) as ytmdesktop:
            await ytmdesktop.initialize()
            print(f"{ytmdesktop.player.has_song=}")
            print(f"{ytmdesktop.player.is_paused=}")
            print(f"{ytmdesktop.track.author=}")
            print(f"{ytmdesktop.track.title=}")
            print(f"{ytmdesktop.track.album=}")

            await ytmdesktop.send_command.track_pause()
            await ytmdesktop.update()
            print(f"{ytmdesktop.player.is_paused=}")

            time.sleep(2)

            await ytmdesktop.send_command.track_play()
            await ytmdesktop.update()
            print(f"{ytmdesktop.player.is_paused=}")


if __name__ == "__main__":

    ## Commandlineoptions
    parser = argparse.ArgumentParser(
        description="Example application for aioytmdesktopapi."
    )

    parser.add_argument(
        "host", help="Hostname or IP Address of the YouTube Music Desktop instance"
    )
    parser.add_argument(
        "--password", help="Password for the YouTube Music Desktop instance"
    )
    parser.add_argument(
        "--loglevel",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default="INFO",
        help="Define loglevel, default is INFO.",
    )

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(args))

    loop.close()
