'''
PROMPT: Write a function cast_vote() that records a vote for a candidate in an election.
The function accepts:
- votes: a dictionary mapping candidate names to their current vote counts
- candidate: a string representing the candidate receiving a vote

If the candidate exists, increment their vote count by 1.
If the candidate does not exist, add them to the dictionary with 1 vote.

Expected Output:
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice") -> {"Alice": 6, "Bob": 3}
cast_vote(votes, "Gina")  -> {"Alice": 6, "Bob": 3, "Gina": 1}
'''

# METHOD 1: Basic if-else approach (beginner-friendly)
def cast_vote_manual(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1  # Increment vote count
    else:
        votes[candidate] = 1   # Add new candidate with 1 vote
    return votes

# METHOD 2: More efficient using .get() with default value
def cast_vote_efficient(votes, candidate):
    votes[candidate] = votes.get(candidate, 0) + 1
    return votes

if __name__ == '__main__':
    votes = {"Alice": 5, "Bob": 3}
    
    print("Manual Method:")
    cast_vote_manual(votes, "Alice")
    print(votes)  # {"Alice": 6, "Bob": 3}
    
    cast_vote_manual(votes, "Gina")
    print(votes)  # {"Alice": 6, "Bob": 3, "Gina": 1}

    # Reset votes for next test
    votes = {"Alice": 5, "Bob": 3}

    print("\nEfficient Method:")
    cast_vote_efficient(votes, "Alice")
    print(votes)  # {"Alice": 6, "Bob": 3}
    
    cast_vote_efficient(votes, "Gina")
    print(votes)  # {"Alice": 6, "Bob": 3, "Gina": 1}
