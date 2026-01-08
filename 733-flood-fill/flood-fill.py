class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        origin = image[sr][sc]

        if image[sr][sc] == color:
            return image

        def dfs(sr, sc):
            if sr < 0 or sr>=rows or sc <0 or sc>=cols:
                return 
            
            if image[sr][sc] != origin:
                return
            
            image[sr][sc] = color

            dfs(sr-1, sc)
            dfs(sr+1, sc)
            dfs(sr, sc-1)
            dfs(sr, sc+1)

            return 

        dfs(sr,sc)
        return image
