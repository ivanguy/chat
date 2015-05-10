from http.client import HTTPConnection as Connect

con = Connect('46.101.152.181:8080')

nick = input('nick=')
header = {'Content-type': 'text/plain'}
con.request('POST','',bytes(nick, 'utf-8'), header)
con.close()
