import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("QueryResults.csv", names=["DATE", "TAG", "POSTS"], header=0)

# print(data.head())
# print(f"last five data: {data.tail()}")
# print(f"Number of row and column are: {data.shape}")
# print(f"Number of entries in each column: {data.count()}")
# total_post = data.groupby('TAG').count()
# print(total_post)
# total_post = data.groupby('TAG').sum()
# print(total_post)

# print(data['TAG'][0])

reshaped_df=data.pivot(index='DATE',columns="TAG", values="POSTS")
# print(reshaped_df)
# print(reshaped_df.fillna(0))
roll_df = reshaped_df.rolling(window=6).mean()
plt.figure(figsize=(8,6))
plt.ylim(0, 35000)
# chart =plt.plot(reshaped_df.index, reshaped_df.java)
# chart = plt.plot(reshaped_df.index, reshaped_df.python)
for column in roll_df.columns:
    plt.plot(reshaped_df.index, roll_df[column], linewidth=3, label=roll_df[column].name)
plt.xlabel("Date", fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
# print(chart)
plt.legend(fontsize=12)

plt.show()