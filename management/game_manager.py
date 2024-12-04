class GameManager:
    _instance = None  # Приватное поле для хранения единственного экземпляра

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameManager, cls).__new__(cls)
        return cls._instance


Manager1 = GameManager()
print("Object created, ", Manager1)

Manager2 = GameManager()
print("Object created, ", Manager2)
