import redis
import time

while(True):
    start_time = time.time()
    r = redis.StrictRedis(host='123.254.187.65' ,port=6379)
    result = r.hget('result', 'result').decode()
    print(result)
    print(time.time() - start_time)