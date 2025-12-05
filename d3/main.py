with open("input.txt", "r") as file:
    content = file.read()

lines: list[str] = list(filter(lambda el: len(el), content.split('\n')))


def compute(nb_batteries: int):
    total_joltage = 0
    for digits in lines:
        ans: list[int] = []
        line_len = len(digits)

        i = 0
        for digit in digits:
            number = int(digit)
            ans_len = len(ans)
            power = min(line_len - i, nb_batteries)
            index_to_change = nb_batteries - power

            if ans_len == index_to_change:
                ans.append(number)
            else:
                found = False
                for j in range(index_to_change, ans_len):
                    if number > ans[j]:
                        ans = ans[:j]
                        ans.append(number)
                        found = True
                        break
                if not found:
                    if ans_len < nb_batteries:
                        ans.append(number)
            i += 1

        result_for_line = int(''.join(map(str, ans)))
        total_joltage += result_for_line

    return total_joltage


# Part 1
p1 = compute(2)
print("Part 1:", p1)
# Part 2
p2 = compute(12)
print("Part 2:", p2)
