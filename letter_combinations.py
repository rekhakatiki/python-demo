from typing import List

def letterCombinations(digits: str) -> List[str]:
    if not digits:
        return []

    # Mapping from digits to corresponding letters
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    result = []

    def backtrack(index: int, path: str):
        if index == len(digits):
            result.append(path)
            return
        for letter in phone_map[digits[index]]:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return result
print(letterCombinations("23"))
print("\nInput: ''")
print("Output:", letterCombinations(""))

print("\nInput: '4'")
print("Output:", letterCombinations("4"))