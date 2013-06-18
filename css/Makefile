#!/bin/sh

everything.min.css: everything.css
	lessc -x everything.css > everything.min.css

everything.css: normalize.css font-awesome.css style.css
	cat normalize.css font-awesome.css style.css > everything.css
