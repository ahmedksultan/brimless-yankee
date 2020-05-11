try:
  fp = open('data/global-terrorism.csv','r')
  s = fp.read()
  fp.close()
  if '\r\n' in s:
    lines = s.split('\r\n')
  else:
    lines = s.split('\n')
  print("works!")
except:
  print ("Dunno where global-terrorism.csv is, but it ain't here.")
