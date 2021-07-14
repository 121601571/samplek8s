import web
import redis
import json
urls = (
    '/', 'hello',
    '/add','addvalue',
    '/show', 'showvalue',
)
app = web.application(urls, globals())
def getCon():
    r = redis.Redis(host='my-redis', port=6379, db=0)
    return r
class addvalue:
    def GET(self):
        r = getCon()
        res = r.get('val')

        if res:
            res = int(res)
            res += 1
            r.set('val', res)
        else:
            res = 0
            res += 1
            r.set('val', res)


        return json.dumps({'val': res})

class showvalue:
    def GET(self):
        r = getCon()
        res = r.get('val')
        if res:
            res = int(res)
            return json.dumps({'val': res})
        return json.dumps({'val': 0})

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()