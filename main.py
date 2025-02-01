from typing import List, Any


def generate_permutations_with_prefix_suffix(
        arr: List[Any], prefix: List[Any] = None, suffix: List[Any] = None
) -> List[List[Any]]:
    if prefix is None:
        prefix = []
    if suffix is None:
        suffix = []
    prefix_len = len(prefix)
    suffix_len = len(suffix)
    if prefix_len + suffix_len > len(arr):
        return []
    remaining = [x for x in arr if x not in prefix and x not in suffix]
    def _generate(current_permutation, remaining_elements):
        if not remaining_elements:
            return [current_permutation]
        permutations = []
        for i, element in enumerate(remaining_elements):
            new_remaining = remaining_elements[:i] + remaining_elements[i + 1:]
            permutations.extend(_generate(current_permutation + [element], new_remaining))
        return permutations
    results = _generate(prefix, remaining)
    results = [x + suffix for x in results]
    return [perm for perm in results if perm[:prefix_len] == prefix and perm[-suffix_len:] == suffix]


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print("Тест с префиксом [2, 1]:")
    for perm in generate_permutations_with_prefix_suffix(arr, prefix=[2, 1]):
        print(perm)
    print("\nТест с префиксом [2] и суффиксом [4]:")
    for perm in generate_permutations_with_prefix_suffix(arr, prefix=[2], suffix=[4]):
        print(perm)
    print("\nТест с префиксом [1] и суффиксом [4,3]:")
    for perm in generate_permutations_with_prefix_suffix(arr, prefix=[1], suffix=[4, 3]):
        print(perm)
    print("\nТест с префиксом [1,2,3] и суффиксом [4]:")
    for perm in generate_permutations_with_prefix_suffix(arr, prefix=[1, 2, 3], suffix=[4]):
        print(perm)
    print("\nТест с префиксом [1,2,3] и суффиксом [3]:")
    for perm in generate_permutations_with_prefix_suffix(arr, prefix=[1, 2, 3], suffix=[3]):
        print(perm)
    print("\nТест без префикса и суффикса:")
    for perm in generate_permutations_with_prefix_suffix(arr):
        print(perm)