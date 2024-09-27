# Arquivo de entrada para desenvolvimento. Certifique-se de ler o README.md
import mean_var_std
from unittest import main

# Testando a função diretamente com a entrada fornecida
print(mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Rodar os testes automaticamente
main(module='test_module', exit=False)
