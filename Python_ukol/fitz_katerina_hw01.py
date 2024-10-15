import json

with open("alice.txt", "r", encoding="utf-8") as alice_input_file:
    content = alice_input_file.read()
    content = content.lower().replace(" ", "").replace("\n", "")

sum_of_symbols = {}

for symbol in content:
    if symbol in sum_of_symbols:
        sum_of_symbols[symbol] += 1
    else:
        sum_of_symbols[symbol] = 1

sum_of_symbols_sorted = dict(sorted(sum_of_symbols.items()))

with open("hw01_output_sorted.json", "w", encoding="utf-8") as alice_output_file_sorted:
     json.dump(sum_of_symbols_sorted, alice_output_file_sorted, ensure_ascii=False, indent=4)

