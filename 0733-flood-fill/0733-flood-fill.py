class Solution(object):

    def ff(self, startc, image, sr, sc, color):
        if len(image) == 0: 
            return
        #check cords
        if sr > len(image)-1 or sr < 0:
            return
        if sc > len(image[0])-1 or sc < 0:
            return
        #check if current cell is same as the start color
        if image[sr][sc] != startc:
            return
        #base case, itself should be flood filled,
        # otherwise this has already been visited
        if image[sr][sc] == color:
            return
        #switch base to new colour
        image[sr][sc] = color
        # recursivley visit all the ones around
        self.ff(startc, image,sr-1,sc,color)
        self.ff(startc,image,sr,sc-1,color)
        self.ff(startc,image,sr+1,sc,color)
        self.ff(startc,image,sr,sc+1,color)
        return
    def floodFill(self, image, sr, sc, color):
        startc = image[sr][sc]
        self.ff(startc, image, sr, sc, color)
        return image



        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        