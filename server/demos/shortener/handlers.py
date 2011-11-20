import webapp2
import jinja2
import os
import json
from google.appengine.api import urlfetch
import logging
import handlers

class PageHandler(handlers.PageHandler):
  """
  The handler for the Shortener app 
  """

class ShortenHandler(webapp2.RequestHandler):
  def post(self):
    logging.info("in request")
    url = "https://www.googleapis.com/urlshortener/v1/url"
    headers = { "Content-Type": "application/json" }
    payload = { "key": "AIzaSyAl280d28vAJd_6431Uc0N5AwHMowThy8c",  "longUrl": "%s" % self.request.get("url") }
    fetchdata = urlfetch.fetch(url, method = "POST", headers = headers, payload = json.dumps(payload) )
    self.response.headers['Content-type'] = fetchdata.headers['Content-type']
    self.response.set_status(fetchdata.status_code)
    self.response.out.write(fetchdata.content)
    
