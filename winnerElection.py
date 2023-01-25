"""
    Dictionary and counter to find a winner of election
"""

from collections import Counter

votes =['john','johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john']

vote_freq = Counter(votes)

max_vote = max(vote_freq.values())

# list comphression
lst = [i for i in vote_freq if vote_freq[i] == max_vote]

print(sorted(lst)[0])

