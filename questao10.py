from test import test

def real_decorate(func):
    def func_wrapper(valor_inicial, juros, tempo):
        return "R$ {:.2f}".format(
            func(valor_inicial, juros, tempo))
    return func_wrapper

@real_decorate
def calculo_juros(valor_inicial, juros, tempo):
    return valor_inicial * ((1 + juros/100)**tempo)


def test_suite():    
    test(calculo_juros(100.0, 10.0, 2) == 'R$ 121.00')
    test(calculo_juros(100.0, 10.0, 2) != '$$ 121.00')
    test(calculo_juros(0.0, 10.0, 2) == 'R$ 0.00')
    test(calculo_juros(0.1, 10.0, 2) == 'R$ 0.12')

test_suite()