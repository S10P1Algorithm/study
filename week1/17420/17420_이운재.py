'''
1. 기한 연장을 최소한으로 하고 싶어한다.
2. 남은 기프티콘 중 기한이 가장 적게 남은 기프티콘만 사용할 수 있다.
3. 단 기한이 가장 적게 남은 기프티콘이 여러 개라면 그 중 아무거나 선택할 수 있다.
4. 하루에 여러 기프티콘을 사용하거나 연장하는 것 모두 가능하다.
5. 한번 연장에 30일이 늘어난다.

원하는 것 - 최소 횟수로 기한 연장을 하면서 기프티콘을 다 쓸 수 있도록 정우를 도와주자.

첫째 줄에 기프티콘의 수 N이 주어진다.

둘째 줄에 A1, A2, ..., AN가 주어진다. 이는 i번째 기프티콘의 남은 기한이 Ai일이라는 뜻이다.

셋째 줄에 B1, B2, ..., BN가 주어진다. 이는 i번째 기프티콘을 Bi일 뒤에 사용할 계획이라는 뜻이다.
------------------------------------------------------------------------------

첫째 줄에 정우가 기한 연장을 해야 하는 최소 횟수를 출력한다.
'''
'''
남은 기프티콘중 기한이 가장 적게 남은 기프티콘만 사용할 수 있기 때문에, 1일이 남은게 10만개가 있다면, 한개를 쓰고 99999개 연장, 마찬가지로 30일뒤 99998개
연장  결국 최대값은 99999*100000/2 여서 4999950000 이여서 32비트 정수 최대값인 2147483647을 넘는다.
'''

import sys

input = sys.stdin.readline

