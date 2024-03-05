#include <iostream>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, K;
	cin >> N >> K;
	int order[101], plug[101]{0, };

	int ans = 0;
	for (int i = 0; i < K; i++) {
		cin >> order[i];
	}

	for (int i = 0; i < K; i++) {
		bool check = false;
		for (int j = 0; j < N; j++) {
			if (order[i] == plug[j]) {
				check = true;
				break;
			}
		}
		if (check) continue;

		for (int j = 0; j < N; j++) {
			if (plug[j] == 0) {
				plug[j] = order[i];
				check = true;
				break;
			}
		}
		if (check) continue;


		int last_used_idx = -1;
		int last_used_div = -1;
		for (int j = 0; j < N; j++) {
			int temp = 0;
			for (int k = i + 1; k < K; k++) {
				if (plug[j] == order[k]) break;
				temp++;
			}
			if (temp > last_used_idx) {
				last_used_idx = temp;
				last_used_div = j;
			}
		}
		plug[last_used_div] = order[i];
		ans++;
	}

	cout << ans;
	return 0;
}

