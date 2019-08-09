"""Create nested CLI tools."""

import click

from underground.cli import feed, stops


@click.group()
def entry_point():
    """Command line handlers for MTA realtime data."""


entry_point.add_command(stops.main, name="stops")
entry_point.add_command(feed.main, name="feed")
