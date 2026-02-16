class Solution:

    def unhappyFriend(self, n: int, pref: list[list[int]], pairs: list[list[int]])->int:

        rank = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(len(pref[i])):

                rank[i][pref[i][j]] = j
        
        partner = {}

        for x, y in pairs:
            partner[x] = y
            partner[y] = x

        unhappy = 0

        for x in range(n):
            y = partner[x]

            for u in range(n):
                if u == x or u == y:
                    continue
                v = partner[u]

                if rank[x][u] < rank[x][y] and rank[u][x] < rank[u][v]:
                    unhappy += 1
                    break  
        
        return unhappy
    

x = Solution()
print(x.unhappyFriend(4, [[1,2,3],[2,3,0],[3,0,1],[0,1,2]], [[0,1],[2,3]]))