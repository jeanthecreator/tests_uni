import os
import sys

# Adicionar diretório pai ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from bytebank import Funcionario

funcionario = Funcionario("Jean", 2020, 3000)
print(funcionario)


# class TestClass:

#     def test_criando_um_objeto_e_usando_o_metodo_idade(self):

#         entrada = '22/11/1988' #Given_Contexto
#         esperado = 35

#         funcionario_teste = Funcionario('Teste Automatio', entrada, 7000)
#         resultado = funcionario_teste.idade() #When_Ação

#         assert resultado == esperado # Then - Desfecho