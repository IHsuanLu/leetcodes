from ast import List

# backtracking + trie
# M * N * 4 * 3^(L - 1), where L is the max length of the word
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        
        curr.endOfWord = True
    
    def prune(self, word) -> None:
        curr = self.root
        node_c_key_tuples = []

        for char in word:
            node_c_key_tuples.append((curr, char))
            curr = curr.children[char]

        for i in range(len(node_c_key_tuples) - 1, -1, -1):
            parent, c_key = node_c_key_tuples[i]
            
            target = parent.children[c_key]
            if len(target.children) == 0:
                del parent.children[c_key]


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        num_rows, num_cols = len(board), len(board[0])
        res = []
        
        trie = Trie()
        for w in words:
            trie.insert(w)
        
        def dfs(row, col, node, path, visited):
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
                return
            if (row, col) in visited:
                return
            if board[row][col] not in node.children:
                return
            
            visited.add((row, col))
            
            curr_node = node.children[board[row][col]]
            new_path = path + board[row][col]
            
            if curr_node.endOfWord:
                res.append(new_path)
                curr_node.endOfWord = False
                trie.prune(new_path)

            dfs(row + 1, col, curr_node, new_path, visited)
            dfs(row - 1, col, curr_node, new_path, visited)            
            dfs(row, col + 1, curr_node, new_path, visited)            
            dfs(row, col - 1, curr_node, new_path, visited)         
            
            visited.remove((row, col))
        
        for r in range(num_rows):
            for c in range(num_cols):
                dfs(r, c, trie.root, "", set())
        
        return res


# backtracking brute force (not accepted) -> word_count * m * n * 4^(m*n)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        num_rows, num_cols = len(board), len(board[0])
        res = []
        def dfs(row, col, idx, t_word, visited):
            if idx == len(t_word):
                if t_word not in res:
                    res.append(t_word)
                return
            
            if row < 0 or col < 0 or row >= num_rows or col >= num_cols:
                return
            
            if (row, col) in visited:
                return
            
            if board[row][col] != t_word[idx]:
                return
            
            visited.add((row, col))
            
            dfs(row + 1, col, idx + 1, t_word, visited)
            dfs(row - 1, col, idx + 1, t_word, visited)            
            dfs(row, col + 1, idx + 1, t_word, visited)            
            dfs(row, col - 1, idx + 1, t_word, visited)         
            
            visited.remove((row, col))
        
        for r in range(num_rows):
            for c in range(num_cols):
                for w in words:
                    if board[r][c] == w[0]:
                        dfs(r, c, 0, w, set())
        
        return res