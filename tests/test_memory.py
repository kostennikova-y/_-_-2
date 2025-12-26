import unittest
import memory

class TestMemory(unittest.TestCase):

    def setUp(self):
        # Сбрасываем память перед каждым тестом
        memory.mc()

    def test_memory_clear(self):
        memory.m_plus(10)
        memory.mc()
        self.assertEqual(memory.mr(), 0)

    def test_memory_plus_single(self):
        memory.m_plus(5)
        self.assertEqual(memory.mr(), 5)

    def test_memory_plus_multiple(self):
        memory.m_plus(5)
        memory.m_plus(10)
        self.assertEqual(memory.mr(), 15)

    def test_memory_plus_negative(self):
        memory.m_plus(10)
        memory.m_plus(-3)
        self.assertEqual(memory.mr(), 7)

    def test_memory_initial_value(self):
        self.assertEqual(memory.mr(), 0)

if __name__ == "__main__":
    unittest.main()
