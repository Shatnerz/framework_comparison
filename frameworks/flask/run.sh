#!/bin/sh

gunicorn app:app --workers=4 --bind=0.0.0.0:13300 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker

