# test_gateveil.py
"""
Tests for GateVeil module.
"""

import unittest
from gateveil import GateVeil

class TestGateVeil(unittest.TestCase):
    """Test cases for GateVeil class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GateVeil()
        self.assertIsInstance(instance, GateVeil)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GateVeil()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
