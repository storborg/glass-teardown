#!/bin/sh

all.min.css: all.css
	lessc -x all.css > all.min.css

all.css: normalize.css font-awesome.css style.css
	cat normalize.css font-awesome.css style.css > all.css
