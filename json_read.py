import json

json_file=open('DQ1.json','r')
json_data = json_file.read()

obj = json.loads(json_data)

list = obj['basic']
print(list)
print(len(list))

for i in range(len(list)):
    print("job_name",list[i].get("job_name"))
    print("job_desc",list[i].get("job_desc"))
    print("tgt_data_obj",list[i].get("tgt_data_obj"))
    print("threshold_c",list[i].get("threshold_c"))
    print("threshold_ce",list[i].get("threshold_ce"))



