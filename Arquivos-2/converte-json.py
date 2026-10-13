import json
x = '{"name":"Lucas", "age":"12", "city":"Rio de Janeiro"}'
y = json.loads(x) #converte para dicionirio em python
print(y["age"])

outro_x = {"name":"Ribeiro", "age":"19", "city":"Paraná"}
outry = json.dumps(outro_x) #Converte para json
print(outry)