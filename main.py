from fordev.generators import people, cnh
from fordev.generators import company, renavam

pessoa = people(uf_code='PR', age=50)
empresa = renavam()
print(empresa)

