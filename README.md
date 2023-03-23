# Maternal Health Track

## How to get the data from the Brazilian Platform
1. Open this [webpage](https://pcdas.icict.fiocruz.br/conjunto-de-dados/sistema-de-informacao-sobre-nascidos-vivos/)
2. Register yourself (Brazilian ID required)
3. Access and explore the data

## How to get the data from Google Drive
1. Download the data from this [link](https://drive.google.com/file/d/1D2RvrBoNO1dXt6CQy0CLJk7FNXvOpqjC/view?usp=share_link)
2. Place `ETLSINASC.zip` under a folder in the root called `data` 


## How to split the data into chunks

1. Run `python split_data.py`
2. The split CSV files will show up in a folder called `split`

## Variables Dictionary
(in Portuguese & translated to English)

| Variável | Tipo | Descrição | Description |
| --- | --- | --- | --- |
| ORIGEM | int8 | Sem descrição | No description |
| CODESTAB | text | Código de estabelecimento | Establishment code |
| CODMUNNASC | int8 | Município de ocorrência, em codificação idêntica a de CODMUNRES, conforme tabela TABMUN | Municipality of occurrence, in the same coding as CODMUNRES, according to the TABMUN table |
| LOCNASC | int8 | Local de ocorrência do nascimento, conforme a tabela: 9: Ignorado; 1: Hospital; 2: Outro Estab Saúde; 3: Domicílio; 4: Outros | Place of birth occurrence, according to the following table: 9: Unknown; 1: Hospital; 2: Other health establishment; 3: Home; 4: Others |
| def_loc_nasc | text | Local de nascimento (Nominal, com as seguintes classificações: Hospital; Outros estabelecimentos de saúde; Domicílio; Via pública; Outros; Ignorado) | Place of birth (Nominal, with the following classifications: Hospital; Other health establishments; Home; Public road; Others; Unknown) |
| IDADEMAE | int8 | Idade da mãe em anos | Age of mother in years |
| ESTCIVMAE | int8 | Estado civil, conforme a tabela: 1: Solteira; 2: Casada; 3: Viuva; 4: Separado judicialmente/Divorciado; 5: União consensual (versões anteriores); 9: Ignorado | Marital status, according to the table: 1: Single; 2: Married; 3: Widow; 4: Separated judicially/Divorced; 5: Consensual union (previous versions); 9: Unknown |
| def_est_civil | text | Estado civil (Situação conjugal: Solteiro; Casado; Viúvo; Separado judicialmente/divorciado; União estável; Ignorado) | Marital status (Marital status: Single; Married; Widow; Separated judicially/Divorced; Stable union; Unknown) |
| ESCMAE | int8 | Escolaridade, anos de estudo concluídos: 1: Nenhuma; 2: 1 a 3 anos; 3: 4 a 7 anos; 4: 8 a 11 anos; 5: 12 e mais; 9: Ignorado | Education, completed years of study: 1: None; 2: 1 to 3 years; 3: 4 to 7 years; 4: 8 to 11 years; 5: 12 or more; 9: Unknown |
| def_escol_mae | text | Escolaridade da mãe (Nenhuma; de 1 a 3 anos; de 4 a 7 anos; 8 a 11 anos; 12 anos e mais; Ignorado) | Mother's education (None; 1 to 3 years; 4 to 7 years; 8 to 11 years; 12 years or more; Unknown) |
| CODOCUPMAE | text | Ocupação, conforme a Classificação Brasileira de Ocupações (CBO-2002) | Occupation, according to the Brazilian Classification of Occupations (CBO-2002) |
| QTDFILVIVO | text | Número de filhos vivos | Number of children alive |
| QTDFILMORT | text | Número de filhos mortos | Number of children deceased |
| CODMUNRES | int8 | Município de residência da mãe, em codificação idêntica a deCODMUNNASC, conforme tabela TABMUN |Mother's municipality of residence, in code identical to that of CODMUNNASC, according to the TABMUN table
| GESTACAO | int8 | Semanas de gestação, conforme a tabela: 9: Ignorado; 1: Menos de 22 semanas; 2: 22 a 27 semanas; 3: 28 a 31 semanas; 4: 32 a 36 semanas; 5: 37 a 41 semanas; 6: 42 semanas e mais | Weeks of pregnancy, according to the table: 9: Unknown; 1: Less than 22 weeks; 2: 22 to 27 weeks; 3: 28 to 31 weeks; 4: 32 to 36 weeks; 5: 37 to 41 weeks; 6: 42 weeks and more |
| def_gestacao | text | Semana de gestação (Nominal, com as seguintes classificações: Menos de 22 semanas; 22 a 27 semanas; 28 a 31 semanas; 32 a 36 semanas; 37 a 41 semanas; 42 semanas ou mais) | Week of pregnancy (Nominal, with the following classifications: Less than 22 weeks; 22 to 27 weeks; 28 to 31 weeks; 32 to 36 weeks; 37 to 41 weeks; 42 weeks or more) |
| GRAVIDEZ | int8 | Tipo de gravidez, conforme a tabela: 9: Ignorado; 1: Única; 2: Dupla; 3: Tripla e mais | Type of pregnancy, according to the table: 9: Unknown; 1: Single; 2: Double; 3: Triple and more |
| def_gravidez | text | Tipo de gravidez (Nominal, com as seguintes classificações: Única; Dupla; Tripla e mais e Ignorada) | Type of pregnancy (Nominal, with the following classifications: Single; Double; Triple and more and Unknown) |
| PARTO | int8 | Tipo de parto, conforme a tabela: 9: Ignorado; 1: Vaginal; 2: Cesáreo | Type of delivery, according to the table: 9: Unknown; 1: Vaginal; 2: Cesarean |
| def_parto | text | Tipo de parto (Nominal, com as seguintes classificações: Vaginal; Cesáreo; Ignorado) | Type of delivery (Nominal, with the following classifications: Vaginal; Cesarean; Unknown) |
| CONSULTAS | int8 | Número de consultas de pré-natal: 1: Nenhuma; 2: de 1 a 3; 3: de 4 a 6; 4: 7 e mais; 9: Ignorado | Number of prenatal consultations: 1: None; 2: 1 to 3; 3: 4 to 6; 4: 7 or more; 9: Unknown |
| def_consultas | text | Número de consultas durante o pré-natal (Nenhuma; de 1 a 3; de 4 a 6; 7 e mais; Ignorado) | Number of consultations during prenatal (None; 1 to 3; 4 to 6; 7 or more; Unknown) |
| DTNASC | text | Data do nascimento, no formato ddmmaaaa | Date of birth, in the format ddmmaaaa |
| data_nasc | date | Data de nascimento | Date of birth |
| ano_nasc | int8 | Ano do nascimento | Year of birth |
| dia_semana_nasc | text | Dia da semana em que ocorreu o nascimento (dom; seg; ter; qua; qui; sex; sáb) | Day of the week on which the birth occurred (sun; mon; tue; wed; thu; fri; sat) |
| HORANASC | text | Horário de nascimento | Birth time |
| SEXO | int8 | Sexo, conforme a tabela: 0: Ignorado, não informado; 1: Masculino; 2: Feminino | Sex, according to table 1: Ignored, not reported; 1: Male; 2: Female |
| def_sexo | text | Sexo (Nominal, com as seguintes classificações: Masculino; Feminino; Ignorado) | Sex (Nominal, with the following classifications: Male; Female; Unknown) |
| APGAR1 | text | Apgar no primeiro minuto 00 a 10 | Apgar at first minute 00 to 10 |
| APGAR5 | text | Apgar no quinto minuto 00 a 10 | Apgar at fifth minute 00 to 10 |
| RACACOR | int8 | Raça/Cor: 1: Branca; 2: Preta; 3: Amarela; 4: Parda; 5: Indígena |
| def_raca_cor | text | Raça/cor (Nominal, com as seguintes classificações: Branca; Preta; Amarela; Parda; Indígena) | Race/Color (Nominal, with the following classifications: White; Black; Yellow; Brown; Indigenous) |
| PESO | text | Peso ao nascer, em gramas | Weight at birth, in grams |
| IDANOMAL | int8 | Anomalia congênita: 9: Ignorado; 1: Sim; 2: Não | Congenital anomaly: 9: Unknown; 1: Yes; 2: No |
| def_anomalia | text | Anomalia congênita (Ignorado; Sim; Não) | Congenital anomaly (Unknown; Yes; No) |
| DTCADASTRO | text | Data do cadastro da DN no sistema | Date of registration of the birth certificate in the system |
| CODANOMAL | text | Código de malformação congênita ou anomalia cromossômica, de acordo com a CID-10 | Code of congenital malformation or chromosomal anomaly, according to the CID-10 |
| NUMEROLOTE | int8 | Número do lote | Batch number |
| VERSAOSIST | text | Versão do sistema | System version |
| DTRECEBIM | text | Data de recebimento no nível central, data da última atualização do registro. | Date of receipt at the central level, date of the last update of the record. |
| DIFDATA | text | Diferença entre a data de óbito e data do recebimento original da DO ([DTNASC] – [DTRECORIG]) | Difference between the date of death and the original receipt date of the DO ([DTNASC] - [DTRECORIG]) |
| DTRECORIGA | text | Data do 1o recebimento do lote, dada pelo Sisnet. | Date of the 1st receipt of the batch, given by Sisnet. |
| NATURALMAE | int8 | Se a mãe for estrangeira, constará o código do país de nascimento. | If the mother is foreign, the country of birth code will be listed. |
| CODMUNNATU | int8 | Código do município de naturalidade da mãe | Code of the mother's place of birth |
| CODUFNATU | int8 | Código da UF de naturalidade da mãe | Code of the mother's state of birth |
| ESCMAE2010 | int8 | Escolaridade 2010. Valores: 0 – Sem escolaridade; 1 –Fundamental I (1a a 4a série); 2 – Fundamental II (5a a 8a série); 3 – Médio (antigo 2o Grau); 4 – Superior incompleto; 5 –Superior completo; 9 – Ignorado. | Education 2010. Values: 0 – No schooling; 1 – Elementary I (1st to 4th grade); 2 – Elementary II (5th to 8th grade); 3 – High school (old 2nd grade); 4 – Incomplete higher education; 5 – Complete higher education; 9 – Unknown. |
| SERIESCMAE | int8 | Série escolar da mãe. Valores de 1 a 8. | Mother's school year. Values from 1 to 8. |
| DTNASCMAE | text | Data de nascimento da mãe | Mother's date of birth |
| RACACORMAE | int8 | Raça/cor da mãe | Mother's race/color |
| QTDGESTANT | text | Número de gestações anteriores | Number of previous pregnancies |
| QTDPARTNOR | text | Número de partos vaginais | Number of vaginal births |
| QTDPARTCES | text | Número de partos cesáreos | Number of cesarean births |
| IDADEPAI | int8 | Idade do pai | Father's age |
| DTULTMENST | text | Data da última menstruação (DUM): dd mm aaaa | Date of last menstruation (DUM): dd mm aaaa |
| SEMAGESTAC | int8 | Número de semanas de gestação. | Number of weeks of gestation. |
| TPMETESTIM | int8 | Método utilizado. Valores: 1– Exame físico; 2– Outro método; 9– Ignorado. | Method used. Values: 1– Physical exam; 2– Other method; 9– Unknown. |
| CONSPRENAT | text | Número de consultas pré‐natal | Number of prenatal consultations |
| MESPRENAT | text | Mês de gestação em que iniciou o pré‐natal | Month of pregnancy when prenatal care began | 
| TPAPRESENT | int8 | Tipo de apresentação do RN. Valores: 1– Cefálico; 2– Pélvica ou podálica; 3– Transversa; 9– Ignorado. | Type of presentation of the RN. Values: 1– Cephalic; 2 – Pelvic or foot; 3- Transversal; 9 – Ignored. |
| STTRABPART | int8 | Trabalho de parto induzido? Valores: 1– Sim; 2– Não; 3– Não se aplica; 9– Ignorado. | Induced labor? Values: 1– Yes; 2– No; 3– Not applicable; 9– Unknown. |
| STCESPARTO | int8 | Cesárea ocorreu antes do trabalho de parto iniciar? Valores: 1–Sim; 2– Não; 3– Não se aplica; 9– Ignorado. | Cesarean occurred before labor started? Values: 1– Yes; 2– No; 3– Not applicable; 9– Unknown. |
| TPNASCASSI | int8 | Nascimento foi assistido por? Valores: 1– Médico; 2–Enfermeira/obstetriz; 3– Parteira; 4– Outros; 9– Ignorado. | Birth was assisted by? Values: 1– Doctor; 2– Nurse/midwife; 3– Midwife; 4– Others; 9– Unknown. |
| TPFUNCRESP | int8 | Tipo de função do responsável pelo preenchimento. Valores:1– Médico; 2– Enfermeiro; 3– Parteira; 4– Funcionário docartório; 5– Outros. | Type of function of the person responsible for filling out. Values: 1– Doctor; 2– Nurse; 3– Midwife; 4– Registry office employee; 5– Others. |
| TPDOCRESP | int8 | Tipo do documento do responsável. Valores: 1‐CNES; 2‐CRM; 3‐COREN; 4‐RG; 5‐CPF. | Type of document of the responsible. Values: 1‐CNES; 2‐CRM; 3‐COREN; 4‐RG; 5‐CPF. |
| DTDECLARAC | text | Data da declaração: dd mm aaaa | Date of the declaration: dd mm aaaa |
| ESCMAEAGR1 | text | Escolaridade 2010 agregada. Valores: 00 – Sem Escolaridade; 01 – Fundamental I Incompleto; 02 – Fundamental I Completo; 03 – Fundamental II Incompleto; 04 – Fundamental II Completo; 05 – Ensino Médio Incompleto; 06 – Ensino Médio Completo; 07 – Superior Incompleto; 08 – Superior Completo; 09 – Ignorado; 10 – Fundamental I Incompleto ou Inespecífico; 11 – Fundamental II Incompleto ou Inespecífico; 12 – EnsinoMédio Incompleto ou Inespecífico. | Education 2010 aggregated. Values: 00 – No schooling; 01 – Elementary I Incomplete; 02 – Elementary I Complete; 03 – Elementary II Incomplete; 04 – Elementary II Complete; 05 – High school Incomplete; 06 – High school Complete; 07 – Incomplete higher education; 08 – Complete higher education; 09 – Unknown; 10 – Elementary I Incomplete or unspecified; 11 – Elementary II Incomplete or unspecified; 12 – High school Incomplete or unspecified. |
| STDNEPIDEM | int8 | Status de DO Epidemiológica. Valores: 1 – SIM; 0 – NÃO. | Status of Epidemiological DO. Values: 1 – YES; 0 – NO. |
| STDNNOVA | int8 | Status de DO Nova. Valores: 1 – SIM; 0 – NÃO. | Status of New DO. Values: 1 – YES; 0 – NO. |
| CODPAISRES | int8 | Código do país de residência | Country code of residence |
| TPROBSON | text | Código do Grupo de Robson, gerado pelo sistema | Code of the Robson Group, generated by the system |
| PARIDADE | int8 | Sem descrição | No description |
| KOTELCHUCK | int8 | Sem descrição | No description |
| nasc_MUNNOME | text | Nome do município de nascimento | Name of the municipality of birth |
| nasc_MUNNOMEX | text | Nome do município de nascimento em maiúsculas e sem acentos | Name of the municipality of birth in uppercase and without accents |
| nasc_AMAZONIA | text | Indica (S/N) se o município de nascimento faz parte da Amazônia Legal (conforme IBGE) | Indicates (Y/N) if the municipality of birth is part of the Legal Amazon (according to IBGE) |
| nasc_FRONTEIRA | text | Indica (S/N) se o município de nascimento faz parte da faixa de fronteira (conforme IBGE) | Indicates (Y/N) if the municipality of birth is part of the border strip (according to IBGE) |
| nasc_CAPITAL | text | Indica (S/N) se o município de nascimento é capital de UF | Indicates (Y/N) if the municipality of birth is the capital of the UF | 
| nasc_MSAUDCOD | int8 | Código da Macrorregional de Saúde a que o Município de nascimento pertence | Code of the Macroregional Health Unit to which the Municipality of birth belongs |
| nasc_RSAUDCOD | int8 | Código da Regional de Saúde a que o Município de nascimento pertence | Code of the Regional Health Unit to which the Municipality of birth belongs |
| nasc_CSAUDCOD | int8 | Código da Microrregional de Saúde a que o Município de nascimento pertence | Code of the Microregional Health Unit to which the Municipality of birth belongs |
| nasc_LATITUDE | float8 | Latitude do município de nascimento | Latitude of the municipality of birth |
| nasc_LONGITUDE | float8 | Longitude do município de nascimento | Longitude of the municipality of birth |
| nasc_ALTITUDE | int8 | Altitude do município de nascimento | Altitude of the municipality of birth |
| nasc_AREA | float8 | Área do município de nascimento | Area of the municipality of birth |
| nasc_codigo_adotado | int8 | Armazena o código atribuído ao município de nascimento atualmente, tratando os casos em que múltiplos códigos tenham sido utilizados para um mesmo município ao longo do tempo | Stores the code assigned to the municipality of birth currently, treating the cases in which multiple codes have been used for the same municipality over time |
| res_MUNNOME | text | Nome do município de residência | Name of the municipality of residence |
| res_MUNNOMEX | text | Nome do município de residência em maiúsculas e sem acentos | Name of the municipality of residence in uppercase and without accents |
| res_AMAZONIA | text | Indica (S/N) se o município de residência faz parte da Amazônia Legal (conforme IBGE) | Indicates (Y/N) if the municipality of residence is part of the Legal Amazon (according to IBGE) |
| res_FRONTEIRA | text | Indica (S/N) se o município de residência faz parte da faixa de fronteira (conforme IBGE) | Indicates (Y/N) if the municipality of residence is part of the border strip (according to IBGE) |
| res_CAPITAL | text | Indica (S/N) se o município de residência é capital de UF | Indicates (Y/N) if the municipality of residence is the capital of the UF |
| res_MSAUDCOD | int8 | Código da Macrorregional de Saúde a que o Município de residência pertence | Code of the Macroregional Health Unit to which the Municipality of residence belongs |
| res_RSAUDCOD | int8 | Código da Regional de Saúde a que o Município de residência pertence | Code of the Regional Health Unit to which the Municipality of residence belongs |
| res_CSAUDCOD | int8 | Código da Microrregional de Saúde a que o Município de residência pertence | Code of the Microregional Health Unit to which the Municipality of residence belongs |
| res_LATITUDE | float8 | Latitude do município de residência | Latitude of the municipality of residence |
| res_LONGITUDE | float8 | Longitude do município de residência | Longitude of the municipality of residence |
| res_ALTITUDE | int8 | Altitude do município de residência | Altitude of the municipality of residence |
| res_AREA | float8 | Área do município de residência | Area of the municipality of residence |
| res_codigo_adotado | int8 | Armazena o código atribuído ao município de residência atualmente, tratando os casos em que múltiplos códigos tenham sido utilizados para um mesmo município ao longo do tempo | Stores the code assigned to the municipality of residence currently, treating the cases in which multiple codes have been used for the same municipality over time |
| nasc_SIGLA_UF          | text      | Sigla da unidade da federação de nascimento | Abbreviation of the federal unit of birth | 
| nasc_CODIGO_UF         | int8      | Código da UF de nascimento | Code of the UF of birth | 
| nasc_NOME_UF           | text      | Nome da unidade da federação de nascimento | Name of the federal unit of birth |
| res_SIGLA_UF           | text      | Sigla da unidade da federação de residência | Abbreviation of the federal unit of residence |
| res_CODIGO_UF          | int8      | Código da UF de residência | Code of the UF of residence |
| res_NOME_UF            | text      | Nome da unidade da federação de residência                                                            | Name of the federal unit of residence |
| nasc_REGIAO            | text      | Nome da região da unidade da federação de nascimento                                                 | Name of the region of the federal unit of birth |
| res_REGIAO             | text      | Nome da região da unidade da federação de residência                                                  | Name of the region of the federal unit of residence |
| codanomal_capitulo     | text      | Capítulo CID-10 da malformação congênita ou anomalia cromossômica | ICD-10 Code of the congenital malformation or chromosomal anomaly |
| codanomal_grupo        | text      | Grupo CID-10 da malformação congênita ou anomalia cromossômica                                        | ICD-10 Code of the congenital malformation or chromosomal anomaly |
| codanomal_categoria    | text      | Categoria CID-10 da malformação congênita ou anomalia cromossômica                                    | ICD-10 Code of the congenital malformation or chromosomal anomaly |
| codanomal_subcategoria | text      | Subcategoria CID-10 da malformação congênita ou anomalia cromossômica                                 | ICD-10 Code of the congenital malformation or chromosomal anomaly |
| nasc_coordenadas       | text      | Coordenadas do município de nascimento                                                               | Coordinates of the municipality of birth |
| res_coordenadas        | text      | Coordenadas do município de residência                                                               | Coordinates of the municipality of residence |
| parto_prematuro        | int8      | ndica a prematuridade do nascimento. 0: não há indícios de prematuridade; 1: há indício de prematuridade dado pela idade gestacional (GESTACAO<=4); 2: há indício de prematuridade dado pelo peso ao nascer (PESO<2500); 3: a idade gestacional e o peso ao nascer indicam prematuridade | Indicates the prematurity of the birth. 0: there are no indications of prematurity; 1: there is a hint of prematurity given by the gestational age (GESTACAO <= 4); 2: there is a hint of prematurity given by the weight at birth (PESO <2500); 3: the gestational age and the weight at birth indicate prematurity |
| def_parto_prematuro    | text      | Indica a prematuridade do nascimento. Termo: não há indícios de prematuridade; Inconclusivo-IG: há indício de prematuridade dado pela idade gestacional (GESTACAO<=4); Inconclusivo-Peso: há indício de prematuridade dado pelo peso ao nascer (PESO<2500); Prematuro: a idade gestacional e o peso ao nascer indicam prematuridade | Indicates the prematurity of the birth. Term: there are no indications of prematurity; Inconclusive-IG: there is a hint of prematurity given by the gestational age (GESTACAO <= 4); Inconclusive-Weight: there is a hint of prematurity given by the weight at birth (PESO <2500); Premature: the gestational age and the weight at birth indicate prematurity |

## Variables Dictionary (in English)

| Variable | Type | Description |
| --- | --- | --- |
| ORIGIN | int8 | No description |
| CODESTAB | text | Establishment code |
| CODMUNNASC | int8 | Municipality of occurrence, in code identical to that of CODMUNRES, according to table TABMUN |
| LOCNASC | int8 | Place of birth, according to the table: 9: Unknown; 1: Hospital; 2: Other Health Estab; 3: Domicile; 4: Others |
| def_loc_born | text | Place of birth (Nominal, with the following classifications: Hospital; Other health facilities; Home; Public road; Other; Unknown) |
| IDADEMAE | int8 | Mother's age in years |
| ESTCIVMAE | int8 | Marital status, according to the table: 1: Single; 2: Married; 3: Widow; 4: Judicially separated/Divorced; 5: Consensual union (previous versions); 9: Skipped |
| def_est_marital | text | Marital status (Marital status: Single; Married; Widowed; Judicially separated/divorced; Stable union; Unknown) |
| ESCMAE | int8 | Education, years of study completed: 1: None; 2: 1 to 3 years; 3: 4 to 7 years old; 4: 8 to 11 years old; 5: 12 and more; 9: Skipped |
| def_choice_mother | text | Mother's education (None; 1 to 3 years; 4 to 7 years; 8 to 11 years; 12 years and more; Unknown) |
| CODOCUPMAE | text | Occupation, according to the Brazilian Classification of Occupations (CBO-2002) |
| QTDFILVIVO | text | Number of living children |
| QTDFILMORT | text | Number of children killed |
| CODMUNRES | int8 | Mother's municipality of residence, in code identical to that of CODMUNNASC, according to table TABMUN |
| PREGNANCY | int8 | Weeks of gestation, according to the table: 9: Unknown; 1: Less than 22 weeks; 2: 22 to 27 weeks; 3: 28 to 31 weeks; 4: 32 to 36 weeks; 5: 37 to 41 weeks; 6: 42 weeks and more |
| def_gestation | text | Pregnancy week (Nominal, with the following classifications: Less than 22 weeks; 22 to 27 weeks; 28 to 31 weeks; 32 to 36 weeks; 37 to 41 weeks; 42 weeks or more) |
| PREGNANCY | int8 | Type of pregnancy, according to the table: 9: Unknown; 1: Single; 2: Double; 3: Triple and more |
| def_pregnancy | text | Type of pregnancy (Nominal, with the following classifications: Single; Double; Triple and more and Unknown) |
| BIRTH | int8 | Type of delivery, according to the table: 9: Unknown; 1: Vaginal; 2: Cesarean section |
| def_parto | text | Type of delivery (Nominal, with the following classifications: Vaginal; Cesarean; Unknown) |
| CONSULTATIONS | int8 | Number of prenatal consultations: 1: None; 2: from 1 to 3; 3: from 4 to 6; 4: 7 and more; 9: Skipped |
| def_queries | text | Number of consultations during prenatal care (None; from 1 to 3; from 4 to 6; 7 and more; Unknown) |
| DTNASC | text | Date of birth, in yyyymmdd format |
| date_birth | date | Date of birth |
| year_birth | int8 | Year of birth |
| day_week_birth | text | Day of the week on which the birth occurred (Sun; Mon; Tue; Wed; Thu; Fri; Sat) |
| HORANASC | text | Birth time |
| SEX | int8 | Gender, according to the table: 0: Unknown, not informed; 1: Male; 2: Female |
| def_sex | text | Gender (Nominal, with the following classifications: Male; Female; Unknown) |
| APGAR1 | text | Apgar in the first minute 00 to 10 |
| APGAR5 | text | Apgar in the fifth minute 00 to 10 |
| RACACOR | int8 | Race/Color: 1: White; 2: Black; 3: Yellow; 4: Brown; 5: Indigenous |
| def_race_color | text | Race/Color (Nominal, with the following classifications: White; Black; Yellow; Brown; Indigenous) |
| WEIGHT | text | Birth weight, in grams |
| IDANOMAL | int8 | Congenital anomaly: 9: Unknown; 1: Yes; 2: No |
| def_anomaly | text | Congenital anomaly (Unknown; Yes; No) |
| DTCADASTRO | text | Date of DN registration in the system |
| CODANOMAL | text | Code of congenital malformation or chromosomal anomaly, according to ICD-10 |
| BATCH NUMBER | int8 | Batch number |
| VERSAOSIST | text | System version |
| DTRECEBIM | text | Date received at central level, date of last record update. |
| DIFDATE | text | Difference between date of death and date of original receipt of DO ([DTNASC] – [DTRECORIG]) |
| DTRECORIGA | text | Date of the 1st batch receipt, given by Sisnet. |
| NATURALMAE | int8 | If the mother is a foreigner, the code of the country of birth will be included. |
| CODMUNNATU | int8 | Code of the mother's place of birth |
| CODUFNATU | int8 | Mother's State of Birth Code |
| ESCMAE2010 | int8 | Schooling 2010. Values: 0 – No schooling; 1 – Fundamental I (1st to 4th grade); 2 – Fundamental II (5th to 8th grade); 3 – Middle (former 2nd Grade); 4 – Incomplete higher education; 5 – Complete higher education; 9 – Ignored. |
| SERIESCMAE | int8 | Mother's school series. Values from 1 to 8. |
| DTNASCMAE | text | Mother's date of birth |
| RACACORMAE | int8 | Mother's race/color |
| QTDMANAGEMENT | text | Number of previous pregnancies |
| QTDPARTNOR | text | Number of vaginal deliveries |
| QTDPARTCES | text | Number of cesarean deliveries |
| FATHERAGE | int8 | Father's age |
| DTULTMENST | text | Date of last menstruation (LMP): dd mm yyyy |
| SEMAGESTAC | int8 | number of weeks
| TPMETESTIM | int8 | Method used. Values: 1– Physical examination; 2- Another method; 9 – Ignored. |
| CONSPRENAT | text | Number of prenatal consultations |
| MESPRENAT | text | Month of pregnancy in which prenatal care started |
| TPAPRESENT | int8 | Type of presentation of the RN. Values: 1– Cephalic; 2 – Pelvic or foot; 3- Transversal; 9 – Ignored. |
| STTRABPART | int8 | Induced labor? Values: 1– Yes; 2- No; 3– Not applicable; 9 – Ignored. |
| STCESPARTO | int8 | Did the cesarean section occur before labor started? Values: 1–Yes; 2- No; 3– Not applicable; 9 – Ignored. |
| TPNASCASSI | int8 | Birth was attended by? Values: 1– Physician; 2–Nurse/midwife; 3- Midwife; 4– Others; 9 – Ignored. |
| TPFUNCRESP | int8 | Type of role of person responsible for completing the form. Values: 1– Physician; 2 – Nurse; 3- Midwife; 4– Registry clerk; 5– Others. |
| TPDOCRESP | int8 | Responsible document type. Values: 1-CNES; 2-CRM; 3-COREN; 4-RG; 5-CPF. |
| DTDECLARAC | text | Declaration date: dd mm yyyy |
| ESCMAEAGR1 | text | 2010 aggregate schooling. Values: 00 – No Education; 01 – Elementary I Incomplete; 02 – Elementary I Complete; 03 – Elementary II Incomplete; 04 – Complete Elementary II; 05 – Incomplete High School; 06 – Complete High School; 07 – Incomplete Higher Education; 08 – Complete Superior; 09 – Ignored; 10 – Fundamental I Incomplete or Unspecific; 11 – Elementary School II Incomplete or Unspecific; 12 – Incomplete or Unspecific High School. |
| STDNEPIDEM | int8 | Epidemiological DO Status. Values: 1 – YES; 0 – NO. |
| STDNNOVA | int8 | New DO status. Values: 1 – YES; 0 – NO. |
| CODPAISRES | int8 | Country of residence code |
| TPROBSON | text | Robson Group Code, generated by the system |
| PARITY | int8 | No description |
| KOTELCHUCK | int8 | No description |
| born_MUNNOME | text | Name of city of birth |
| born_MUNNOMEX | text | Name of the municipality of birth in capital letters and without accents |
| born_AMAZONIA | text | Indicates (Y/N) if the municipality of birth is part of the Legal Amazon (according to IBGE) |
| born_BORDER | text | Indicates (Y/N) if the municipality of birth is part of the border strip (according to IBGE) |
| born_CAPITAL | text | Indicates (Y/N) if the city of birth is the capital of UF |
| born_MSAUDCOD | int8 | Macroregional Health Code to which the municipality of birth belongs |
| born_RSAUDCOD | int8 | Regional Health Code to which the municipality of birth belongs |
| born_CSAUDCOD | int8 | Microregional Health Code to which the municipality of birth belongs |
| born_LATITUDE | float8 | Latitude of birth county |
| born_LONGITUDE | float8 | Longitude of county of birth |
| born_ALTITUDE | int8 | Altitude of birth municipality |
| born_AREA | float8 | Area of the municipality of birth |
| born_code_adopted | int8 | Stores the code currently assigned to the municipality of birth, handling cases in which multiple codes have been used for the same municipality over time |
| res_MUNNOME | text | Name of municipality of residence |
| res_MUNNOMEX | text | Name of municipality of residence in capital letters and without accents |
| res_AMAZONIA | text | Indicates (Y/N) if the municipality of residence is part of the Legal Amazon (according to IBGE) |
| res_BORDER | text | Indicates (Y/N) if the municipality of residence is part of the border strip (according to IBGE) |
| res_CAPITAL | text | Indicates (Y/N) if the municipality of residence is the capital of UF |
| res_MSAUDCOD | int8 | Macroregional Health Code to which the municipality of residence belongs |
| res_RSAUDCOD | int8 | Regional Health Code to which the municipality of residence belongs |
| res_CSAUDCOD | int8 | Health Microregional Code to which the municipality of residence belongs |
| res_LATITUDE | float8 | Latitude of county of residence |
| res_LONGITUDE | float8 | Longitude of county of residence |
| res_ALTITUDE | int8 | Altitude of the municipality of residence |
| res_AREA | float8 | Area of the municipality of residence |
| res_code_adopted | int8 | Stores the code currently assigned to the municipality of residence, handling cases in which multiple codes have been used for the same municipality over time |
| born_SIGLA_UF | text | Acronym of Federation Unit of Birth |
| born_CODIGO_UF | int8 | State of birth code |
| born_NAME_UF | text | Federation Unit Name of Birth |
| res_SIGLA_UF | text | Acronym of federation unit of residence |
| res_CODIGO_UF | int8 | State of residence code |
| res_NAME_UF | text | Name of federation unit of residence |
| born_REGION | text | Region Name of State of Birth |
| res_REGION | text | Region Name of State of Residence |
| codename_chapter | text | Chapter ICD-10 Congenital Malformation or Chromosomal Abnormality |
| codename_group | text | ICD-10 group of congenital malformation or chromosomal abnormality |
| codename_category | text | ICD-10 Category of Congenital Malformation or Chromosomal Abnormality |
| codename_subcategory | text | Congenital Malformation or Chromosomal Abnormality ICD-10 Subcategory |
| birth_coordinates | text | Coordinates of the municipality of birth |
| res_coordinates | text | Coordinates of the municipality of residence |
| premature_birth | int8 | indicates prematurity of birth. 0: no signs of prematurity; 1: there is evidence of prematurity given by the gestational age (GESTATION<=4); 2: there is evidence of prematurity given by birth weight (WEIGHT<2500); 3: Gestational age and birth weight indicate prematurity |
| def_premature_birth | text | Indicates prematurity of birth. Term: there is no evidence of prematurity; Inconclusive-GA: there is evidence of prematurity given by gestational age (GESTATION<=4); Inconclusive-Weight: there is evidence of prematurity given by birth weight (WEIGHT<2500); Premature: Gestational Age and Birth Weight Indicate Prematurity |

**Autor**: Plataforma de Ciência de Dados Aplicada à Saúde
**Mantenedor**: Time de Governança e Engenharia de Dados
**Última Atualização**: 17 de Maio de 2022
**Criado**: 22 de Novembro de 2018
**Agregação**: Individual (Declarações de Nascido Vivo)
**Cobertura temporal**: 1996 a 2020
**Frequência de atualização**: Anual

**Author**: Data Science Platform Applied to Health
**Maintainer**: Governance and Data Engineering Team
**Last Update**: May 17, 2022
**Created**: November 22, 2018
**Aggregation**: Individual (Live Birth Certificates)
**Time coverage**: 1996 to 2020
**Update frequency**: Annual