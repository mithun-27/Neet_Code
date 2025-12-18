# 271. Encode and Decode Strings
"""Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters."""

#answer
from typing import List
class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            decoded_strs.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded_strs

#example usage
solution = Solution()
encoded = solution.encode(["neet","code","love","you"])
print(encoded)  # Output: "4#neet4#code4#love3#you"
decoded = solution.decode(encoded)
print(decoded)  # Output: ["neet","code","love","you"]


"""WALKTHROUGH
1. We define a class Solution with two methods: encode and decode.
2. The encode method takes a list of strings strs as input and initializes an empty string encoded_str to store the encoded result.
3. We iterate through each string s in the input list strs. For each string, we append its length followed by a '#' character and then the string itself to encoded_str.
4. After processing all strings, we return the concatenated encoded_str.    
5. The decode method takes the encoded string s as input and initializes an empty list decoded_strs to store the decoded strings.
6. We use a while loop to iterate through the encoded string s. Inside the loop, we use another pointer j to find the position of the '#' character, which separates the length of the string from the string itself.
7. We extract the length of the string by converting the substring from index i to j into an integer.
8. We then extract the actual string using the length we just obtained and append it to the decoded_strs list.
9. We update the index i to point to the next segment in the encoded string and continue the process until we have processed the entire string.
10. Finally, we return the list of decoded strings.
"""