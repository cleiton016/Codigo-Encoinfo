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
        self.valor=50
        self.univercidade=univercidade
class Inscricao_de_Profissional(Inscricao):
    def __init__(self,univercidade):
        super().__init__()
        self.valor=50
        self.univercidade=univercidade
class Encoinfo:
    def __init__(self):
        self.inscritos=[]
    def atender(self,pessoa,inscricao,atendente):
        if len(self.inscritos)<50:
            self.inscritos.append(Inscrito(pessoa,inscricao,atendente))
            print('Ola! eu sou',atendente+'. Parabéns sua inscrição foi realizada com sucesso!')
        else:
            self.emitir_relatorio()
    def emitir_relatorio(self):
        ca,cprof,cprofi=0,0,0
        at={}
        for i in self.inscritos:
            at[i.atendente]=at.get(i.atendente,0)+1
            if type(i.inscricao)==Inscricao_de_Aluno:
                ca+=1
            elif type(i.inscricao)==Inscricao_de_Professor:
                cprof+=1
            else:
                cprofi+=1
        self.inprimir('Aluno','Professor','Profissional',ca,cprof,cprofi)
        lista=[]
        for  i in at:
            lista.append(i)
        self.inprimir(lista[0],lista[1],lista[2],at[lista[0]],at[lista[1]],at[lista[2]])
    def inprimir(self,n1,n2,n3,a,b,c):
        largura = 50
        print('=' * largura)
        print('** Relatório **'.center(largura))
        largura_a = int(.3 * largura)
        largura_b = int(.3 * largura)
        largura_c = int(.3 * largura)
        print('+{}+{}+{}+'.format('-' * largura_a,'-' * largura_b, '-' * largura_c))
        print('|{:^{lm}}|{:^{ln}}|{:^{lf}}|'.format(n1,n2,n3,
                                                    lm=largura_a, ln=largura_b, lf=largura_c))
        print('+{}+{}+{}+'.format('-' * largura_a,
                                  '-' * largura_b, '-' * largura_c))
        print('|{:^{lm}}|{:^{ln}}|{:^{lf}}|'.format(a,b,c,
                                                    lm=largura_a, ln=largura_b, lf=largura_c))
        print('+{}+{}+{}+'.format('-' * largura_a,
                                  '-' * largura_b, '-' * largura_c))
class Inscrito:
    def __init__(self,pessoa,inscricao,atendente):
        self.pessoa=pessoa
        self.inscricao=inscricao
        self.atendente=atendente
class Atendente(Pessoa):
    def __init__(self,nome,encoinfo):
        super().__init__(nome)
        self.encoinfo=encoinfo
    def atender(self, pessoa, inscricao):
        self.encoinfo.atender(pessoa,inscricao,self.nome)
e=Encoinfo()
atendentes=[Atendente('Atendente 1',e),Atendente('Atendente 2',e),Atendente('Atendente 3',e)]
univercidade=['CEULP-ULBRA','FACTO','IFTO','ITOP']
op=[Inscricao_de_Professor,Inscricao_de_Aluno,Inscricao_de_Profissional]
for n in range(51):
    p=Pessoa('José'+str(n))
    random.sample(atendentes,1)[0].atender(p,random.sample(op,1)[0](random.sample(univercidade,1)[0]))