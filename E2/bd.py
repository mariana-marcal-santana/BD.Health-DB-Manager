
import random
import random
from datetime import datetime, timedelta

ruas_lisboa = [
    "Rua Augusta", "Avenida da Liberdade", "Rua do Ouro", "Rua da Prata", 
    "Rua Garrett", "Rua do Carmo", "Rua dos Fanqueiros", "Rua dos Bacalhoeiros", 
    "Rua do Alecrim", "Rua das Portas de Santo Antão", "Rua de São Bento", 
    "Rua da Madalena", "Rua do Arsenal", "Rua do Comércio", "Rua da Conceição",
    "Rua dos Douradores", "Rua dos Correeiros", "Rua da Vitória", 
    "Rua da Misericórdia", "Rua de São Nicolau", "Rua da Saudade", 
    "Rua de São Paulo", "Rua da Boavista", "Rua do Conde de Redondo", 
    "Rua das Janelas Verdes", "Rua da Escola Politécnica", "Rua do Salitre", 
    "Rua Castilho", "Rua Tomás Ribeiro", "Rua Braamcamp", "Rua Rodrigo da Fonseca", 
    "Rua Barata Salgueiro", "Rua da Imprensa Nacional", "Rua de São José", 
    "Rua do Telhal", "Rua da Horta Seca", "Rua da Madalena", "Rua do Crucifixo", 
    "Rua de Santa Justa", "Rua do Carmo", "Rua dos Sapateiros", "Rua de São Julião", 
    "Rua de Santo António da Sé", "Rua do Benformoso", "Rua da Mouraria", 
    "Rua da Palma", "Rua dos Cavaleiros", "Rua de São Lázaro", "Rua de Arroios", 
    "Rua de Sapadores", "Rua Morais Soares", "Rua dos Anjos", "Rua do Forno do Tijolo", 
    "Rua da Penha de França", "Rua Visconde de Santarém", "Rua de Dona Estefânia", 
    "Rua Pascoal de Melo", "Rua do Conde Redondo", "Rua de Santa Marta", 
    "Rua Luciano Cordeiro", "Rua Alexandre Herculano", "Rua Braancamp", 
    "Rua Barata Salgueiro", "Rua Joaquim António de Aguiar", "Rua Castilho", 
    "Rua Rodrigo da Fonseca", "Rua das Amoreiras", "Rua de Campo de Ourique", 
    "Rua Ferreira Borges", "Rua Francisco Metrass", "Rua Saraiva de Carvalho", 
    "Rua Ferreira Borges", "Rua Dom João V", "Rua de São Bento", 
    "Rua do Sol ao Rato", "Rua da Escola Politécnica", "Rua de São Marçal", 
    "Rua do Século", "Rua da Imprensa Nacional", "Rua de São Bento", 
    "Rua dos Poiais de São Bento", "Rua de São Paulo", "Rua da Boavista", 
    "Rua dos Remolares", "Rua de São Paulo", "Rua da Cintura do Porto de Lisboa", 
    "Rua Cintura do Porto de Lisboa", "Rua do Instituto Industrial", 
    "Rua Dom Luís I", "Rua de São Bento", "Rua da Imprensa Nacional", 
    "Rua Nova do Loureiro", "Rua da Rosa", "Rua Dom Pedro V", "Rua da Atalaia", 
    "Rua do Norte", "Rua do Diário de Notícias", "Rua da Bica de Duarte Belo", 
    "Rua Marechal Saldanha", "Rua de São Mamede ao Caldas", "Rua de Santa Catarina", 
    "Rua da Academia das Ciências", "Rua de São Pedro de Alcântara", 
    "Rua do Conde de Soure", "Rua de São Bento", "Rua da Escola Politécnica", 
    "Rua de São Marçal", "Rua do Século", "Rua de O Século"
]

medicamentos = [
    "Paracetamol (Tylenol)",
    "Ibuprofeno (Advil, Motrin)",
    "Amoxicilina (Amoxil)",
    "Metformina (Glifage)",
    "Omeprazol (Losec, Prilosec)",
    "Simvastatina (Zocor)",
    "Atorvastatina (Lipitor)",
    "Losartana (Cozaar)",
    "Levotiroxina (Synthroid)",
    "Hidrocortisona (Cortef)",
    "Atenolol (Tenormin)",
    "Lisinopril (Prinivil, Zestril)",
    "Furosemida (Lasix)",
    "Amlodipina (Norvasc)",
    "Clopidogrel (Plavix)",
    "Sertralina (Zoloft)",
    "Escitalopram (Lexapro)",
    "Bupropiona (Wellbutrin)",
    "Trazodona (Desyrel)",
    "Ciprofloxacino (Cipro)",
    "Azitromicina (Zithromax)",
    "Fluoxetina (Prozac)",
    "Cetirizina (Zyrtec)",
    "Loratadina (Claritin)",
    "Diazepam (Valium)",
    "Alprazolam (Xanax)",
    "Tramadol (Ultram)",
    "Prednisona (Deltasone)",
    "Warfarina (Coumadin)",
    "Ranitidina (Zantac)",
    "Esomeprazol (Nexium)",
    "Cetamina (Ketalar)",
    "Dexametasona (Decadron)",
    "Metronidazol (Flagyl)",
    "Clindamicina (Cleocin)",
    "Sulfametoxazol/Trimetoprima (Bactrim, Septra)",
    "Gabapentina (Neurontin)",
    "Lamotrigina (Lamictal)",
    "Levetiracetam (Keppra)",
    "Carbamazepina (Tegretol)",
    "Oxcarbazepina (Trileptal)",
    "Venlafaxina (Effexor)",
    "Duloxetina (Cymbalta)",
    "Aspirina (Bayer)",
    "Diclofenaco (Voltaren)",
    "Meloxicam (Mobic)",
    "Naproxeno (Aleve)",
    "Pantoprazol (Protonix)",
    "Famotidina (Pepcid)"
]

clinicas = []
enfermeiros = []
medicos = []
trabalha = []
pacientes = []
consultas = []
receitas = []
observacoes = []


def criar_clinicas(num_clinicas):
    global clinicas
    ruas_lisboa = ["Rua A", "Rua B", "Rua C", "Rua D", "Rua E", "Rua F", "Rua G", "Rua H", "Rua I", "Rua J", "Rua K", "Rua L", "Rua M", "Rua N", "Rua O"]
    localidades = ["Lisboa", "Oeiras", "Cascais", "Sintra", "Amadora"]

    for i in range(num_clinicas):
        nome_clinica = f"Clinica {localidades[i % len(localidades)]} {chr(65 + i)}"
        telefone = "21" + "".join([str(random.randint(0, 9)) for _ in range(7)])
        morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} {random.choice(localidades)}"
        clinicas.append({"nome": nome_clinica, "telefone": telefone, "morada": morada})

    return clinicas


def escrever_clinicas_em_txt(clinicas):
    nome_arquivo = "populate1.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Clínicas\n")
        file.write("INSERT INTO clinica (nome, telefone, morada) VALUES\n")
        for clinica in clinicas:
            linha = f"('{clinica['nome']}', '{clinica['telefone']}', '{clinica['morada']}'),\n"
            file.write(linha)
    print('\n')
    return nome_arquivo

# Gerar dados das clínicas
num_clinicas = 5
clinicas = criar_clinicas(num_clinicas)

# Escrever os dados no arquivo .txt
nome_arquivo = escrever_clinicas_em_txt(clinicas)

print(f"Os dados das clínicas foram escritos em '{nome_arquivo}'.")

def criar_enfermeiros(num_enfermeiros, clinicas):
    global enfermeiros
    for clinica in clinicas:
        nome_clinica = clinica['nome']
        for i in range(1, num_enfermeiros + 1):
            nome_enfermeiro = f"Enfermeiro {nome_clinica.split()[-1][0]}{i}"
            nif = ''.join([str(random.randint(0, 9)) for _ in range(9)])
            telefone = "21" + "".join([str(random.randint(0, 9)) for _ in range(7)])
            morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} Lisboa"
            enfermeiros.append({"nif": nif, "nome": nome_enfermeiro, "telefone": telefone, "morada": morada, "nome_clinica": nome_clinica})
    return enfermeiros

def escrever_enfermeiros_em_txt(enfermeiros):
    nome_arquivo = "populate2.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Enfermeiros\n")
        file.write("INSERT INTO enfermeiro (nif, nome, telefone, morada, nome_clinica) VALUES\n")
        for enfermeiro in enfermeiros:
            linha = f"('{enfermeiro['nif']}', '{enfermeiro['nome']}', '{enfermeiro['telefone']}', '{enfermeiro['morada']}', '{enfermeiro['nome_clinica']}'),\n"
            file.write(linha)
    print('\n')
    return nome_arquivo

# Gerar dados dos enfermeiros
num_enfermeiros_por_clinica = 5
enfermeiros = criar_enfermeiros(num_enfermeiros_por_clinica, clinicas)

# Escrever os dados no arquivo .txt
nome_arquivo_enfermeiros = escrever_enfermeiros_em_txt(enfermeiros)

print(f"Os dados dos enfermeiros foram escritos em '{nome_arquivo_enfermeiros}'.")

def gerar_medicos():
    global medicos
    especialidades = ["clinica geral", "ortopedia", "cardiologia", "neurologia", "pediatria", "dermatologia", "urologia"]
    for i in range(1, 61):
        nif = str(i).zfill(9)
        nome_medico = f"Medico {i}"
        telefone = "2100000" + str(i + 20).zfill(2)
        morada = f"{random.choice(ruas_lisboa)}, 1000-{random.randint(100, 999)} Lisboa"
        especialidade = especialidades[(i - 1) // 10]  # Alterna a cada 10 médicos
        medicos.append({
            "nif": nif,
            "nome": nome_medico,
            "telefone": telefone,
            "morada": morada,
            "especialidade": especialidade
        })
    return medicos

def escrever_medicos_em_txt(medicos):
    nome_arquivo = "populate3.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Médicos\n")
        file.write("INSERT INTO medico (nif, nome, telefone, morada, especialidade) VALUES\n")
        for medico in medicos[:-1]:
            linha = f"('{medico['nif']}', '{medico['nome']}', '{medico['telefone']}', '{medico['morada']}', '{medico['especialidade']}'),\n"
            file.write(linha)
        medico = medicos[-1]
        linha = f"('{medico['nif']}', '{medico['nome']}', '{medico['telefone']}', '{medico['morada']}', '{medico['especialidade']}');\n"
        file.write(linha)
    print('\n')

# Uso das funções
medicos = gerar_medicos()
escrever_medicos_em_txt(medicos)
print("Os dados dos médicos foram escritos em 'medicos.txt'.")


def gerar_trabalha(medicos, clinicas):
    global trabalha
    clinicas_nomes = [clinica['nome'] for clinica in clinicas]

    medico_clinica_dias = {medico['nif']: {} for medico in medicos}

    # Atribuir cada médico a duas clínicas aleatórias, garantindo que não estejam alocados a mais de uma clínica no mesmo dia
    for medico in medicos:
        nif = medico['nif']
        clinicas_aleatorias = random.sample(clinicas_nomes, 2)

        for clinica_nome in clinicas_aleatorias:
            for dia_semana in range(7):
                if dia_semana not in medico_clinica_dias[nif]:
                    medico_clinica_dias[nif][dia_semana] = []

                if clinica_nome not in medico_clinica_dias[nif][dia_semana]:
                    medico_clinica_dias[nif][dia_semana].append(clinica_nome)
                    trabalha.append({
                        "nif": nif,
                        "nome": clinica_nome,
                        "dia_da_semana": dia_semana
                    })

    # Garantir que cada clínica tem até 8 médicos alocados em cada dia da semana
    clinica_dias_medicos = {clinica['nome']: {dia: [] for dia in range(7)} for clinica in clinicas}

    for clinica in clinicas:
        clinica_nome = clinica['nome']
        for dia_semana in range(7):
            medicos_disponiveis = [medico['nif'] for medico in medicos if medico['nif'] not in clinica_dias_medicos[clinica_nome][dia_semana]]

            medicos_alocados = random.sample(medicos_disponiveis, min(8, len(medicos_disponiveis)))

            for nif in medicos_alocados:
                clinica_dias_medicos[clinica_nome][dia_semana].append(nif)
                trabalha.append({
                    "nif": nif,
                    "nome": clinica_nome,
                    "dia_da_semana": dia_semana
                })

    return trabalha

def escrever_trabalha_em_txt(trabalha):
    nome_arquivo = "populate4.sql"
    with open(nome_arquivo, 'w') as file:
        file.write("-- Inserir Trabalha\n")
        file.write("INSERT INTO trabalha (nif, nome, dia_da_semana) VALUES\n")
        for entry in trabalha[:-1]:
            linha = f"('{entry['nif']}', '{entry['nome']}', {entry['dia_da_semana']}),\n"
            file.write(linha)
        entry = trabalha[-1]
        linha = f"('{entry['nif']}', '{entry['nome']}', {entry['dia_da_semana']});\n"
        file.write(linha)

# Uso das funções
trabalha = gerar_trabalha(medicos, clinicas)
escrever_trabalha_em_txt(trabalha)


def gerar_pacientes(num_pacientes, nif_inicial):
    global pacientes
    localidades = ['Alfama', 'Baixa', 'Belém', 'Chiado', 'Graça', 'Mouraria', 'Parque das Nações', 'Restelo', 'Areeiro', 'Campo de Ourique']
    
    for i in range(num_pacientes):
        contador = nif_inicial + i
        nome = f"Paciente {contador}"
        
        # Gerar código postal no formato XXXX-XXX
        codigo_postal = f"{random.randint(1000, 9999)}-{random.randint(100, 999)}"
        
        # Selecionar localidade aleatoriamente dentro de Lisboa
        localidade = random.choice(localidades)
        
        # Construir a morada
        morada = f"Rua {contador}, {codigo_postal} {localidade}"
        
        # Gerar ssn e nif
        ssn = f"{contador:011d}"
        nif = f"{contador:09d}"
        
        # Gerar telefone
        telefone = f"210{random.randint(1000000, 9999999)}"
        
        # Gerar data de nascimento
        ano = random.randint(1950, 2000)
        mes = random.randint(1, 12)
        dia = random.randint(1, 28)  # Simples para evitar problemas com meses curtos
        data_nasc = f"{ano:04d}-{mes:02d}-{dia:02d}"
        
        pacientes.append({
            "ssn": ssn,
            "nif": nif,
            "nome": nome,
            "telefone": telefone,
            "morada": morada,
            "data_nasc": data_nasc
        })
    
    return pacientes

def escrever_population_txt(pacientes):
    with open("populate5.sql", "w") as f:
        f.write("-- Inserir Pacientes\n")
        f.write("INSERT INTO paciente (ssn, nif, nome, telefone, morada, data_nasc) VALUES\n")
        
        values = []
        for p in pacientes:
            value = f"('{p['ssn']}', '{p['nif']}', '{p['nome']}', '{p['telefone']}', '{p['morada']}', '{p['data_nasc']}')"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

# Definir o número de pacientes e o NIF inicial (depois do último médico)
num_pacientes = 5000
nif_inicial = 601111112  # Ajustar conforme necessário

# Gerar dados dos pacientes
pacientes = gerar_pacientes(num_pacientes, nif_inicial)

# Escrever dados no arquivo population.txt
escrever_population_txt(pacientes)

def gerar_consultas(data_inicio, data_fim):
    global consultas
    global pacientes
    global medicos
    global clinicas
    global trabalha
    
    id_consulta = 1
    for paciente in pacientes :

        ssn = paciente['ssn']
        data_consulta = random_date(data_inicio, data_fim)
        hora_consulta = random_time_restrict()
        data_consulta = datetime.strptime(data_consulta, "%Y-%m-%d")
        # Obter médico aleatório
        medico = random.choice(medicos)
        nome_clinica = get_clinica(medico['nif'], data_consulta.weekday())
       
        while medico_tem_consulta_no_horario(medico, data_consulta, hora_consulta):
            hora_consulta = random_time_restrict()
           
        # Criar consulta com os dados gerados
        consulta = {
            "id": id_consulta,
            "ssn": ssn, 
            "nif": medico['nif'],
            "nome_clinica": nome_clinica,
            "data": data_consulta,
            "hora": hora_consulta,
            "codigo_sns": None
        }
        id_consulta += 1
        # Adicionar consulta à lista de consultas
        consultas.append(consulta)

    for day in range((data_fim - data_inicio).days + 1):
        
        data = data_inicio + timedelta(days=day)
        
        for clinica in clinicas:
            for i in range(1,20):
                medicos_clinica = get_medicos_clinica(data,clinica)
                medico = random.choice(medicos_clinica)
                ssn = random.choice(pacientes)['ssn']
                hora_consulta = random_time_restrict()
                while medico_tem_consulta_no_horario(medico, data, hora_consulta) or\
                    paciente_tem_consulta_no_horario(paciente, data, hora_consulta):
                    hora_consulta = random_time_restrict()
                consulta = {
                    "id": id_consulta,
                    "ssn": ssn,
                    "nif": medico['nif'],
                    "nome_clinica": clinica['nome'],
                    "data": data,
                    "hora": hora_consulta,
                    "codigo_sns": None
                }
                id_consulta += 1
                consultas.append(consulta)

        for medico in medicos:
            for i in range(1, 2):

                clinica = random.choice(clinicas)['nome']
                ssn = random.choice(pacientes)['ssn']
                hora_consulta = random_time_restrict()

                while medico_tem_consulta_no_horario(medico, data, hora_consulta) or\
                    paciente_tem_consulta_no_horario(paciente, data, hora_consulta):
                    hora_consulta = random_time_restrict()
                consulta = {
                    "id": id_consulta,
                    "ssn": ssn,
                    "nif": medico['nif'],
                    "nome_clinica": clinica,
                    "data": data,
                    "hora": hora_consulta,
                    "codigo_sns": None
                }
                id_consulta += 1
                consultas.append(consulta)
        
    return consultas



def paciente_tem_consulta_no_horario(paciente, data_consulta, hora_consulta):
    global consultas
    for consulta in consultas:
        if consulta['ssn'] == paciente['ssn'] and consulta['data'] == data_consulta and consulta['hora'] == hora_consulta:
            return True
    return False


def medico_tem_consulta_no_horario(medico, data_consulta, hora_consulta):
    global consultas
    for consulta in consultas:
        if consulta['nif'] == medico['nif'] and consulta['data'] == data_consulta and consulta['hora'] == hora_consulta:
            return True
    return False

def get_clinica(nif_medico, dia_semana):
    global trabalha
    for item in trabalha:
        if item['nif'] == nif_medico and item['dia_da_semana'] == dia_semana:
            return item['nome']

def random_date(start, end):
    # Gerar uma data aleatória dentro do intervalo especificado
    start_timestamp = start.timestamp()
    end_timestamp = end.timestamp()
    random_timestamp = random.uniform(start_timestamp, end_timestamp)
    random_date = datetime.fromtimestamp(random_timestamp)
    random_date_str = random_date.strftime("%Y-%m-%d")
    return random_date_str

def random_time_restrict():
    # Gerar uma hora aleatória entre 8:00 e 18:30, exceto entre 13:00 e 14:00
    hora = random.randint(8, 19)  
    minutos = random.choice([0, 30]) 
    while hora == 13 and minutos == 30:
        hora = random.randint(8, 19)  
        minutos = random.choice([0, 30]) 

    hora_consulta = '{:02d}:{:02d}:00'.format(hora, minutos)
    # Verificar se a hora está dentro do intervalo permitido
    return hora_consulta
    
def get_medicos_clinica(data, clinica):
    global medicos
    medicos_clinica = []
    for item in trabalha:
        if item['nome'] == clinica['nome'] and item['dia_da_semana'] == data.weekday():
            for medico in medicos:
                if medico['nif'] == item['nif']:
                    medicos_clinica.append(medico)
    return medicos_clinica
    
def generate_codigo_sns():
    return ''.join([str(random.randint(0, 9)) for _ in range(12)])

# Definir datas de início e fim
data_inicio = datetime(2023, 12, 1)
data_fim = datetime(2024, 1, 31)
# Uso das funções
consultas = gerar_consultas(data_inicio, data_fim)

# Escrever dados no arquivo consultas.sql
def escrever_consultas_em_sql(consultas):
    with open("populate6.sql", "w") as f:
        f.write("-- Inserir Consultas\n")
        f.write("INSERT INTO consulta (id,ssn, nif, nome, data, hora, codigo_sns) VALUES\n")
        
        values = []
        for consulta in consultas:
            if consulta['codigo_sns'] is not None:
                value = f"('{consulta['id']}','{consulta['ssn']}', '{consulta['nif']}', '{consulta['nome_clinica']}', '{consulta['data'].strftime('%Y-%m-%d')}', '{consulta['hora']}', '{consulta['codigo_sns']}')"
            else:
                value = f"('{consulta['id']}','{consulta['ssn']}', '{consulta['nif']}', '{consulta['nome_clinica']}', '{consulta['data'].strftime('%Y-%m-%d')}', '{consulta['hora']}', NULL)"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

escrever_consultas_em_sql(consultas)

def gerar_receitas():
    global consultas
    global receitas
    global medicamentos
    for consulta in consultas:
        if consulta['codigo_sns'] is not None:
            numero_medicamentos = random.randint(1, 6)
            for i in range(numero_medicamentos):
                medicamento = random.choice(medicamentos)
                quantidade = random.randint(1, 3)
                receitas.append({
                    "codigo_sns": consulta['codigo_sns'],
                    "medicamento": medicamento,
                    "quantidade": quantidade
                })
    
    return receitas


def escrever_receitas_em_sql(receitas):
    with open("populate7.sql", "w") as f:
        f.write("-- Inserir Receitas\n")
        f.write("INSERT INTO receita (codigo_sns, medicamento, quantidade) VALUES\n")
        
        values = []
        for receita in receitas:
            value = f"('{receita['codigo_sns']}', '{receita['medicamento']}', {receita['quantidade']})"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")
  
# Uso das funções
receitas = gerar_receitas()
escrever_receitas_em_sql(receitas)


sintomas = [
    'Dor de cabeça', 'Náusea', 'Vómito', 'Febre', 'Tosse',
    'Fadiga', 'Falta de ar', 'Tontura', 'Perda de apetite', 'Dor abdominal',
    'Diarreia', 'Constipação', 'Dor no peito', 'Dor nas articulações', 'Dor muscular',
    'Arrepios', 'Suores noturnos', 'Palpitações', 'Confusão mental', 'Visão turva',
    'Zumbido nos ouvidos', 'Formigamento', 'Comichão', 'Erupção cutânea', 'Inchaço',
    'Icterícia', 'Tosse com sangue', 'Dificuldade para engolir', 'Rigidez matinal',
    'Perda de peso inexplicável', 'Incontinência urinária', 'Urgência urinária', 'Dores de garganta',
    'Rouquidão', 'Sonolência', 'Alterações de humor', 'Depressão', 'Ansiedade',
    'Insônia', 'Pesadelos', 'Paralisia', 'Espasmos musculares', 'Fraqueza',
    'Tremores', 'Sensação de desmaio', 'Desmaios', 'Dor na lombar', 'Dor de dentes',
    'Queimação ao urinar', 'Alterações no paladar'
]

medicoes = [
    'Temperatura corporal', 'Frequência cardíaca', 'Pressão arterial sistólica', 'Pressão arterial diastólica', 'Saturação de oxigênio',
    'Nível de glicose no sangue', 'Peso corporal', 'Altura', 'Índice de massa corporal', 'Taxa de respiração',
    'Nível de colesterol total', 'Nível de HDL', 'Nível de LDL', 'Nível de triglicerídeos', 'Taxa de filtração glomerular',
    'Volume urinário', 'Taxa de sedimentação de eritrócitos', 'Hemoglobina', 'Contagem de leucócitos'
]

def gerar_observacoes():
    global consultas
    global sintomas
    global medicoes
    global observacoes
    for consulta in consultas:
        numero_sintomas = random.randint(1, 5)
        for i in range(numero_sintomas):
            sintoma = random.choice(sintomas)
            observacoes.append({
                "id": consulta['id'],
                "sintoma": sintoma,
                "valor" : None
            })
        numero_metricas = random.randint(0, 3)
        for i in range(numero_metricas):
            medicao = random.choice(medicoes)
            valor = random.uniform(0, 100)
            observacoes.append({
                "id": consulta['id'],
                "medicao": medicao,
                "valor": valor
            })
    return observacoes

def escrever_observacoes_em_sql(observacoes):
    with open("populate8.sql", "w") as f:
        f.write("-- Inserir Observações\n")
        f.write("INSERT INTO observacao (id, parametro, valor) VALUES\n")
        
        values = []
        for observacao in observacoes:
            if observacao['valor'] is not None:
                value = f"('{observacao['id']}', '{observacao['medicao']}', {observacao['valor']})"
            else:
                value = f"('{observacao['id']}', '{observacao['sintoma']}', NULL)"
            values.append(value)
        
        f.write(",\n".join(values))
        f.write(";")

# Uso das funções
observacoes = gerar_observacoes()
escrever_observacoes_em_sql(observacoes)
