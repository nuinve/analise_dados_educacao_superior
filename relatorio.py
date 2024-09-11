from fpdf import FPDF

class PDF(FPDF):

    def titulo_capa(self,label):
        self.set_font('arial', 'B', size=16)
        self.cell(0, 65, label, 0, 1, 'C')

    def titulo(self, label):
        self.set_font('Arial', 'B', size=22)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('Arial', size=12)
        self.cell(0, -30, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('Arial', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('Arial', 'B', size=14)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def titulo_medio(self, label):
        self.set_font('Arial', size=14)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('Arial', size=12)
        self.multi_cell(0, 7, text, align='J')
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

pdf.add_page()

pdf.set_line_width(1.0)
pdf.rect(5, 5, 200, 287, 'D') #insere o retangulo ao redor


# Página de Título
pdf.titulo_capa("Análise da Desigualdade Educacional no Ensino Superior Brasileiro")
pdf.sub_titulo("Base de Dados: Censo da Educação Superior (2020), INEP")
pdf.imagem("img.png", 40, 80, 130)
pdf.ln(160)
pdf.linha_centralizada("Autor: Nubia Pereira")
pdf.linha_centralizada("Setembro de 2024")

# Página 2 - Introdução
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("O ensino superior é muito mais do que apenas um diploma; para muitas pessoas é a oportunidade de ascender socioeconômicamente, desenvolver habilidades e construir networking.")

pdf.paragrafo("O Censo, realizado anualmente pelo Inep, é o instrumento de pesquisa mais completo do Brasil sobre as instituições de educação superior (IES) que ofertam cursos de graduação e sequencias de formação específica, além de seus alunos e docentes.")

pdf.add_page()

pdf.titulo_base("Regiões onde há mais oferta de instituições de ensino superior")

pdf.imagem("Gráfico_região.png", 30, 30, 150)
pdf.ln(120)

pdf.paragrafo("Conforme filtrado os dados extraidos do censo, foi possivel analisar que a região sudeste e sul são as regiões com mais instituições de rede de ensino privado no Brasil, isso se dá devido a uma combinação de fatores históricos, econômicos e sociais. Com valores menores de instituições, nordeste, norte e centro-oeste representam 82% do território brasileiro, mas mesmo assim apresentam menor número de faculdades privadas e públicas. Com exceção do Nordeste, região que apresenta maior número de universidades públicas depois da região sudeste.")

pdf.paragrafo("também foi possivel notar que o ensino à distância é mais ofertado pelas instituições privadas. Isso gera um impasse para aqueles que nao tem renda o suficiente para ingressar por meio dessa rede, ficando sujeitos a ter que estudar e se dedicar mais para passar em uma faculdade pública, o que escala para outras questões como sociais e raciais.")

pdf.paragrafo("Portanto, é notório a desigualdade regional e disparidade na concentração de investimentos para a educação superior conforme as regiões no Brasil, limitando a possibilidade de muitos jovens ingressarem de modo gratuito e até mesmo pago por meio de instituição privada devido a baixa oferta de universidades nessas áreas, levando à necessidade de estar migrando para a região sudeste ou outra.")

# Página 3 - Preferência de Grau de Ensino
pdf.add_page()

pdf.titulo_base("Preferência de Grau de Ensino")

pdf.paragrafo("Ao analisar os dados referentes ao grau de ensino conferido ao aluno após a conclusão do curso, foi possível notar a preferência pelo modelo de ensino tecnólogo.")

pdf.imagem("Gráfico_grau.png", 22, 43, 165)
pdf.ln(99)

pdf.paragrafo("Isso pode ocorrer devido a diversos fatores como o custo, que tende a ser menor em relação ao bacharelado e a necessidade de trabalhar e se inserir no mercado de trabalho mais rápido, motivado a questões sociais e econômicas.\nAlém disso, o perfil do jovem que opta por esse grau são alunos de escola pública, dos quais tendem a ter menor renda por família. ")

pdf.imagem("Gráfico_perfil_tecnologo.png", 61, 189, 90) #quanto maior o numero do meio, mais baixo fica a imagem
pdf.ln(93)

# Página 4 - O Turno Importa
pdf.add_page()

pdf.titulo_base("O Turno Importa")

pdf.paragrafo("Ao analisar os dados, também foi possível observar a preferência dos alunos por estudar no período da noite, dessa forma, a crescente demanda por qualificação profissional tem levado muitos jovens a conciliarem estudos e trabalho durante o ensino superior. ")

pdf.imagem("turno.png", 18, 50, 170)
pdf.ln(112)

pdf.paragrafo("A necessidade de trabalhar durante o dia para se sustentar destaca-se nessa escolha. Porém, como consequência gera uma rotina cansativa, falta de tempo para se preparar para provas e atividades, e até mesmo lazer. De acordo com uma pesquisa realizada pelo IBGE, o Brasil registrou quase 8 milhões de jovens entre 15 e 29 anos estudando e trabalhando em 2022.")

pdf.paragrafo("Essa dupla jornada, embora admirável, impacta significativamente a saúde mental desses indivíduos. Gerenciar atividades acadêmicas, sociais e, muitas vezes, responsabilidades familiares, gera uma sobrecarga que pode levar ao esgotamento físico, emocional e estresse.  ")
# Página 5 - Panorama Racial
pdf.add_page()

pdf.titulo_base("Influência do ensino médio para ingresso no ensino superior ")

pdf.paragrafo("Através da análise, foi possivel observar que alunos que concluíram o ensino médio em escolas públicas, são maioria sobre os dados de evasão na faculdade. Esse é um problema complexo com diversas causas interligadas.")


pdf.imagem("Gráfico_evasao.png", 35, 65, 140)
pdf.ln(135)


pdf.paragrafo("A transição do ensino médio para a universidade é um momento desafiador para todos os alunos. Principalmente para aqueles que desejam estudar em uma instituição pública e tem que competir pela vaga por meio dos vestibulares. Porém, pode ser ainda mais difícil para aqueles que vêm de escolas públicas, visto que geralmente possuem menos autonomia. Além disso, a qualidade do ensino médio oferecido em escolas públicas pode variar muito, e muitos alunos demoram para passar no vestibular e chegam à universidade com defasagens em relação aos conteúdos básicos. Isso, somado à falta de apoio e à sindrome do impostor por nao se sentirem pertencentes ao ambiente universitário e nao serem capazes de acompanhar os colegas, ocasiona no trancamento do curso.")

pdf.add_page()
pdf.titulo_base("Panorama Racial na Educação Superior")

pdf.paragrafo("Conforme a análise, foi observado a predominância de alunos brancos, em contraste às pessoas pretas, que são minoria matriculadas no ensino superior.")

pdf.imagem("Gráfico_raca.png", 25, 50, 160)
pdf.ln(98)

pdf.paragrafo("De acordo com a Pesquisa Nacional por Amostra de Domicílios (Pnad) sobre educação de 2023, divulgada pelo IBGE, 29,5% das pessoas brancas de 18 a 24 anos estavam no ensino superior e 6,5% já tinham se formado. Entre os pretos e pardos, são apenas 16,4% cursando uma graduação e 2,9% com o diploma. Isso denuncia a desigualdade racial, onde pessoas brancas têm mais acesso à educação no país.")


pdf.imagem("Gráfico_concluintes.png", 15, 190, 170)
pdf.ln(93)

pdf.paragrafo("Alguns fatores que contribuem para essa realidade envolvem dificuldades financeiras. Alunos de escolas públicas vêm de famílias com menor renda, o que dificulta a conciliação dos estudos com o trabalho para se manter. A falta de recursos financeiros pode impedir o acesso a materiais didáticos, cursos preparatórios e outras ferramentas importantes para o sucesso acadêmico. Além disso, a desigualdade na educação básica afeta o desempenho no ensino superior.")


pdf.titulo_base("Conclusão")

pdf.paragrafo("Portanto, através da análise dos dados disponíveis pelo governo sobre o ensino superior no Brasil, foi possível observar as disparidades no acesso à educação superior, dos quais envolve questões raciais e a defasagem de aprendizado no ensino médio e como isso influencia na educação brasileira.")

pdf.paragrafo("Além disso, A educação é muito mais do que um simples caminho para um diploma ou um bom emprego. Ela é um dos pilares mais importantes para o desenvolvimento econômico de um país. A relação entre educação e economia é profunda e complexa, influenciando mutuamente diversos aspectos da sociedade.")

pdf.paragrafo("De acordo com a pesquisadora do IBGE, Betina Fresneda, o Brasil tem o maior retorno salarial para quem possui nível superior entre todos os países da OCDE. Portanto, é crucial que o governo e as instituições trabalhem juntos para reduzir as desigualdades, com investimentos na educação básica e políticas de permanência no ensino superior.")





pdf.add_page()

pdf.titulo_base("Referências Bibliográficas")

pdf.paragrafo("Acesso à universidade é menor para alunos da rede pública - Jornal Extra Classe: https://www.extraclasse.org.br/educacao/2018/12/acesso-a-universidade-e-menor-para-alunos-da-rede-publica/")
pdf.paragrafo("Desigualdade entre brancos e negros no ensino vai da alfabetização à universidade - O Globo: https://oglobo.globo.com/brasil/noticia/2024/03/26/desigualdade-entre-brancos-e-negros-no-ensino-vai-da-alfabetizacao-a-universidade.ghtml")
pdf.paragrafo("ALISSON, Eliton. ''A grande massa de estudantes que concluem o ensino médio em escolas públicas não considera o ingresso em universidades públicas'', diz Marcelo Knobel. Ensino Superior Unicamp, Campinas, 07 Fev. 2014. Disponível em: https://www.revistaensinosuperior.gr.unicamp.br/reportagens/a-grande-massa-de-estudantes-que-concluem-o-ensino-medio-em-escolas-publicas-nao-considera-o-ingresso-em-universidades-publicas-diz-marcelo-knobel>. Acesso em: 05 de Abril de 2017.")

pdf.output("relatorio.pdf")