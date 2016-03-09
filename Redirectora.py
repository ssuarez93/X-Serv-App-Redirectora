#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sistemas Teleco. Sara Suárez.

import WebApp
import random

class Redirectora(WebApp.webApp):
    def process(self, parsedRequest):
        aleatorio = random.randint(1, 1000000)
        URL = "http://localhost:1234/" + str(aleatorio)

        htmlAnswer = '<html><body><font size=6><font face=Comic Sans MS> Hola! Vas a ser redirigido a ' + \
                     '<a href=' + URL + '>' + URL + '</a></p>' + \
                     '<meta http-equiv="refresh" content="3; url=' + URL + '" />'
        return("307 Temporary Redirect", htmlAnswer)

if __name__ == "__main__":
    try:
        servidor= Redirectora("localhost", 1234)
    except KeyboardInterrupt:
    	print "Closing binded socket"
