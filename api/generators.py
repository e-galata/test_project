from faker import Faker

class User:
    def __init__(self, locale='en_US'):
        self.faker = Faker(locale)
        self.result = {}
        self.reset()

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

    def reset(self):
        self.set_name()
        self.set_job()

    def build(self):
        return self.result
