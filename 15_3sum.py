def three_sum(arr):
    arr = list(set(arr))
    answers = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            for k in range(len(arr)):
                if arr[i] + arr[j] + arr[k] == 0 and i!= j and i != k and j != k:
                    answers.append([arr[i]] + [arr[j]] + [arr[k]])
    return answers

print(three_sum([-1, 0, 1, 2, -1, -4]))
print(three_sum([0, 0, 0]))
