import redis
import time

r = redis.StrictRedis(host='' ,port=6379)

first_time =  r.hget('result', 'time')

start_time = time.time() 

while(True):
    result = r.hgetall('result')
    if first_time == result.get('time'.encode()).decode():
        continue

    first_time =  result.get('time'.encode()).decode()
    result = result.get('result'.encode()).decode()
    print(result)
    print(time.time() - start_time)
    start_time = time.time() 
