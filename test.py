from redis_storage import RedisStorage


HOST = 'localhost'
PORT = 6379
DB = 1

def test():
    r = RedisStorage(host=HOST, port=PORT, db=DB)
    print(r)


if __name__ == '__main__':
    test()