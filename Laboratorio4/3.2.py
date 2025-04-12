def evaluate_postfix(expression):
    """Evaluate a postfix expression in Reverse Polish Notation."""
    stack = []
    operators = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b
    }
    
    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            # It's an operator, pop two operands and apply
            if len(stack) < 2:
                raise ValueError("Invalid postfix expression: not enough operands")
            
            b = stack.pop()  # Second operand
            a = stack.pop()  # First operand
            
            # Apply the operator
            result = operators[token](a, b)
            stack.append(result)
        else:
            # It's an operand, convert to number and push
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token in expression: {token}")
    
    # If we have exactly one value in the stack, it's the result
    if len(stack) == 1:
        return stack[0]
    else:
        raise ValueError("Invalid postfix expression: too many operands")


def test_postfix_evaluation():
    """Test postfix expression evaluation with different operations."""
    test_cases = [
        ("3 4 +", 7),             # 3 + 4 = 7
        ("5 2 -", 3),             # 5 - 2 = 3
        ("3 4 * 2 +", 14),        # 3 * 4 + 2 = 14
        ("7 2 / 3 *", 10.5),      # 7 / 2 * 3 = 10.5
        ("5 1 2 + 4 * + 3 -", 14) # 5 + ((1 + 2) * 4) - 3 = 14
    ]
    
    print("Testing postfix expression evaluation:")
    for expr, expected in test_cases:
        try:
            result = evaluate_postfix(expr)
            print(f"Expression: '{expr}', Result: {result}, Expected: {expected}")
            assert abs(result - expected) < 1e-10, f"Test failed for '{expr}'"
        except Exception as e:
            print(f"Expression: '{expr}', Error: {str(e)}")
    
    print("All postfix evaluation tests passed!")


# Example usage
if __name__ == "__main__":
    test_postfix_evaluation()
