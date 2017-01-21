I have nothing better to do, so what the hell.

Benchmarks
==========

+------------+---------------------------+----------------+---------------+
| Server     | Implementation            | Requests/sec   | Avg Latency   |
+============+===========================+================+===============+
| Sanic_     | Python 3.5 + uvloop       | 42,162         | 2.40ms        |
+------------+---------------------------+----------------+---------------+
| Flask_     | Python 2.7 (gunicorn)     | 11,184         | 9.67ms        |
+------------+---------------------------+----------------+---------------+
| aiohttp    | Python 3.5 + uvloop       | 8,864          | 11.29ms       |
+------------+---------------------------+----------------+---------------+
| rhc_       | Python 2.7                | 7,357          | 21.25ms       |
+------------+---------------------------+----------------+---------------+
| Flask_     | Python 2.7 (no gunicorn)  | 992            | 45.22ms       |
+------------+---------------------------+----------------+---------------+

.. _Sanic: https://github.com/channelcat/sanic
.. _Flask: https://github.com/pallets/flask
.. rhc: https://github.com/robertchase/rhc


Raw Output
==========

Sanic
-----

    wrk -t4 -c100 -d30s http://localhost:13300/

::
    Running 30s test @ http://localhost:13300/
      4 threads and 100 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     2.40ms  775.10us  20.33ms   91.45%
        Req/Sec    10.59k   648.63    13.42k    83.50%
      1266187 requests in 30.03s, 159.39MB read
    Requests/sec:  42162.07
    Transfer/sec:      5.31MB


Flask (No gunicorn)
-------------------

    wrk -t4 -c100 -d30s http://localhost:13300/

::
    Running 30s test @ http://localhost:13300/
      4 threads and 100 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    45.22ms    4.94ms  96.10ms   90.72%
        Req/Sec   538.47     83.06   730.00     76.80%
      29867 requests in 30.10s, 4.76MB read
      Socket errors: connect 100, read 0, write 0, timeout 0
    Requests/sec:    992.42
    Transfer/sec:    161.85KB


Flask (gunicorn)
----------------

    wrk -t4 -c100 -d30s http://localhost:13300/

::
    Running 30s test @ http://localhost:13300/
      4 threads and 100 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     9.67ms    6.28ms  90.78ms   91.71%
        Req/Sec     2.81k   382.14     3.69k    71.83%
      335726 requests in 30.02s, 56.03MB read
    Requests/sec:  11183.79
    Transfer/sec:      1.87MB


aiohttp
--------

    wrk -t4 -c100 -d30s http://localhost:13300/

::
    Running 30s test @ http://localhost:13300/
      4 threads and 100 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    11.29ms    1.32ms  47.05ms   95.42%
        Req/Sec     2.23k   114.43     2.51k    83.50%
      266041 requests in 30.01s, 39.33MB read
    Requests/sec:   8863.93
    Transfer/sec:      1.31MB


rhc
---

    wrk -t4 -c100 -d30s http://localhost:13300/
    
::
    Running 30s test @ http://localhost:13300/
      4 threads and 100 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    21.25ms   91.03ms   1.77s    98.79%
        Req/Sec     1.88k   453.93     6.00k    92.72%
      220808 requests in 30.02s, 28.85MB read
      Socket errors: connect 0, read 0, write 0, timeout 11
    Requests/sec:   7356.50
    Transfer/sec:      0.96MB
