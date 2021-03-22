import redis

class RedisStorage:
    """
        Класс для взаимодействия с Redis хранилищем
    """

    def __init__(self, host: str, port: int, db: int, decode_type='utf-8'):
        self.host = host
        self.port = port
        self.db = db
        self.initialize_storage()

    def initialize_storage(self):
        """
            Подключается к Redis хранилищу
        :return:
        """
        self.storage = redis.Redis(host=self.host, port=self.port, db=self.db)

    def decode(self, value: bytes) -> str:
        """
            Декодирует значение в кодировку UTF-8, изначально в bytes
        """
        if value is None:
            return None
        return value.decode(self.decode_type)

    def get(self, key: str) -> bytes:
        value = self.storage.get(key)
        return self.decode(value)

    def set(self, key, value):
        self.storage.set(key, value)