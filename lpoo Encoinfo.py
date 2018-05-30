import random
class Pessoa:
    def __init__(self,nome):
        self.nome=nome
class Inscricao:
    def __init__(self):
        self.valor=0
class Inscricao_de_Aluno(Inscricao):
    def __init__(self,univercidade):
        super().__init__()
        self.valor=50
        self.univercidade=univercidade
class Inscricao_de_Professor(Inscricao):
    def __init__(self,univercidade):
        super().__init__()
        self.valor=80
        self.univercidade=univercidade
class Inscricao_de_Profissional(Inscricao):
    def __init__(self,univercidade):
        super().__init__()
        self.valor=120
        self.univercidade=univercidade
class Encoinfo:
    def __init__(self):
        self.inscritos=[]
    def atender(self,pessoa,inscricao,atendente):
        if len(self.inscritos)<50:
            self.inscritos.append(Inscrito(pessoa,inscricao,atendente))
            atendente.total+=1
            if type(inscricao)==Inscricao_de_Aluno:
                atendente.qt_aluno+=1
            elif type(inscricao) == Inscricao_de_Professor:
                atendente.qt_prof+=1
            else:
                atendente.qt_profi+=1
            #print('Sua inscrição foi realizada com êxito!')
        else:
            self.emitir_relatorio()
    def emitir_relatorio(self):
        al,pr,pf,=0,0,0,
        nome=[]
        atendimento=[]
        aluno,prof,profi=[],[],[]
        for i in self.inscritos:
            if i.atendente.nome not in nome:
                nome.append(i.atendente.nome)
                atendimento.append(i.atendente.total)
                aluno.append(i.atendente.qt_aluno)
                prof.append(i.atendente.qt_prof)
                profi.append(i.atendente.qt_profi)
            if type(i.inscricao)==Inscricao_de_Aluno:
                al+=i.inscricao.valor
            elif type(i.inscricao) ==Inscricao_de_Professor:
                pr+=i.inscricao.valor
            else:
                pf+=i.inscricao.valor
        largura = 85
        print('=' * largura)
        print(' ** Relatório ** '.center(largura))
        largura_a = int(.19 * largura)
        largura_b = int(.19 * largura)
        largura_c = int(.19 * largura)
        largura_d = int(.19 * largura)
        largura_e = int(.19 * largura)
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_a, '-' * largura_b, '-' * largura_c,'-'*largura_d,'-'*largura_e))
        print('|{}|{:^{ln}}|{:^{lf}}|{:^{lm}}|{:^{tt}}|'.format(' '*largura_a,nome[0],nome[1],nome[2],'Total pago',
                                                                     lm=largura_b, ln=largura_c, lf=largura_d,tt=largura_e))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_a, '-' * largura_b, '-' * largura_c, '-' * largura_d,
                                        '-' * largura_e))
        print('|{:^{a}}|{:^{b}}|{:^{c}}|{:^{d}}|{}|'.format('QT-atendimento',atendimento[0],atendimento[1],atendimento[2],' '*largura_e,
                                                        a=largura_a, b=largura_b, c=largura_c,d=largura_d))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_a, '-' * largura_b, '-' * largura_c, '-' * largura_d,
                                        '-' * largura_e))
        print('|{:^{a}}|{:^{b}}|{:^{c}}|{:^{d}}|{:^{e}}|'.format('QT-Alunos', aluno[0], aluno[1],
                                                            aluno[2], al,
                                                            a=largura_a, b=largura_b, c=largura_c, d=largura_d,e=largura_e))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_a, '-' * largura_b, '-' * largura_c, '-' * largura_d,
                                        '-' * largura_e))
        print('|{:^{a}}|{:^{b}}|{:^{c}}|{:^{d}}|{:^{e}}|'.format('QT-Professores', prof[0], prof[1],
                                                                 prof[2], pr,
                                                                 a=largura_a, b=largura_b, c=largura_c, d=largura_d,
                                                                 e=largura_e))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_a, '-' * largura_b, '-' * largura_c, '-' * largura_d,
                                        '-' * largura_e))
        print('|{:^{a}}|{:^{b}}|{:^{c}}|{:^{d}}|{:^{e}}|'.format('QT-Profissionais', profi[0], profi[1],
                                                                 profi[2], pf,
                                                                 a=largura_a, b=largura_b, c=largura_c, d=largura_d,
                                                                 e=largura_e))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_a, '-' * largura_b, '-' * largura_c, '-' * largura_d,
                                       '-' * largura_e))
        print('|{:^{a}}|{}|{}|{}|{:^{e}}|'.format('Total geral',' '*largura_b, ' '*largura_c,
                                                                ' '*largura_d, al+pr+pf,
                                                                a=largura_a,e=largura_e))
        print('+{}+{}+{}+{}+{}+'.format('-' * largura_a, '-' * largura_b, '-' * largura_c, '-' * largura_d,
                                        '-' * largura_e))
class Inscrito:
    def __init__(self,pessoa,inscricao,atendente):
        self.pessoa=pessoa
        self.inscricao=inscricao
        self.atendente=atendente
class Atendente(Pessoa):
    def __init__(self,nome,encoinfo):
        super().__init__(nome)
        self.encoinfo=encoinfo
        self.total    = 0
        self.qt_aluno = 0
        self.qt_prof  = 0
        self.qt_profi = 0

e=Encoinfo()
atendentes=[Atendente('Cleiton',e),Atendente('Athos',e),Atendente('Crisley',e)]
univercidade=['CEULP-ULBRA','FACTO','IFTO','ITOP']
a=Inscricao_de_Aluno
p=Inscricao_de_Professor
op=[p,p,a,a,a,a,a,a,a,Inscricao_de_Profissional]
for n in range(51):
    p=Pessoa('José'+str(n))
    atendente=random.sample(atendentes,1)[0]
    inscricao=random.sample(op,1)[0]
    atendente.encoinfo.atender(p,inscricao(random.sample(univercidade,1)[0]),atendente)

