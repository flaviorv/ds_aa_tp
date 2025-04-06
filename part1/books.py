class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def all_words(self):
        def _dfs(node, prefix, words):
            if node.is_end:
                words.append(prefix)
            for char, child in node.children.items():
                _dfs(child, prefix + char, words)
        words = []
        _dfs(self.root, "", words)
        return words

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def autocomplete(self, prefix):
        def _dfs(node, current, results):
            if node.is_end:
                results.append(current)
            for char, child in node.children.items():
                _dfs(child, current + char, results)
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        _dfs(node, prefix, results)
        return results

    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end:
                    print(f"{word} not found to be removed")
                    return False
                node.is_end = False
                print(f"{word} removed")
                return len(node.children) == 0
            char = word[depth]
            if char not in node.children:
                print(f"{word} not found to be removed")
                return False
            should_delete_child = _delete(node.children[char], word, depth + 1)
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end
            return False
        _delete(self.root, word, 0)

    def suggest_corrections(self, word, max_distance=2):
        from difflib import SequenceMatcher

        def levenshtein(a, b):
            dp = [[0] * (len(b)+1) for _ in range(len(a)+1)]
            for i in range(len(a)+1):
                for j in range(len(b)+1):
                    if i == 0:
                        dp[i][j] = j
                    elif j == 0:
                        dp[i][j] = i
                    elif a[i-1] == b[j-1]:
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
            return dp[len(a)][len(b)]
        candidates = self.all_words()
        suggestions = []
        for candidate in candidates:
            distance = levenshtein(word, candidate)
            if distance <= max_distance:
                suggestions.append((candidate, distance))
        suggestions.sort(key=lambda x: x[1])
        return [s[0] for s in suggestions]


if __name__ == "__main__":
    titles = [
        "harry potter", "hamlet", "o senhor dos aneis", "dom casmurro",
        "orgulho e preconceito", "a revolução dos bichos", "1984", "o pequeno príncipe",
        "o código da vinci", "o alquimista", "capitães da areia", "o cortiço",
        "a ilha do tesouro", "romeu e julieta", "a metamorfose", "o lobo da estepe",
        "moby dick", "a divina comédia", "grande sertão veredas"
    ]

    trie = Trie()
    for title in titles:
        trie.insert(title)

    print("All titles:")
    print(trie.all_words())

    print("\nAutocomple:")
    prefixes = ["a div", "ha", "a ", "o c"]
    for prefix in prefixes:
        print(f"{prefix} - {trie.autocomplete(prefix)}")


    print("\nAutocorrect:")
    incorrect_words = ["grandi sertao veredas", "a divna comedia"]
    for word in incorrect_words:
        print(f"{word} - Sugestions: {trie.suggest_corrections(word)}")

    print("\nRemove:")
    trie.delete("harry potter")
    print("\nAfter delete:")
    print(trie.all_words())
