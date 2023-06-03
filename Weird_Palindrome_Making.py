def min_operations(T, test_cases):
    for _ in range(T):
        N = test_cases[_][0]
        A = test_cases[_][1]

        odd_count = 0  # Count of characters with odd number of occurrences

        for i in range(N):
            if A[i] % 2 == 1:
                odd_count += 1

        min_ops = odd_count // 2

        print(min_ops)

# Read the number of test cases
T = int(input())

test_cases = []
# Read the test cases
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

# Solve the problem
min_operations(T, test_cases)