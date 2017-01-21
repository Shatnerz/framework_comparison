# Straight from the sanic repo in tests/performance/sanic

import sys

from sanic import Sanic
from sanic.response import json

app = Sanic("test")


@app.route("/")
async def test(request):
    return json({"test": True})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=sys.argv[1])
