class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        start = image[sr][sc]

        if start == color:
            return image
            
        def dfs(i, j):
            if i < 0 or i  >= rows or j< 0 or j >= cols:
                return

            if image[i][j] != start:
                return

            image[i][j] = color
        
            

            up = dfs(i-1, j)
            down = dfs(i+1, j)
            left = dfs(i, j-1)
            right = dfs(i, j+1)

        dfs(sr, sc)

        return image







        