# Some helper functions

# TODO: Parameterize functions, you don't want to be touching this file every fking time

import numpy as np

#util
def timeStringToSeconds(time_str):
    minute = int(time_str[0])
    seconds = int(time_str[2:3])
    return (minute*60)+seconds

def makeTarget(rank):
    if rank >= 4:
        return 0
    else:
        return int(1/rank*10)
        #return 1

def getModelInput(df):
    return df.set_index(["race_id"]).sort_index(),df["race_id"].value_counts().sort_index()

def makePrizeTarget(df):
    prizeTargetList = []
    for index,row in df.iterrows():
        if row["rank"] >= 4:
            prizeTargetList.append(0)
        else:
            prizeTargetList.append((int(list(map(int,row["prize"][4:].replace("万円","").split(",")))[row["rank"]])) )
    return prizeTargetList

def makePassageValues(df):
    passage_4 = [
        [],[],[],[],
    ]
    for index,row in df.iterrows():
        if row["passage_rate"] != np.nan:
            passage_list = str(row["passage_rate"]).split("-")
            for i in range(len(passage_list)):
                passage_4[i].append(passage_list[i])
            if len(passage_list) != 4:
                for i in range(4 - len(passage_list)):
                    passage_4[3-i].append(np.nan)

        else:
            for i in range(4):
                passage_4[i].append(np.nan)

    return passage_4[0],passage_4[1],passage_4[2],passage_4[3]

