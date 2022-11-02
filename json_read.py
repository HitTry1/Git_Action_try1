import json

json_file=open('DQ1.json','r')
json_data = json_file.read()

obj = json.loads(json_data)

#print(str(obj['basic']))
list = obj['basic']

#print(list)
#print(len(list))
#try :
  #  print(list['job_name'])
   # print(list[0].get('job_name'))
#except KeyError :
 #   print("key not found")


print("job_name :",list['job_name'])
print("job_desc  :",list['job_desc'])
print("tgt_data_obj :",list['tgt_data_obj'])
print("threshold_c : ",list['threshold_c'])
print("threshold_ce : ",list['threshold_ce'])




