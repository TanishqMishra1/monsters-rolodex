# Answer-1
class Solution:
    def longestPalindrome(self, s: str) -> int:
        pairs = 0
        unpaired_chars = set()
        
        for char in s:
            if char in unpaired_chars:
                pairs += 1
                unpaired_chars.remove(char)
            else:
                unpaired_chars.add(char)
        
        return pairs * 2 + 1 if unpaired_chars else pairs * 2

#Answer-2
A distributed system is a network that stores data on more than one node (physical or virtual machines) at the same time. 
Because all cloud applications are distributed systems, it’s essential to understand the CAP theorem when designing a cloud 
app so that you can choose a data management system that delivers the characteristics your application needs most.

The CAP theorem is also called Brewer’s Theorem, because it was first advanced by Professor Eric A.
Brewer during a talk he gave on distributed computing in 2000. Two years later, MIT professors Seth Gilbert and Nancy Lynch published a proof of “Brewer’s Conjecture.”

In theoretical computer science, the CAP theorem, also named Brewer's theorem after computer scientist Eric Brewer,
states that it is impossible for a distributed data store to simultaneously provide more than two out of the following three guarantees: 
Consistency: Every read receives the most recent write or an error. 