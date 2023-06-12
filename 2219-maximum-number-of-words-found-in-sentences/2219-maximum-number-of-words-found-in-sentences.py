class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
       
        cur_max=0
        for i in sentences:
            s=i.split()
            if len(s)>cur_max:
                cur_max=len(s)

        return cur_max