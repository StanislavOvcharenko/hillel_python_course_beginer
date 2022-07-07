from unittest import TestCase, main
from main import weather

class test_string(TestCase):
    def test_typeerror_weather(self):
        with self.assertRaises(TypeError):
            weather(1)

    def test_nameerror_weather(self):
        with self.assertRaises(NameError):
            weather(Dnipro)

if __name__ == '__main__':
    main()