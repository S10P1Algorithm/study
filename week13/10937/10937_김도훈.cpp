#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    // 문자를 숫자로 매핑하여 배열을 초기화
    vector<vector<int>> arr(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            char c;
            cin >> c;
            arr[i][j] = c - 'A';
        }
    }

    // dp 배열을 2차원 벡터로 초기화
    vector<vector<int>> dp(N, vector<int>(1 << N, 0));

    // 비용 행렬 초기화
    vector<vector<int>> cost = {
        {100, 70, 40, 0, 0, 0},
        {70, 50, 30, 0, 0, 0},
        {40, 30, 20, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0}
    };

    // 0번째 행을 초기화
    for (int j = 1; j < N; j++) {
        for (int curr_bit = 0; curr_bit < (1 << N); curr_bit++) {
            if (!(curr_bit & (1 << j)) && !(curr_bit & (1 << (j - 1)))) {
                int new_bit = (curr_bit | (1 << j)) | (1 << (j - 1));
                dp[0][new_bit] = max(dp[0][new_bit], dp[0][curr_bit] + cost[arr[0][j]][arr[0][j - 1]]);
            }
        }
    }

    // i번째 행 계산
    for (int i = 1; i < N; i++) {
        int prev_max = *max_element(dp[i - 1].begin(), dp[i - 1].end());
        dp[i][0] = prev_max;

        // 세로 연결 처리
        for (int curr_bit = 0; curr_bit < (1 << N); curr_bit++) {
            for (int prev_bit = 0; prev_bit < (1 << N); prev_bit++) {
                int temp = dp[i - 1][prev_bit];
                bool valid = true;
                for (int j = 0; j < N; j++) {
                    if (curr_bit & (1 << j)) {
                        if (prev_bit & (1 << j)) {
                            valid = false;
                            break;
                        }
                        else {
                            temp += cost[arr[i][j]][arr[i - 1][j]];
                        }
                    }
                }
                if (valid) {
                    dp[i][curr_bit] = max(dp[i][curr_bit], temp);
                }
            }
        }

        // 가로 연결 처리
        for (int curr_bit = 0; curr_bit < (1 << N); curr_bit++) {
            for (int j = 1; j < N; j++) {
                if (!(curr_bit & (1 << j)) && !(curr_bit & (1 << (j - 1)))) {
                    int new_bit = curr_bit | (1 << j) | (1 << (j - 1));
                    dp[i][new_bit] = max(dp[i][new_bit], dp[i][curr_bit] + cost[arr[i][j]][arr[i][j - 1]]);
                }
            }
        }
    }

    // 최대 점수 계산
    int ans = *max_element(dp[N - 1].begin(), dp[N - 1].end());
    cout << ans << endl;

    return 0;
}
