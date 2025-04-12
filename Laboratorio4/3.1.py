def is_balanced(expression):
    """Check if an expression has balanced parentheses, brackets, and braces."""
    stack = []
    opening = "({["
    closing = ")}]"
    
    brackets_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in expression:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return False
            top = stack.pop()
            if top != brackets_map[char]:
                return False
    
    return len(stack) == 0
def test_balanced_parentheses():
    """Test parentheses balancing with various expressions."""
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),
        (")(", False),
        ("((((", False),
        ("))))", False),
        ("a*(b+c)-(d/e)", True)
    ]
    
    print("Testing parentheses balancing:")
    for expr, expected in test_cases:
        result = is_balanced(expr)
        print(f"Expression: '{expr}', Balanced: {result}, Expected: {expected}")
        assert result == expected, f"Test failed for '{expr}'"
    
    print("All balanced parentheses tests passed!")

# Example usage
if __name__ == "__main__":
    test_balanced_parentheses()
