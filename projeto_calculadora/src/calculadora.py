import math

class Calculadora :
  def __init__ ( self ) :
    self.historico = []
    self.resultado = 0
  
  def somar ( self , a , b ):
    if not isinstance (a , (int , float ) ) or not isinstance (b , (int , float ) ):
      raise TypeError (" Argumentos devem ser numeros ")
    resultado = a + b
    self.historico.append ( f"{a} + {b} = { resultado }")
    self.resultado = resultado
    return resultado
  
  def subtrair ( self , a , b ) :
    if not isinstance (a , (int , float ) ) or not isinstance (b , (int , float ) ):
      raise TypeError (" Argumentos devem ser numeros ")
    resultado = a - b
    self.historico.append ( f"{a} - {b} = { resultado }")
    self.resultado = resultado
    return resultado
  
  def multiplicar ( self , a , b ) :
    if not isinstance (a , (int , float ) ) or not isinstance (b , (int , float ) ):
      raise TypeError (" Argumentos devem ser numeros ")
    resultado = a * b
    self.historico.append ( f"{a} * {b} = { resultado }")
    self.resultado = resultado
    return resultado
  
  def dividir ( self , a , b) :
    if not isinstance (a , (int , float ) ) or not isinstance (b , (int , float ) ):
      raise TypeError (" Argumentos devem ser numeros ")
    if b == 0:
      raise ValueError (" Divisao por zero nao permitida ")
    resultado = a / b
    self.historico.append ( f"{a} / {b} = { resultado }")
    self.resultado = resultado
    return resultado
  
  def potencia ( self , base , expoente ) :
    if not isinstance ( base , (int , float ) ) or not isinstance ( expoente , (int , float ) ) :
      raise TypeError (" Argumentos devem ser numeros ")
    resultado = base ** expoente
    self.historico.append ( f"{ base } ^ { expoente } = { resultado }")
    self.resultado = resultado
    return resultado
  
  def limpar_historico ( self ):
    self.historico.clear ()
  
  def obter_ultimo_resultado ( self ) :
   return self.resultado

calc = Calculadora()
print(calc.somar(1,2))
