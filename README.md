# easyredis
Store data in redis as convenient as memcached which can take any kind data types

### Store data
```bash
   thisdata = dict(info1=1, info2=2, info3="1234")
   EasyRedis().set_cache(memkey="thiskey", content=thisdata)
```

### Customize TTL (Time To Live) value
```bash
   thisdata = dict(info1=1, info2=2, info3="1234")
   EasyRedis().set_cache(memkey="thiskey", content=thisdata, ttl_seconds=600)
```

### Get data
```bash
   thisdata = dict(info1=1, info2=2, info3="1234")
   EasyRedis().get_cache(memkey="thiskey")
```

### Remove data
```bash
   thisdata = dict(info1=1, info2=2, info3="1234")
   EasyRedis().del_cache(memkey="thiskey")
```
