from faker import Faker

class JsonBuilder():
    """
    Базовый класс для Json билдеров, подключает faker для данных
    содержит метод класса для использования в параметрах тестов
    имеет дефолтную локаль, каждый билдер может передавать свою локаль в этот класс
    билдит result как данные JSON
    """
    def __init__(self, locale='en_US'):
        self.faker = Faker(locale)
        self.result = {}

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self

    def build(self):
        return self.result

class User(JsonBuilder):
    """
    Класс билдер данных пользователя post /api/users
    {name: str, job: str}, наследуется от родительского класса
    где хранится класс метод вызываемый в тестах, в родительский класс передаем locale и билдим
    """
    def __init__(self, locale):
        super().__init__(locale)
        self.set_name().set_job()

    @classmethod
    def create(cls, locale='en_US', name=None, job=None):
        instance = cls(locale)
        if name is not None:
            instance.set_name(name)
        if job is not None:
            instance.set_job(job)
        return instance.build()

    def set_name(self, name=None):
        self.result['name'] = name if name else self.faker.first_name()
        return self

    def set_job(self, job=None):
        self.result['job'] = job if job else self.faker.job()
        return self
