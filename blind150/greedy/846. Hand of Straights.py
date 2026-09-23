#846. Hand of Straights
"""Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.

Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.

 

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.

 

Constraints:

1 <= hand.length <= 104
0 <= hand[i] <= 109
1 <= groupSize <= hand.length"""


#answer:
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1
        return True


#example:
"""Input
hand =
[1,2,3,6,2,3,4,7,8]
groupSize =
3
Output
true
Expected
true"""

#example:
"""Input
hand =
[1,2,3,4,5]
groupSize =
4
Output
false
Expected
false"""

"""Walkthrough:
1. We want to determine whether all cards in the hand can be divided into groups of size `groupSize`, where each group contains consecutive numbers.
2. If the total number of cards is not divisible by `groupSize`, it is impossible to form equal-sized groups, so we immediately return `False`.
3. We use a frequency map (`Counter`) to store how many times each card value appears in the hand.
4. For every card number, we try to identify the smallest possible value that could be the start of its consecutive group.
5. We repeatedly move left while `start - 1` exists in the frequency map because the current card cannot be the start of a sequence if a smaller consecutive card is still available.
6. Once we find the true starting point of a sequence, we begin forming consecutive groups from that value.
7. While there are still copies of the starting card available, we attempt to build a complete group of length `groupSize`.
8. To create a group, we check every value from `start` to `start + groupSize - 1`.
9. If any required card is missing (`count[i] == 0`), then a valid consecutive group cannot be formed, so we return `False`.
10. Otherwise, we use one occurrence of every card in the group by decrementing their frequencies.
11. We continue forming groups from the same starting value until all copies of that starting card have been used.
12. Then we move to the next possible starting value and repeat the process.
13. If all cards are successfully consumed while forming valid consecutive groups, then every card belongs to exactly one valid group.
14. The key insight is that every sequence must start from its smallest available card, so we always expand groups from the earliest possible starting point.
15. After processing all cards, if no invalid group was encountered, we return `True`.
16. The time complexity is approximately `O(n × groupSize)` in the worst case, and the auxiliary space complexity is `O(n)` for storing the frequency map."""