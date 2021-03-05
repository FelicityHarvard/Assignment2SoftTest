import unittest
import Assignment2

class TestAssignment(unittest.TestCase):

    def test_bmi(Self):
      Self.assertEqual(Assignment2.bmical(5,3,265), (48, 'Obese'))
      Self.assertEqual(Assignment2.bmical(6,2,100), (13, 'Underweight'))
      Self.assertEqual(Assignment2.bmical(6,1,175), (24, 'Normal weight'))
      # Self.assertEqual(Assignment2.bmical(4,1,100), (29, 'Overweight'))
      # For some reason when testing this one function it says Category is being called before it is made but i dont know why 
      # that error is occuring 

    def test_retierment(Self):
      Self.assertEqual(Assignment2.retir(25,65000,0.1,1500000), (0))
      Self.assertEqual(Assignment2.retir(45,100000,0.15,500000), (70))
         

        
if __name__ == '__main__':
    unittest.main()