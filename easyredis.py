import redis
import json

REDIS_HOST = ''
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_PWD = ''
TTL = 300


class EasyRedis(object):

    def __init__(self):
        self.mc = redis.StrictRedis(host=REDIS_HOST,
                                    port=REDIS_PORT,
                                    db=REDIS_DB,
                                    password=REDIS_PWD)

    def set_cache(self, memkey, content, ttl_seconds=TTL):
        return self.mc.set(memkey, json.dumps(content), ttl_seconds)

    def get_cache(self, memkey):
        a = self.mc.get(memkey)
        if not a:
            retval = a
        else:
            retval = a.decode() if a is not None else False
            retval = json.loads(retval)
        return retval

    def del_cache(self, memkey):
        return self.mc.delete(memkey)

    def sets_add(self, sets_name, value):
        return self.mc.sadd(sets_name, value)

    def sets_is_member(self, sets_name, value):
        return self.mc.sismember(sets_name, value)

    def sets_delete(self, sets_name, value):
        return self.mc.srem(sets_name, value)

    def sets_members(self, sets_name):
        return self.mc.smembers(sets_name)