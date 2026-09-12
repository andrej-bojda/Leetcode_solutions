from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = "".join(f"{len(word)}#{word}" for word in strs)
        return encoded_strs

    def decode(self, s: str) -> List[str]:
        decoded_strs: List[str] = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1 + length
            decoded_strs.append(s[j + 1:i])
        return decoded_strs

