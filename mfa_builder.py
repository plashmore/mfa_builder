import pandas as pd
import prince
answer="yes"
index=1
groups={}
master=pd.DataFrame()
while answer!="no":
    answer=input("Do you have more classes to include (yes/no):")
    while answer != "yes" and answer != "no":
        answer=input("Please input 'yes' or 'no':")
    if answer == "yes":
        file_name=input("Filename (include .csv):")
        df=pd.read_csv(file_name)
        group_name=input("Group name:")
        group_cols=df.columns.tolist()[1:]
        if index==1:
            master=df
        else:
            df2=df.drop(df.columns[0], axis=1)
            master=pd.concat([master,df2], axis=1)

    groups[group_name]=group_cols

    index=index+1

mfa=prince.MFA(n_components=2, n_iter=3, copy=True, check_input=True, engine='sklearn', random_state=42)

master2=master.drop(df.columns[0],axis=1)
mfa=mfa.fit(master2, groups=groups)
mfa.plot(master2, x_component=0, y_component=1)
