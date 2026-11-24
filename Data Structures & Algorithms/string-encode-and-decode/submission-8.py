class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for words in strs:
            string = string + str(len(words)) + "#" + words
        return string


    def decode(self, s: str) -> List[str]:
        array = []
        i = 0 #current index
        while i < len(s):
            #FIND THE "#"
            j = s.index("#", i)
            #FIND LENGTH OF WORD
            length = int(s[i:j])
            #NOW CREATE THE WORD
            word = s[j+1:j+1+length]
            array.append(word)
            #NEXT ENCODED STRING
            i = j+1+length
        return array


            
