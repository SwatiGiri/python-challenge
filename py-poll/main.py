
import pandas as pd

data_file = "C:/Users/swati/Downloads/Python/03-Python/Homework/Instructions/PyPoll/raw_data/election_data_2.csv"

df = pd.read_csv(data_file)

# Header
print("Election Results")
print("-------------------------")


# Calculating total votes
total_votes = len(df)
print("Total Votes:", total_votes)
print("-------------------------")

# Finding Total Candidates
candidate_list = df["Candidate"].value_counts()
winner_name = ""
winner_votes = 0
for key, value in candidate_list.items():
    print(key, ": ", value/total_votes * 100, "% ", "(", value, ")", sep="")
    if value > winner_votes:
        winner_votes = value
        winner_name = key
print("-------------------------")
print("Winner:", winner_name)
print("-------------------------")

