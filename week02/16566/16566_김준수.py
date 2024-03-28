# N, M, K = map(int, input().split())
# minsu_cards = list(map(int, input().split()))
# enemy_cards = list(map(int, input().split()))
#
# already = []
# for i in enemy_cards:
#     close_card = 0
#     close = 4000000
#     for j in minsu_cards:
#         if j not in already:
#             if j - i == 1:
#                 already.append(j)
#                 break
#             elif 0 < (j - i) < close:
#                 close = j - i
#                 close_card = j
#     else:
#         already.append(close_card)
#
# for k in already:
#     print(k)
# import sys
# input = sys.stdin.readline
#
#
# N, M, K = map(int, input().split())
# minsu_cards = set(map(int, input().split()))
# enemy_cards = list(map(int, input().split()))
#
# already = set()
# for i in enemy_cards:
#     close_card = 0
#     close = 4000000
#     for j in minsu_cards:
#         ab = j - i
#         if j not in already:
#             if ab == 1:
#                 already.add(j)
#                 print(j)
#                 break
#             elif 0 < ab < close:
#                 close = ab
#                 close_card = j
#     else:
#         already.add(close_card)
#         print(close_card)

# N, M, K = map(int, input().split())
# minsu_cards = set(map(int, input().split()))
# enemy_cards = list(map(int, input().split()))
#
# already = set()
# for i in enemy_cards:
#     minsoo_card = min((card for card in minsu_cards if card > i and card not in already), default=None)
#     if minsoo_card is not None:
#         already.add(minsoo_card)
#         print(minsoo_card)
#     else:
#         minsoo_card = min(minsu_cards - already)
#         already.add(minsoo_card)
#         print(minsoo_card)

# from bisect import bisect_left
#
# N, M, K = map(int, input().split())
# minsu_cards = sorted(map(int, input().split()))
# enemy_cards = list(map(int, input().split()))
#
# already = set()
#
# for i in enemy_cards:
#     idx = bisect_left(minsu_cards, i + 1)
#     if idx < len(minsu_cards):
#         minsoo_card = minsu_cards[idx]
#         if minsoo_card not in already:
#             already.add(minsoo_card)
#             print(minsoo_card)
#         else:
#             minsoo_card = min(set(minsu_cards) - already)
#             already.add(minsoo_card)
#             print(minsoo_card)
#     else:
#         minsoo_card = min(set(minsu_cards) - already)
#         already.add(minsoo_card)
#         print(minsoo_card)

