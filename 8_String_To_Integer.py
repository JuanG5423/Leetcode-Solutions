class Solution:
    def myAtoi(self,s: str) -> int:
        nums_set = set(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
        numbers = ""
        sign_count = 0
        for char in s.strip():
            if char == '-' and len(numbers) == 0 and sign_count < 1:
                numbers += char
                sign_count += 1
            elif char in nums_set:
                numbers += char
            elif char == '+' and len(numbers) == 0 and sign_count < 1:
                sign_count += 1
            else:
                break
        if len(numbers) <= 0:
            return 0
        else:
            if numbers == '+' or numbers == '-':
                return 0
            elif int(numbers) > 2**31 - 1:
                return 2**31 - 1
            elif int(numbers) < -2 ** 31:
                return -2 ** 31
            else:
                return int(numbers)