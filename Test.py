import FunctionPlotter
import unittest
import pytest

@pytest.fixture
def app(qtbot):
    test_app = FunctionPlotter.Window()
    qtbot.Window(test_app)
    return test_app

class Test(unittest.TestCase):
    def testFunction(self):
        try:
            result = FunctionPlotter.Window.string2func(self,"x")
            print('Passed')
        except ValueError as e:
            print('Failed')

        try:
            result = FunctionPlotter.Window.string2func(self,"y")
            print('Passed')
        except ValueError as e:
            print('Failed')

        try:
            result = FunctionPlotter.Window.string2func(self,"5*x^3 + 2*x")
            print('Passed')
        except ValueError as e:
            print('Failed')

        try:
            result = FunctionPlotter.Window.string2func(self,"x^2+3-1")
            print('Passed')
        except ValueError as e:
            print('Failed')

        try:
            result = FunctionPlotter.Window.string2func(self,"sin(x)*cos(x)")
            print('Passed')
        except ValueError as e:
            print('Failed')

        try:
            result = FunctionPlotter.Window.string2func(self,"hello x")
            print('Passed')
        except ValueError as e:
            print('Failed')
        
        try:
            result = FunctionPlotter.Window.string2func(self,"x*x")
            print('Passed')
        except ValueError as e:
            print('Failed')

        try:
            result = FunctionPlotter.Window.string2func(self,"x^0.5")
            print('Passed')
        except ValueError as e:
            print('Failed')

        try:
            result = FunctionPlotter.Window.string2func(self,"tan(x)")
            print('Passed')
        except ValueError as e:
            print('Failed')
                                    

if __name__ == '__main__':
    unittest.main()       