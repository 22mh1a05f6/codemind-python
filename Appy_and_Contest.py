def solve_contest(T, test_cases):
    for _ in range(T):
        N, A, B, K = test_cases[_]
        
        count_A = N // A  # number of problems divisible by A
        count_B = N // B  # number of problems divisible by B
        count_A_and_B = N // (A * B)  # number of problems divisible by both A and B
        
        count_A_only = count_A - count_A_and_B  # number of problems divisible by A but not B
        count_B_only = count_B - count_A_and_B  # number of problems divisible by B but not A
        
        if count_A_only + count_B_only >= K:
            print("Win")
        else:
            print("Lose")

# Read the number of test cases
T = int(input())

test_cases = []
# Read the test cases
for _ in range(T):
    N, A, B, K = map(int, input().split())
    test_cases.append((N, A, B, K))

# Solve the contest
solve_contest(T, test_cases)