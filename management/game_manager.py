class GameManager:
    _instance = None  # Приватное поле для хранения единственного экземпляра
    isCreated = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance

    def __init__(self, settings=None):
        if GameManager.isCreated:
            return
        GameManager.isCreated = True
        # self._map = Map(settings)
        # self._entities = []
        self._map = ["Пидор"]
        pass

    def notify_port(self, notify_message):
        # В зависимости от сообщения, сделать какое-то взаимодействие игры и персонажа
        pass