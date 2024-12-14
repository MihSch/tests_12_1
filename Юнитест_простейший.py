import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        name = runner.Runner('John')
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        n = runner.Runner('n')
        for i in range (10):
            n.run()
        self.assertEqual(n.distance, 10)

    def test_challenge(self):
        n1 = runner.Runner('n1')
        n2 = runner.Runner('n2')
        for i in range (10):
            n1.run()
            n2.walk()
        self.assertNotEqual(n1.distance, n2.distance)


