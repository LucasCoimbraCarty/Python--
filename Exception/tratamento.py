x = 5
y = 'hello'
z = x + y

#Instruções chamada try-except

while True:
    try:
        n1 = int(input('Numerador: '))
        n2 = int(input('Denominador: '))
    
        result = n1/n2

        if n1<0 or n2<0:
              raise TypeError
        
    except ValueError:
            print('Digite apenas números!!')
            print('Tente Novamente')
    except ZeroDivisionError:
            print('Denominador deve ser diferente de zero!!')
    except TypeError:
          print('O valor informado é negativo!!')
    except Exception:
            print('Ocorreu um erro!')
    else:
        print(f'Resultado: {result:.2f}')
    finally:
        print('Tchau, obrigado')