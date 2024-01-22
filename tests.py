import unittest
import s2_q12
import s4_q56
import s4_q59
import s3_q86


class S2Q12TestCase(unittest.TestCase):
    def test_first(self):
        _input = [1, 0, -1, 1, 0, -1, 0, 1, -1]
        _output = [-1, -1, -1, 0, 0, 0, 1, 1, 1]

        self.assertEqual(
            s2_q12.sort_array(_input),
            _output,
            "First test failed!"
        )

    def test_second(self):
        _input = [1, 0, -1, 1, 0, -1, 0, 1, -1, -1, 0, 1, -1]
        _output = [-1, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1]

        self.assertEqual(
            s2_q12.sort_array(_input),
            _output,
            "Second test failed!"
        )


class S4Q56(unittest.TestCase):
    def test_first(self):
        _input = [160, 170, 150, 206, 102]

        self.assertTrue(
            s4_q56.is_tallest_double_of_shortest(_input),
            "The tallest person is 2 times or taller than the shortest person."
        )

    def test_second(self):
        _input = [160, 170, 150, 180, 140]

        self.assertFalse(
            s4_q56.is_tallest_double_of_shortest(_input),
            "The condition is not satisfied."
        )


class S4Q59(unittest.TestCase):
    @staticmethod
    def make_tree():
        bst = s4_q59.BST()

        bst.insert(5)
        bst.insert(3)
        bst.insert(7)
        bst.insert(2)
        bst.insert(4)
        bst.insert(6)
        bst.insert(8)

        return bst

    def test_find(self):
        _output = [2, 3, 4, 5, 6, 7]

        bst = self.make_tree()

        self.assertCountEqual(  # to avoid checking order of elements
            bst.find(2, 7),
            _output,
            "The points are not correct!"
        )

    def test_delete(self):
        _output = [2, 4, 5, 6, 7]

        bst = self.make_tree()
        bst.delete(3)

        self.assertCountEqual(  # to avoid checking order of elements
            bst.find(2, 7),
            _output,
            "deletion failed!"
        )


class S3Q86(unittest.TestCase):
    @staticmethod
    def make_ds():
        custom_ds = s3_q86.CustomDataStructure()
        custom_ds.set(0, 5)
        custom_ds.set(2, 10)
        return custom_ds

    def test_0(self):
        _input = 0
        _output = 5

        custom_ds = self.make_ds()

        self.assertEqual(
            custom_ds.get(_input),
            _output,
            f"The output must be {_output}"
        )

    def test_1(self):
        _input = 1

        custom_ds = self.make_ds()

        self.assertIsNone(
            custom_ds.get(_input),
            f"The output must be None"
        )

    def test_2(self):
        _input = 2
        _output = 10

        custom_ds = self.make_ds()

        self.assertEqual(
            custom_ds.get(_input),
            _output,
            f"The output must be {_output}"
        )

    def test_3(self):
        _input = 3
        _output = None

        custom_ds = self.make_ds()

        with self.assertRaises(IndexError):
            custom_ds.get(_input)


if __name__ == '__main__':
    unittest.main()
