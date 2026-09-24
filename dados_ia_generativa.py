"""
Dados extraídos EXCLUSIVAMENTE das fontes carregadas no NotebookLM
(IBM - What Is Artificial Intelligence (AI)? | Wikipédia - Inteligência Artificial)

Uso: dados estruturados para o projeto de Python com IA do bootcamp da Accenture.
Gerado via prompt de extração controlada (ver README.md -> Engenharia de Prompts).
"""

glossario_ia_generativa = [
    {
        "termo": "IA Generativa (Generative AI)",
        "definicao": "Modelos de deep learning capazes de criar conteúdos originais como texto longo, imagens de alta qualidade, vídeo ou áudio em resposta a um prompt.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Large Language Model (LLM)",
        "definicao": "Modelo de base criado para aplicações de geração de texto treinado em imensas quantidades de dados brutos e não estruturados.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Transformer",
        "definicao": "Arquitetura treinada em dados sequenciais para gerar sequências estendidas de conteúdo, estando no núcleo das principais ferramentas generativas.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Modelo de Difusão (Diffusion Model)",
        "definicao": "Modelo que adiciona ruído a imagens até ficarem irreconhecíveis e depois remove o ruído para gerar imagens originais em resposta a prompts.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Variational Autoencoder (VAE)",
        "definicao": "Modelo de deep learning introduzido para gerar múltiplas variações de conteúdo em resposta a uma instrução ou comando.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Modelo de Base (Foundation Model)",
        "definicao": "Modelo amplo treinado em volumes massivos de dados não rotulados que serve como alicerce para diversos tipos de aplicações generativas.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Retrieval-Augmented Generation (RAG)",
        "definicao": "Técnica que estende o modelo de base utilizando fontes externas relevantes para refinar os parâmetros e gerar respostas mais precisas.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Fine-Tuning (Ajuste Fino)",
        "definicao": "Processo de adaptação do modelo alimentando-o com dados rotulados e pares de perguntas/respostas específicos da aplicação desejada.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Reinforcement Learning with Human Feedback (RLHF)",
        "definicao": "Método de ajuste onde avaliações humanas sobre as respostas do modelo ajudam a aprimorar sua precisão e relevância.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "termo": "Prompt",
        "definicao": "Requisição ou instrução em texto enviada pelo usuário à qual o modelo generativo responde gerando um novo conteúdo.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    }
]

hierarquia_conceitos = [
    {
        "nivel": 1,
        "conceito": "Inteligência Artificial (IA)",
        "descricao": "Tecnologia que possibilita computadores simularem aprendizado, compreensão e tomada de decisão humana.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "nivel": 2,
        "conceito": "Machine Learning (ML)",
        "descricao": "Subcampo da IA focado no treinamento de algoritmos para fazer previsões com base em dados.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "nivel": 3,
        "conceito": "Deep Learning (DL)",
        "descricao": "Subconjunto do ML que utiliza redes neurais profundas com múltiplas camadas ocultas.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "nivel": 4,
        "conceito": "IA Generativa (Gen AI)",
        "descricao": "Modelos de Deep Learning capazes de criar conteúdos originais complexos em resposta a solicitações.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    }
]

aplicacoes_praticas = [
    {
        "aplicacao": "Desenvolvimento e Modernização de Software",
        "descricao": "Geração automatizada de código de programação e aceleração da migração de sistemas legados.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "aplicacao": "Atendimento e Experiência do Cliente",
        "descricao": "Chatbots e assistentes virtuais com IA generativa para responder a dúvidas e chamados de suporte.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "aplicacao": "Marketing Personalizado",
        "descricao": "Criação automatizada de textos publicitários e ofertas personalizadas para clientes em tempo real.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "aplicacao": "Criação de Arte e Mídia Visual",
        "descricao": "Geração de imagens de alta qualidade, arte digital e vídeos a partir de prompts de texto.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "aplicacao": "Sistemas de Recomendação de Conteúdo",
        "descricao": "Uso de IA generativa para recomendar filmes e conteúdos em plataformas de streaming como a Netflix.",
        "fonte": "Inteligência artificial – Wikipédia, a enciclopédia livre"
    }
]

limitacoes_tecnicas = [
    {
        "limitacao": "Alucinações",
        "descricao": "Modelos de linguagem probabilísticos produzem respostas incorretas ou fatos falsos.",
        "fonte": "Inteligência artificial – Wikipédia, a enciclopédia livre"
    },
    {
        "limitacao": "Alto Custo Computacional e Financeiro",
        "descricao": "Treinar modelos de base exige milhares de GPUs clusterizadas e investimentos de milhões de dólares.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    },
    {
        "limitacao": "Viés nos Dados e Desvio do Modelo (Model Drift)",
        "descricao": "Vulnerabilidade a dados de treinamento enviesados e perda de desempenho ao longo do tempo.",
        "fonte": "What Is Artificial Intelligence (AI)? | IBM"
    }
]


if __name__ == "__main__":
    # Teste rápido: exibe todos os termos do glossário
    print("=== Glossário de IA Generativa ===\n")
    for item in glossario_ia_generativa:
        print(f"- {item['termo']}: {item['definicao']} (Fonte: {item['fonte']})")

    print("\n=== Hierarquia de Conceitos ===\n")
    for item in hierarquia_conceitos:
        print(f"Nível {item['nivel']}: {item['conceito']} - {item['descricao']}")
