import glob


tmpl = '''
<a class="image image-bordered" href="%(title)s.jpg">
  <img src="%(filename)s" alt="" title="">
</a>'''


for fn in glob.glob('appointment/*-tiny.jpg'):
    title = fn.split('.')[0].rsplit('-', 1)[0]
    print tmpl % dict(title=title, filename=fn)
