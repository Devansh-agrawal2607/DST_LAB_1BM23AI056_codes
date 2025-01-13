def isBalanced(s):
    stack = []
    brackets = {']': '[', '}': '{', ')': '('}
    opening_count = {'(': 0, '{': 0, '[': 0}
    closing_count = {')': 0, '}': 0, ']': 0}

    for char in s:
        if char in brackets:
            top_element = stack.pop() if stack else '%'
            if brackets[char] != top_element:
                return "NO", opening_count, closing_count
            closing_count[char] += 1
        else:
            stack.append(char)
            opening_count[char] += 1
    
    balance_result = "YES" if not stack else "NO"
    return balance_result, opening_count, closing_count

if __name__ == '__main__':
    t = int(input("Enter how many question do you need to count the code: ").strip())

    for _ in range(t):
        s = input("Enter Braces:")
        result, opening_count, closing_count = isBalanced(s)
        print("Are the braces balanced (YES or NO): ",result)
        print(f"Opening braces: {opening_count}")
        print(f"Closing braces: {closing_count}")