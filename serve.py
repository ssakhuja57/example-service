#!/usr/local/bin/python -u

import os
import json
import web
import socket
import datetime

class hostname:

  def GET(self):
    return json.dumps({'msg': 'hello there from ' + socket.gethostname()})

class env_vars:

  def GET(self):
    return str(os.environ)

class time:

  def GET(self):
    return 'hello, the current time is ' + str(datetime.datetime.now())

class cars:

  def GET(self, car_id):
    j = json.load(open('cars.json'))
    return json.dumps(j[carid])

if __name__ == '__main__':

  ### map uris to classes
  urls = (
    '/', 'hostname',
    '/env', 'env_vars',
    '/time', 'time',
    '/cars/(.*)', 'cars'
  )
  app = web.application(urls, globals())

  ### start http server
  web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', 8080))
