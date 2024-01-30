import pandas as pd
file_path = 'docs/quests/DDA/dataset_datatypes.md/SpineSurgeryList(1).csv'
df_surgery = pd.read_csv(file_path)
print(df_surgery)
print(df_surgery.columns)
print(df_surgery[['체중', '신장']])


def caculate_bmi(params) :
    weight = params.loc['체중']
    height = params.loc['신장']
    result = weight / (height * 0.01)**2
    return result
df_surgery['BMI']= df_surgery[['체중', '신장']].apply(caculate_bmi, axis=1) # 컬럼 생성
result_round = round(df_surgery[['체중', '신장', 'BMI']], 2) #반올림
df_surgery['BMI'] = result_round['BMI']
print(df_surgery)
pass



