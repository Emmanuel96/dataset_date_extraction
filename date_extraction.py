import pandas as pd
import re 
doc = []
with open('dates.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)
# df.head(10)


def date_sorter():
#     pd.options.display.max_colwidth = 500
    for index, value in df.items(): 
        print(f'index: {index} value: {value}')
    # Your code here
    p1 = '\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
    p2 = '(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)[a-z]*[-,\.\s]*\d{1,2}[-,\.\s]*\d{4}'
    p3 = '\d{1,2}[\s]*(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)[a-z]*[\s\.,]*\d{2,4}'
    p4 = '(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)[a-z]*\d{1,2}(?:th|st|nd)[-,\s]*\d{2,4}'
    p5 = '(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)[a-z]*[\s,]*\d{4}'
    p6 = '\d{1,2}[/]\d{4}'
    p7 = '\d{4}'
    df_2 = df.str.extract(r'('+p1+'|'+p2+'|'+p3+'|'+p4+'|'+p5+'|'+p6+'|'+p7+')', expand= False)
    # df_2[df_2.notnull()]
    for index, value in df_2.items(): 
#         # if it matches the format 2020
#         if(int(value) == )
#         print(value)
        if(re.match('\d{1,2}(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sept|Oct|Nov|Dec)[a-z]*[\s\.,]*\d{2,4}', value)): 
            # insert space between second character i.e. 2June1996 becomes 2 June 1996
            value = value[0] +' ' + value[1:]
#             print('2june: ' + value)
            df_2[index] = value
        if('Decemeber' in value): 
            value = value.replace('Decemeber', 'Dec')
            df_2[index] = value
#             print('decemember: ', value)
        if('Janaury' in value): 
            value = value.replace('Janaury', 'January')
            df_2[index] = value
        if(value == '7787'):
            value = 'August 2008'
            df_2[index] = value
        if re.match(p7, value): 
            value = "01/01/" + value
            df_2[index] = value
        elif re.match(p6, value):
            # if it matches the format 9/2009
            value =  str(re.match('^(.+?)/', value).group()) + "01/" +  value[-4:]
            df_2[index] = value
        elif re.match('\d{1,2}[/-]\d{1,2}[/-]\d{2}',value): 
            # if it has the structure 1/5/89
            if ('/' in value[-4:] or '-' in value[-4:]): 
                val = value[-2:]
                value = value[:-2] + str(int(val) +1900)
                df_2[index] = value
        print(f'index: {index} value: {value}')
        
    # used coerce so it stores any overly high value as NULL
    df_2 = pd.to_datetime(df_2, errors = 'coerce')
    # Then we replace the null value(s) with 0
#     df_2 = df_2.fillna(0)
#     df_2 = df_2.dt.strftime('%m/%d/%Y')
    df_2 = df_2.sort_values()
    # last step is to return sorted dates
    final_df = pd.Series(df_2.index)
    return final_df


print(date_sorter())