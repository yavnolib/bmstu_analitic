import pandas as pd
import datetime
pand = pd.read_excel('s.xlsx')
# Заполним корректно все названия столбцов
# mas_rename_ind=[4,5,7,8,10,11]
# ind_count=0
# for number in mas_rename_ind:
#   pand.columns.values[number]=pand['Unnamed: '+str(number)][0]+str(ind_count//2+1)
#   ind_count+=1
# удалим иностранных абитуриентов и лишние строки, преобразуем коды специальностей в нормальный вид
last_num=int(input('введите последний номер иностранного абитуриента'))
all_num=[1,2,3]
for select_num in all_num:
  num=0
  for i in pand[str(select_num)+'-й конкурс']:
      if isinstance(i, datetime.date):
        lable=i.strftime('%Y-%m-%d')
        nums=lable.split('-')
        end='.'.join(nums)[2:]
        pand[str(select_num)+'-й конкурс'][num]=end
      num+=1
pand=pand[last_num+1:]
pand=pand.fillna(value='-')
checker_row=[ind for ind in range(last_num+1,len(pand)+last_num+1)]
del_id=[]
for i in checker_row:
  print(pand['Рег. №'][i],' ',i)
  if pand['Рег. №'][i] == 'Рег. №':
    del_id.append(i)
    del_id.append(i+1)
print(del_id)
correct_pand=pand.drop(del_id)
for elem in correct_pand['Рег. №']:
  print(elem)
indexes=[i for i in correct_pand['№']]
correct_pand.set_axis(indexes,inplace=True)
# На данном моменте в переменной correct_pand находится полностью верная таблица поступающих (без иностранных граждан). Можно приступать к анализу
all_=correct_pand['1-й конкурс'].value_counts()
def get_bvi(naprav:str):
  count_bvi=0
  for row in indik:
    if correct_pand['1-й конкурс'][row]==naprav:
      if correct_pand['Unnamed: 4'][row]=='БВИ':
        count_bvi+=1
  return count_bvi
bvi={}
for napnapnap in naprav:
  bvi.update({napnapnap:get_bvi(napnapnap)})
print(all_['01.03.02'], bvi['01.03.02'], my_naprav)
