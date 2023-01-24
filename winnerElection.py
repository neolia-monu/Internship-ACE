from collections import Counter

votes =['john','johnny','jackie','johnny','john','jackie',
    'jamie','jamie','john','johnny','jamie','johnny','john']

vote_freq = Counter(votes)

max_vote = max(vote_freq.values())

# list comphression
lst = [i for i in vote_freq if i == max_vote]

print(so)