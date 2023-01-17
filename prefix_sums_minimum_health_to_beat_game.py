from ast import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        prefix_sum = damage[:]
        max_val = damage[0]

        armor_is_used = False
        for i in range(len(damage)):
            max_val = max(max_val, damage[i])
            if not armor_is_used and damage[i] >= armor:
                prefix_sum[i] -= armor
                armor_is_used = True

            if i + 1 < len(damage):
                prefix_sum[i + 1] += prefix_sum[i]

        if not armor_is_used:
            prefix_sum[-1] -= max_val

        return prefix_sum[-1] + 1

