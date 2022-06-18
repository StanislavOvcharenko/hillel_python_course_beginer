class Users:

    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

    def __call__(self, *args, **kwargs):
        print("i'm users data")

    def __repr__(self):
        v = vars(self)
        print(f'its my atributes : {v}')

    @property
    def user_data(self):
        return self.name, self.age, self.mail

    @user_data.setter
    def user_data(self, value: list):
        self.name = value[0]
        self.age = value[1]
        self.mail = value[2]

    @user_data.deleter
    def user_data(self):
        self.name = None
        self.age = None
        self.mail = None


y = Users("Stas", 27, "fsafasf@gmail.ru")

print(y.user_data)

y.user_data = ["stas", 25, "123456@gmail.com"]

print(y.user_data)

del y.user_data
print(y.user_data)


class Singletone:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singletone, cls).__new__(cls)
        return cls.instance


a = Singletone()
b = Singletone()
print(a, b)
print(a is b)
