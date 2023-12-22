class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        output = []
        for i in image:
            rev = i[::-1]
            cur_image = []
            for j in rev:
                if j == 1:
                    cur_image.append(0)
                else:
                    cur_image.append(1)
            output.append(cur_image)

        return output
