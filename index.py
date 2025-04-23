import tokenize, keyword
from collections import Counter
import os

# keyword list + print
ListKey = keyword.kwlist + ['print']

# getting input
input_code = input("Enter file path or Python code: ")

# checking input is file
if os.path.isfile(input_code):
    file_path = input_code
    print(f"\n{file_path} selected to analyse.")
else:
    # if input is python code
    file_path = "temp_code.py"
    with open(file_path, "w") as f:
        f.write(input_code)
    print(f"\nCode Saved in:{file_path} ")

counts = Counter()
try:
    with open(file_path, "rb") as f:
        tokens = tokenize.tokenize(f.readline)
        for token in tokens:
            tok_type = token.type
            tok_str = token.string
            if tok_type == tokenize.NAME:
                if tok_str in ListKey:
                    counts['KeyWords'] += 1
                else:
                    counts['Variables'] += 1
            elif tok_type == tokenize.NUMBER:
                counts['Numbers'] += 1
            elif tok_type == tokenize.STRING:
                counts['Strings'] += 1
            elif tok_type == tokenize.COMMENT:
                counts['Comments'] += 1
            elif tok_type == tokenize.OP:
                counts['Operators'] += 1
except tokenize.TokenError as e:#handling error
    pass

# print the result
for key, value in counts.items():
    print(f"{key}: {value}")

# running the code
with open(file_path, "r", encoding="utf-8") as f: #utf-8 because maybe you type farsi in file
    code = f.read()
    try:
        print("\nYour code output:")
        exec(code)
    except Exception as e:
        print(f"\nERROR!!!:\n {e}")
