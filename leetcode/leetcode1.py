class Solution(object):
    def romanToInt(self, s):

        DictRoman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        sum=0
        skip_value=False

        for index, x in enumerate(s):
            if index!=len(s)-1:
                if skip_value==True:
                    skip_value=False
                    continue
                if DictRoman[x]<DictRoman[s[index+1]]:
                    sum+=DictRoman[s[index+1]]-DictRoman[x]
                    skip_value=True
                    continue
                else:
                    sum+=DictRoman[x]
            if index==len(s)-1 and skip_value==False:
                sum+=DictRoman[x]
        return sum

solution = Solution()
print(solution.romanToInt('III'))
