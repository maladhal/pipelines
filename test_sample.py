"""
Sample test file to demonstrate Jenkins pipeline functionality.
This file contains basic pytest test cases.
"""

import pytest
import math


def add_numbers(a, b):
    """Simple function to add two numbers."""
    return a + b


def divide_numbers(a, b):
    """Simple function to divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


class TestBasicOperations:
    """Test class for basic mathematical operations."""
    
    def test_add_positive_numbers(self):
        """Test addition of positive numbers."""
        result = add_numbers(5, 3)
        assert result == 8
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = add_numbers(-5, 3)
        assert result == -2
    
    def test_add_zero(self):
        """Test addition with zero."""
        result = add_numbers(5, 0)
        assert result == 5
    
    def test_divide_positive_numbers(self):
        """Test division of positive numbers."""
        result = divide_numbers(10, 2)
        assert result == 5.0
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide_numbers(10, 0)
    
    def test_circle_area_positive_radius(self):
        """Test circle area calculation with positive radius."""
        radius = 3
        expected_area = math.pi * 9  # π * r²
        result = calculate_circle_area(radius)
        assert abs(result - expected_area) < 0.001
    
    def test_circle_area_zero_radius(self):
        """Test circle area calculation with zero radius."""
        result = calculate_circle_area(0)
        assert result == 0
    
    def test_circle_area_negative_radius_raises_error(self):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            calculate_circle_area(-5)


class TestEdgeCases:
    """Test class for edge cases."""
    
    @pytest.mark.parametrize("a,b,expected", [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (0.5, 0.25, 0.75)
    ])
    def test_add_numbers_parametrized(self, a, b, expected):
        """Parametrized test for addition function."""
        result = add_numbers(a, b)
        assert result == expected
    
    def test_large_numbers(self):
        """Test with large numbers."""
        large_num = 10**10
        result = add_numbers(large_num, large_num)
        assert result == 2 * large_num


if __name__ == "__main__":
    pytest.main([__file__])