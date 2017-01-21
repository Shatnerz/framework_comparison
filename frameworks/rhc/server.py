"""Everything needed for a simple rhc server."""

from __future__ import print_function


def setup(config):
    print("Starting")
    print(config)


def teardown():
    'Teardown'


def test(request):
    return {"test": True}
