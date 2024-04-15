#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int N;
    cin >> N;

    // ���ڸ� ���ڷ� �����Ͽ� �迭�� �ʱ�ȭ
    vector<vector<int>> arr(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            char c;
            cin >> c;
            arr[i][j] = c - 'A';
        }
    }

    // dp �迭�� 2���� ���ͷ� �ʱ�ȭ
    vector<vector<int>> dp(N, vector<int>(1 << N, 0));

    // ��� ��� �ʱ�ȭ
    vector<vector<int>> cost = {
        {100, 70, 40, 0, 0, 0},
        {70, 50, 30, 0, 0, 0},
        {40, 30, 20, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0},
        {0, 0, 0, 0, 0, 0}
    };

    // 0��° ���� �ʱ�ȭ
    for (int j = 1; j < N; j++) {
        for (int curr_bit = 0; curr_bit < (1 << N); curr_bit++) {
            if (!(curr_bit & (1 << j)) && !(curr_bit & (1 << (j - 1)))) {
                int new_bit = (curr_bit | (1 << j)) | (1 << (j - 1));
                dp[0][new_bit] = max(dp[0][new_bit], dp[0][curr_bit] + cost[arr[0][j]][arr[0][j - 1]]);
            }
        }
    }

    // i��° �� ���
    for (int i = 1; i < N; i++) {
        int prev_max = *max_element(dp[i - 1].begin(), dp[i - 1].end());
        dp[i][0] = prev_max;

        // ���� ���� ó��
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

        // ���� ���� ó��
        for (int curr_bit = 0; curr_bit < (1 << N); curr_bit++) {
            for (int j = 1; j < N; j++) {
                if (!(curr_bit & (1 << j)) && !(curr_bit & (1 << (j - 1)))) {
                    int new_bit = curr_bit | (1 << j) | (1 << (j - 1));
                    dp[i][new_bit] = max(dp[i][new_bit], dp[i][curr_bit] + cost[arr[i][j]][arr[i][j - 1]]);
                }
            }
        }
    }

    // �ִ� ���� ���
    int ans = *max_element(dp[N - 1].begin(), dp[N - 1].end());
    cout << ans << endl;

    return 0;
}
