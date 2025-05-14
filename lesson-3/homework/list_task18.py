# main list and sublist
main_list = [1, 2, 3, 4, 5, 6, 7]
sub_list = [3, 4, 5]

ans = False

for i in range(len(main_list) - len(sub_list) + 1):
    if main_list[i:i + len(sub_list)] == sub_list:
        ans = True  # If matched, ans = true
        break   # Stop checking after found it

# Print result
print(ans)