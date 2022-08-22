def cria_conta(numero, titular, saldo, limite):
   conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
   return conta

def deposita(conta,valor):
   conta["saldo"] += valor

   
def saca(conta,valor):
   conta["saldo"] -= valor

def extrato(conta):
   print("saldo é {}".format(conta["saldo"]))


# from teste import cria_conta (em outras abas)
conta = cria_conta(123, "Paola", 500, 5000.0) 
deposita(conta, 15.0)
extrato(conta)
saca(conta, 65.0)
extrato(conta)

