"""
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.

For example, flipping [1,1,0] horizontally results in [0,1,1].
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

For example, inverting [0,1,1] results in [1,0,0].
 

Example 1:

Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

"""

def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            i, j = 0, len(row)-1
            while i <= j:
                row[i], row[j] = row[j], row[i]
                if i == j:
                    if row[i] == 0:
                        row[i] = 1
                    else:
                        row[i] = 0
                else:
                    if row[i] == 0:
                        row[i] = 1
                    else:
                        row[i] = 0
                    if row[j] == 1:
                        row[j] = 0
                    else:
                        row[j] = 1
                i+=1
                j-=1
        return image