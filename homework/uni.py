def dictionary(keys, values):
    try:
        if type(keys) and type(values) is not list:
            raise TypeError('Input argument is not a list')
    except TypeError:
        print('Argument is not a list.')
    else:
        result = dict.fromkeys(keys, None)
        result.update(zip(keys, values))
        return result


print(dictionary([2,3,4,5],[2,4,3]))

if __name__ == '__main__':
    import unittest

    class Test_U(unittest.TestCase):

        def test_normal_values(self):
            self.assertEqual(dictionary([2,3,4,5],[22,33,44,55]),{2: 22, 3: 33, 4: 44, 5: 55})
            self.assertEqual(dictionary([2,3,4,5,6],[22,33,44,55]),{2: 22, 3: 33, 4: 44, 5: 55, 6: None})

        def test_vals_float_type(self):
            self.assertTrue(dictionary(7.7, 7.7) is None)
            self.assertTrue(dictionary([7.7],[7.7]), {7.7: 7.7})

        def test_vals_bool_type(self):
            self.assertIsNone(dictionary(False,True), None)

        def test_negative_values(self):
            self.assertEqual(dictionary(-3,-4), None)
            self.assertEqual(dictionary(-355,-4444), None)

        def test_iter_objs(self):
            self.assertIs(dictionary('sss','zzz'), None )
            self.assertIs(dictionary({33,44},{33,44}), None )

    unittest.main(verbosity=2)

assert dictionary([2,3,4,5],[22,33,44,55]) == {2: 22, 3: 33, 4: 44, 5: 55}, ('Wrong!')
assert dictionary([2,3,4,5,6],[22,33,44,55]) == {2: 22, 3: 33, 4: 44, 5: 55, 6: None}, ('Wrong!')

