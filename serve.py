#!/usr/local/bin/python -u

import json
import web
import socket


class hello:

  def GET(self):
    return json.dumps({'msg': 'hello hello from ' + socket.gethostname()})


if __name__ == '__main__':

  ### map uris to classes
  urls = (
    '/', 'hello',
  )
  app = web.application(urls, globals())

  ### start http server
  web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', 80))
