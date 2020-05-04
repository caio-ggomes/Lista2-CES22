class ITA_Subject:

    area = None
    enjoy = None

    def __init__(self, subject_name, professor):
        
        if subject_name[0] != self.area[0]:
            raise Exception("Invalid subject name for this area")
        
        self.professor = professor
        self.name = subject_name
    
    def study(self):
        print("I {0} studying {1}".format(self.enjoy, self.name))

    def avaliacao_do_curso(self, avaliacoes):
        avaliacao_total = avaliacoes[0]
        for i in range(1, len(avaliacoes)):
            avaliacao_total += avaliacoes[i]
        print('Avaliação final do curso: {}'.format(
            avaliacao_total))
        

class Computation_Subject(ITA_Subject):
    
    area = 'Computation'
    enjoy = 'like'

class Electronics_Subject(ITA_Subject):

    area = 'Electronics'
    enjoy = 'don\'t like'

class Mathematics_Subject(ITA_Subject):

    area = 'Mathematics'
    enjoy = 'love'

class Humanities_Subject(ITA_Subject):

    area = 'Humanities'
    enjoy = 'hate'


def main():
    MAT_12 = Mathematics_Subject('MAT-12', 'Luiz Augusto')
    CES_22 = Computation_Subject('CES-22', 'Karla')
    ELE_52 = Electronics_Subject('ELE-52', 'Douglas')
    #If you uncomment the line below the compilation 
    # will raise an exception.
    #CES_12 = Humanities_Subject('CES-12', 'Nilda')
    CES_22.study()
    ELE_52.study()
    # Veja que independente do tipo de avaliação (texto
    # ou nota de 0 a 10). O python conseguiu compilar o 
    # código, pois utiliza do duck_typing. Foi utilizado 
    # o símbolo '+' tanto para soma de strings quanto para 
    # soma de notas.
    CES_22.avaliacao_do_curso(['Muito bom.', 'Bom.', 
    'Sensacional.'])
    CES_22.avaliacao_do_curso([10.0, 9.5, 10.0])

main()