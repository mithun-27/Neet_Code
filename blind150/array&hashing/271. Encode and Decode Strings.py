#271. Encode and Decode Strings
"""Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
    // ... your code
    return encoded_string;
}
Machine 2 (receiver) has the function:

vector<string> decode(string s) {
    //... your code
    return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

Example 1:

Input: dummy_input = ["Hello","World"]

Output: ["Hello","World"]

Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);
Example 2:

Input: dummy_input = [""]

Output: [""]

Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters."""

#answer
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
    
#example 1:
dummy_input = ["Hello","World"]
solution = Solution()
encoded_string = solution.encode(dummy_input)
print(encoded_string) # Output: "5#Hello5#World"
decoded_strings = solution.decode(encoded_string)
print(decoded_strings) # Output: ["Hello","World"]

#example 2:
dummy_input = [""]
solution = Solution()
encoded_string = solution.encode(dummy_input)
print(encoded_string) # Output: "0#"
decoded_strings = solution.decode(encoded_string)
print(decoded_strings) # Output: [""]

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