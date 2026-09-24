# 🧠 Miniguia de Estudos com NotebookLM — Inteligência Artificial Generativa: Fundamentos e Aplicações

Repositório criado para o desafio de projeto da **DIO**: uso do NotebookLM como ferramenta de aprendizagem ativa, aliando curadoria de fontes, engenharia de prompts e organização do conhecimento.

---

## 🎯 Contexto e Objetivos

**Assunto escolhido:** Inteligência Artificial Generativa — conceitos fundamentais, funcionamento e aplicações práticas.

Escolhi esse tema porque a IA generativa se tornou uma ferramenta central no dia a dia de quem trabalha com tecnologia, e eu sentia que dominava o "uso" das ferramentas (prompts, chats, etc.) sem entender profundamente os **fundamentos técnicos** por trás delas — como modelos de linguagem são treinados, o que são tokens e embeddings, e quais são os limites reais dessa tecnologia.

**Objetivos de estudo:**

1. Compreender, em nível conceitual, como funcionam modelos de IA generativa (redes neurais, treinamento, inferência).
2. Diferenciar IA, Machine Learning, Deep Learning e IA Generativa — termos frequentemente confundidos.
3. Identificar aplicações práticas e limitações éticas/técnicas da IA generativa no mercado de trabalho.
4. Construir um material de revisão rápida (glossário + resumos + prompts) para consultas futuras.

---

## 📚 Curadoria de Fontes

Fontes abertas selecionadas e carregadas no NotebookLM (texto/PDF), priorizando material didático e de referência confiável:

| # | Fonte | Tipo | Link |
|---|-------|------|------|
| 1 | Wikipédia — Inteligência Artificial | Texto (artigo) | https://pt.wikipedia.org/wiki/Inteligência_artificial |
| 2 | Wikipédia — Aprendizado de máquina | Texto (artigo) | https://pt.wikipedia.org/wiki/Aprendizado_de_máquina |
| 3 | IBM — What is Artificial Intelligence (AI)? | Texto (artigo técnico) | https://www.ibm.com/topics/artificial-intelligence |
| 4 | Google — Machine Learning Crash Course (Introdução) | Texto (curso aberto) | https://developers.google.com/machine-learning/crash-course |
| 5 | Stanford CS229 — Lecture Notes (Introdução ao ML) | PDF (material acadêmico aberto) | https://cs229.stanford.edu/main_notes.pdf |

> 💡 Critério de seleção: priorizei fontes de instituições reconhecidas (Stanford, Google, IBM) e uma enciclopédia colaborativa para ter uma visão de "consenso geral", evitando blogs sem curadoria editorial.

---

## 🧪 Engenharia de Prompts e "Cicatrizes"

Documentação do processo de testes de prompts no NotebookLM — o que funcionou, o que não funcionou, e os ajustes feitos.

### Prompt 1 (versão inicial — genérico demais)
**Prompt:** `"Explique inteligência artificial."`

**Resultado:** Resposta correta, porém muito genérica — misturou definições de IA, ML e Deep Learning em um único parágrafo, sem distinguir claramente os conceitos.

**Problema identificado:** Prompt aberto demais não guia o modelo a estruturar a resposta.

---

### Prompt 2 (refinado — pedindo estrutura)
**Prompt:** `"Com base nas fontes carregadas, compare IA, Machine Learning, Deep Learning e IA Generativa em formato de tabela, destacando a relação hierárquica entre eles."`

**Resultado:** ✅ Resposta muito mais útil — o NotebookLM gerou uma tabela clara mostrando que IA Generativa é um subconjunto de Deep Learning, que por sua vez é um subconjunto de Machine Learning, que é um subconjunto de IA.

**Referência citada pela IA:** artigo da IBM e o verbete da Wikipédia sobre Aprendizado de Máquina.

**Aprendizado:** Pedir formato de saída (tabela, lista, comparação) aumenta muito a qualidade e a utilidade da resposta.

---

### Prompt 3 (troubleshooting — resposta incompleta)
**Prompt:** `"Quais são as limitações técnicas dos modelos de IA generativa?"`

**Resultado:** A primeira resposta trouxe apenas limitações genéricas ("pode errar", "precisa de dados"), sem profundidade técnica.

**Dificuldade encontrada:** As fontes carregadas tratavam pouco desse tema específico (limitações), então o modelo "forçou" uma resposta rasa com base em conhecimento geral, e não nas fontes.

**Ajuste feito:** Adicionei explicitamente a instrução de citar a fonte:
`"Quais são as limitações técnicas dos modelos de IA generativa? Cite explicitamente de qual fonte você tirou cada limitação e, se uma informação não estiver nas fontes, avise."`

**Resultado após o ajuste:** O NotebookLM passou a indicar claramente quando uma informação não vinha das fontes carregadas, o que aumentou a confiabilidade da resposta e evitou "alucinação silenciosa".

**Aprendizado principal (cicatriz):** Sempre pedir citação de fonte explicitamente quando o objetivo é rigor — o NotebookLM tende a complementar com conhecimento geral se não for instruído a se limitar ao material carregado.

---

### Prompt 4 (extração de dados reais para o projeto Python — bootcamp Accenture)
**Prompt:** Prompt estruturado pedindo dados reais das fontes carregadas, com regra explícita de citar a fonte de cada item, avisar quando algo não fosse encontrado, e gerar a saída já em formato de lista de dicionários Python (não apenas texto).

**Resultado:** ✅ Excelente — o NotebookLM retornou uma tabela markdown completa (10 termos de glossário, hierarquia IA → ML → DL → IA Generativa, 5 aplicações práticas e 3 limitações técnicas), **todas com fonte citada** (principalmente *"What Is Artificial Intelligence (AI)? | IBM"* e a Wikipédia), além de um bloco de código Python já estruturado em listas de dicionários, pronto para uso no projeto.

**Referências citadas pela IA:** artigo da IBM (fonte majoritária) e o verbete da Wikipédia sobre Inteligência Artificial (para as aplicações de recomendação de conteúdo e a limitação de alucinações).

**Observação:** diferente do Prompt 3, aqui **nenhuma informação ficou sem fonte** — todos os 4 pedidos foram atendidos com base real nas fontes carregadas, sem necessidade de complementar com conhecimento geral. Isso confirma que a instrução explícita de citação (aprendizado do Prompt 3) funciona de forma consistente quando reaplicada.

**Entrega gerada:** os dados foram salvos no arquivo [`dados_ia_generativa.py`](./dados_ia_generativa.py), consumido diretamente pelo projeto Python do bootcamp da Accenture.

---

## 📘 Miniguia de Estudo (Entrega Final)

### 🔹 Resumo Estruturado

**1. O que é Inteligência Artificial (IA)?**
Campo da ciência da computação dedicado a criar sistemas capazes de realizar tarefas que normalmente exigiriam inteligência humana, como reconhecimento de padrões, tomada de decisão e compreensão de linguagem.

**2. Hierarquia dos conceitos**
- **IA** → área geral.
- **Machine Learning (ML)** → subárea da IA em que sistemas aprendem padrões a partir de dados, em vez de seguir regras programadas manualmente.
- **Deep Learning (DL)** → subárea do ML baseada em redes neurais artificiais com múltiplas camadas, capaz de aprender representações complexas.
- **IA Generativa** → subárea do Deep Learning voltada para a criação de novos conteúdos (texto, imagem, áudio) a partir de padrões aprendidos.

**3. Como um modelo de linguagem aprende**
O modelo é treinado em grandes volumes de texto, ajustando bilhões de parâmetros internos para prever a próxima palavra (token) mais provável em uma sequência. Esse processo é chamado de **treinamento por previsão de próximo token**.

**4. Aplicações práticas**
Assistentes conversacionais, geração de código, resumo automático de documentos, tradução, geração de imagens e apoio à pesquisa (como o próprio NotebookLM).

**5. Limitações**
Modelos podem gerar informações incorretas com confiança ("alucinação"), refletir vieses presentes nos dados de treinamento, e têm um limite de conhecimento definido pela data de corte do treinamento.

---

### 🔹 Glossário

*(Dados extraídos e validados diretamente das fontes via NotebookLM — ver Prompt 4. Disponível também em formato Python em [`dados_ia_generativa.py`](./dados_ia_generativa.py).)*

| Termo | Definição | Fonte |
|-------|-----------|-------|
| **IA Generativa (Generative AI)** | Modelos de deep learning capazes de criar conteúdos originais como texto longo, imagens de alta qualidade, vídeo ou áudio em resposta a um prompt. | IBM |
| **Large Language Model (LLM)** | Modelo de base criado para aplicações de geração de texto, treinado em imensas quantidades de dados brutos e não estruturados. | IBM |
| **Transformer** | Arquitetura treinada em dados sequenciais para gerar sequências estendidas de conteúdo; está no núcleo das principais ferramentas generativas. | IBM |
| **Modelo de Difusão (Diffusion Model)** | Modelo que adiciona ruído a imagens até ficarem irreconhecíveis e depois remove o ruído para gerar imagens originais. | IBM |
| **Variational Autoencoder (VAE)** | Modelo de deep learning usado para gerar múltiplas variações de conteúdo em resposta a uma instrução. | IBM |
| **Modelo de Base (Foundation Model)** | Modelo amplo treinado em volumes massivos de dados não rotulados, usado como alicerce para aplicações generativas. | IBM |
| **Retrieval-Augmented Generation (RAG)** | Técnica que estende o modelo de base usando fontes externas relevantes para gerar respostas mais precisas. | IBM |
| **Fine-Tuning (Ajuste Fino)** | Adaptação do modelo com dados rotulados e pares de perguntas/respostas específicos da aplicação desejada. | IBM |
| **RLHF** | Aprendizado por reforço com feedback humano, usado para aprimorar a precisão e relevância das respostas do modelo. | IBM |
| **Prompt** | Requisição ou instrução em texto enviada ao modelo, à qual ele responde gerando um novo conteúdo. | IBM |

---

### 🔹 Prompts Reutilizáveis para Revisão Futura

Conjunto de prompts testados e validados, prontos para reutilização em futuras sessões de estudo no NotebookLM (ou qualquer IA baseada em fontes):

1. `"Com base nas fontes carregadas, resuma o tema [X] em até 5 bullet points, do mais básico ao mais avançado."`
2. `"Crie uma tabela comparando [conceito A] e [conceito B], citando a fonte de cada informação."`
3. `"Gere 5 perguntas de múltipla escolha sobre o conteúdo das fontes, para eu testar meu entendimento sobre [tema]."`
4. `"Quais pontos das fontes carregadas ainda não ficaram claros ou parecem contraditórios entre si?"`
5. `"Explique [conceito] como se eu fosse iniciante, e depois explique novamente em nível técnico avançado, citando as fontes usadas em cada versão."`
6. `"Liste os termos técnicos mais importantes sobre [tema] presentes nas fontes, com definição de uma frase cada, para eu montar um glossário."`
7. `"Se alguma informação da sua resposta não estiver presente nas fontes carregadas, avise explicitamente."` *(usar sempre como complemento de outros prompts, para evitar alucinação)*

---

## ✅ Como usar este repositório

1. Leia o **Contexto e Objetivos** para entender o escopo do estudo.
2. Acesse as fontes listadas na **Curadoria de Fontes** e, se quiser, carregue-as você mesmo no [NotebookLM](https://notebooklm.google.com/).
3. Use os **prompts documentados** como ponto de partida para suas próprias sessões de estudo.
4. Consulte o **Miniguia de Estudo** sempre que precisar revisar o tema rapidamente.

---

*Projeto desenvolvido como parte do desafio "Caderno Temático no NotebookLM" da [DIO](https://www.dio.me/).*
