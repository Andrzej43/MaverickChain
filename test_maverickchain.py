# test_maverickchain.py
"""
Tests for MaverickChain module.
"""

import unittest
from maverickchain import MaverickChain

class TestMaverickChain(unittest.TestCase):
    """Test cases for MaverickChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MaverickChain()
        self.assertIsInstance(instance, MaverickChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MaverickChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
