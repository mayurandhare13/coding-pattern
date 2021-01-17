'''
Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

Input: [
  [1,0,1],
  [1,1,1],
  [0,1,1]
]
Output: [
  [0,1,0],
  [0,0,0],
  [0,0,1]
]

Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]
'''


def flip_and_invert_image(matrix):
    cols = len(matrix[0])

    for row in matrix:
        for i in range((cols+1) // 2):
            row[i], row[cols - 1 - i] = row[cols - i - 1] ^ 1, row[i] ^ 1
    
    return matrix


if __name__ == "__main__":
    print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_and_invert_image([[1,1,0,0], [1,0,0,1], [0,1,1,1], [1,0,1,0]]))
