from unittest import TestCase,main
from dz16.Ovcharenko_Stanislav_dz16 import start_stop

class MyTest(TestCase):

    def test_exchange_usd(self):
        self.assertEqual(start_stop("EXCHANGE USD 100"), "UAH 3700.0, RATE 37.0")

    def test_exchange_uah(self):
        self.assertEqual(start_stop("EXCHANGE UAH 100"), "USD 2.6455026455026456,RATE 0.026455026455026457")

    def test_course_usd(self):
        self.assertEqual(start_stop("COURSE USD"), ('rate 37.8', 'availible 19997.354497354496'))

    def test_course_uah(self):
        self.assertEqual(start_stop("COURSE UAH"), ('rate 37.8', 'availible 19997.354497354496'))

    def test_stop(self):
        with self.assertRaises(AssertionError) as e:
            start_stop("STOP")
        self.assertEqual()




if __name__ == "__main__":
    main()