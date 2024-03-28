# Define the function to recursively track the grid
def tracking(i, j, mask):
    global Ans
    if i == M:
        # Initialize ansAr to store the concatenated numbers
        ansAr = [0] * (M * N + 1)
        
        # Concatenate numbers based on the masking
        for i in range(M):
            for j in range(N):
                ansAr[masking[i][j]] *= 10
                ansAr[masking[i][j]] += pann[i][j]
        
        # Calculate the sum of concatenated numbers
        tmpAns = sum(ansAr)
        Ans = max(Ans, tmpAns)
        return

    # Set the current mask value for the current position
    masking[i][j] = mask

    ni, nj = (i + 1, 0) if j == N - 1 else (i, j + 1)
    
    # Check for compatibility with adjacent cells and recursively explore
    if i and ((not j or masking[i - 1][j - 1] != masking[i - 1][j]) and (j == N - 1 or masking[i - 1][j + 1] != masking[i - 1][j])):
        masking[i][j] = masking[i - 1][j]
        tracking(ni, nj, mask)

    if j and ((not i or masking[i - 1][j - 1] != masking[i][j - 1]) and (i == M - 1 or masking[i + 1][j - 1] != masking[i][j - 1])):
        masking[i][j] = masking[i][j - 1]
        tracking(ni, nj, mask)

    masking[i][j] = mask
    tracking(ni, nj, mask + 1)

# Initialize variables
pann = []
masking = []
ansAr = [0] * 17
Ans = 0

# Input dimensions of the grid
M, N = map(int, input().split())

# Input the grid
for _ in range(M):
    inp = input().strip()
    row = [int(x) for x in inp]
    pann.append(row)
    masking.append([0] * N)

# Start tracking from the top-left cell with mask 1
tracking(0, 0, 1)

# Output the maximum sum of concatenated numbers
print(Ans)
