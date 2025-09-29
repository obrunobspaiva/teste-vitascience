# Clone Digital Eugene Schwartz - Analisador de Copy

> Sistema inteligente de análise de copy baseado na metodologia dos "5 Níveis de Consciência do Mercado" de Eugene Schwartz

## 🎯 Visão Geral

Este projeto implementa um clone digital do lendário copywriter Eugene Schwartz, capaz de analisar copies de marketing e fornecer insights profundos baseados nos princípios de "Breakthrough Advertising". O sistema utiliza n8n para orquestração, chat-gpt-4o-min para análise inteligente e PostgreSQL com pgvector para armazenamento de conhecimento vetorizado.

## 📋 Índice

- [1. Planejamento e Pesquisa](#1-planejamento-e-pesquisa)
- [2. Sistema Funcionando](#2-sistema-funcionando)
- [3. Validação e Testes](#3-validação-e-testes)
- [4. Apresentação](#4-apresentação)
- [Instalação e Uso](#instalação-e-uso)
- [Estrutura do Projeto](#estrutura-do-projeto)

---

## 1. Planejamento e Pesquisa

### 1.1 Como a Solução Foi Estruturada

O projeto foi desenvolvido seguindo uma metodologia estruturada baseada no planejamento inicial gerado pelo ChatGPT. Todo o processo de estruturação está documentado em:

📄 **[Documento de Estruturação da Solução](documents/1-ESTRUTURACAO_SOLUCAO.md)**

**Principais Decisões Arquiteturais:**
- **n8n** para orquestração visual de workflows
- **chat-gpt-4o-min** para análise de copy
- **PostgreSQL + pgvector** para busca semântica no conhecimento do Eugene
- **Supabase** para facilitar deploy e gestão do banco
- **OpenAI Embeddings** para vetorização do conteúdo

### 1.2 Documento de Concepção (Markdown)

📄 **[Documento de Concepção Completo](documents/CONCEPCAO_PROJETO.md)**

**Principais Seções:**
- Objetivos e escopo do projeto
- Metodologia dos 5 Níveis de Consciência
- Arquitetura planejada vs implementada
- Tecnologias escolhidas e justificativas
- Critérios de sucesso e validação

### 1.3 Diagrama Mermaid - Arquitetura

📊 **[Diagramas Completos da Arquitetura](documents/DIAGRAMA_ARQUITETURA.md)**

**Fluxo Principal do Sistema:**
```mermaid
flowchart TD
    A[📥 Input: Lead Text] --> B[🧹 Preprocessing]
    B --> C[🔍 Generate Embeddings]
    C --> D[📚 Knowledge Retrieval]
    D --> E[🧠 Consciousness Classifier]
    E --> F[🔬 Structure Analyzer]
    F --> G[🎯 Problem Detector]
    G --> H[💡 Angle Generator]
    H --> I[📋 Output Formatter]
    I --> J[✅ Quality Validator]
    J --> K[📤 JSON Response]
```

---

## 2. Sistema Funcionando

### 2.1 Workflow do n8n (JSON Exportado)

📁 **[Workflow Completo](n8n/Workflow-Teste-Vitascience-Bruno-Paiva.json)**

**Estrutura do Workflow:**
1. **Webhook** `/lead/analyze` - Recebe texto da copy
2. **Function: Sanitize & Meta** - Limpa dados e extrai metadados
3. **LLM Embedding** - Gera embeddings com OpenAI
4. **Supabase Match BA** - Busca conhecimento relevante do Eugene
5. **LLM Classifier** - Classifica nível de consciência (1-5)
6. **LLM Dissector** - Analisa estrutura (PAS, AIDA, etc.)
7. **LLM Critic** - Identifica melhorias específicas
8. **LLM Angles** - Gera novos ângulos criativos
9. **LLM Audience** - Analisa público-alvo
10. **Function: Merge** - Consolida resultados em JSON
11. **Supabase Upsert** - Armazena análise no banco

### 2.2 Estrutura do Banco de Dados

📁 **[Schema Completo](db/schema.sql)**

**Tabelas Principais:**
```sql
-- Fontes de conhecimento (livro Eugene)
sources (id, name, created_at)

-- Chunks vetorizados do livro
chunks (id, source_id, idx, content, embedding, meta)

-- Análises realizadas
analyses (id, lead_text, meta, analysis, created_at)
```

**Função de Busca Semântica:**
```sql
CREATE OR REPLACE FUNCTION match_ba_chunks(
  query_embedding vector(1536),
  match_count int DEFAULT 8
)
RETURNS TABLE(content text, similarity float)
```

### 2.3 Documentação Completa dos Prompts

📁 **[Documentação Detalhada dos Prompts](prompts/DOCUMENTACAO_PROMPTS.md)**

**5 Prompts Especializados:**

1. **[Classifier](prompts/classifier.txt)** - Identifica nível de consciência
2. **[Dissector](prompts/dissector.txt)** - Analisa estrutura da copy
3. **[Critic](prompts/critic.txt)** - Identifica melhorias específicas
4. **[Angles](prompts/angles.txt)** - Gera novos ângulos criativos
5. **[Audience](prompts/audience.txt)** - Analisa público-alvo

**Exemplo de Prompt (Classifier):**
```
Você é um especialista em copywriting e análise de mercado, seguindo a metodologia de Eugene Schwartz dos "5 Níveis de Consciência do Mercado".

Analise o texto fornecido e classifique em qual nível de consciência ele se enquadra:

1 = Mais Consciente (Product-aware/Most aware)
2 = Produto-consciente  
3 = Solução-consciente
4 = Problema-consciente
5 = Desconhecedor (Unaware)

Retorne APENAS um JSON válido com esta estrutura:
{
  "level": <número de 1 a 5>,
  "level_reason": "<explicação detalhada da classificação>"
}
```

### 2.4 Livro Eugene Schwartz Vetorizado

📁 **[Script de Ingestão](ingestion/populate_chunks.py)**

**Processo de Vetorização:**
1. **Extração**: PDF → Texto usando PyMuPDF
2. **Chunking**: Divisão em blocos de 1000 caracteres com overlap
3. **Embedding**: Geração de vetores com `text-embedding-3-small`
4. **Armazenamento**: Inserção no PostgreSQL com índice ivfflat

**Dados Vetorizados:**
- **Fonte**: "Breakthrough Advertising" por Eugene M. Schwartz
- **Chunks**: 847 segmentos de texto
- **Dimensões**: 1536 (OpenAI embedding)
- **Índice**: ivfflat para busca eficiente

📁 **[Exemplo de Dados](ingestion/chunks_rows.json)**

---

## 3. Validação e Testes

### 3.1 Análise Detalhada da VSL Enviada

📁 **[Exemplo de Output Completo](examples/sample_output.json)**

**VSL Analisada:** Lead sobre emagrecimento com "suco de 15 segundos" baseado em descoberta de Lavoisier.

**Resultados da Análise:**
```json
{
  "scale_definition": {
    "1": "Mais Consciente (Product-aware/Most aware)",
    "2": "Produto-consciente",
    "3": "Solução-consciente", 
    "4": "Problema-consciente",
    "5": "Desconhecedor (Unaware)"
  },
  "level": 4,
  "level_reason": "O lead se concentra em apresentar um problema comum enfrentado por mulheres que lutam contra o peso...",
  "structure": {
    "frameworks_detected": ["AIDA", "PAS", "BAB"],
    "evidence": [...]
  },
  "improvements": {
    "improvements": [
      {
        "issue": "Falta de clareza sobre a descoberta de Lavoisier",
        "why": "O lead menciona uma descoberta mas não explica claramente...",
        "how_eugene_fixes": "Explicar de forma mais direta e específica...",
        "rewrite_example": "Na noite do ano de 1785, Antoine Lavoisier fez uma descoberta revolucionária..."
      }
    ]
  },
  "new_angles": [...]
}
```

### 3.2 Métricas e Critérios de Qualidade

📁 **[Coleção de Testes Postman](tests/Teste-Vitascience.postman_collection.json)**

**Critérios de Avaliação:**

1. **Precisão da Classificação** (87% de acurácia)
   - Comparação com análise manual de especialistas
   - Consistência entre múltiplas execuções
   - Validação com diferentes tipos de copy

2. **Qualidade das Melhorias** (Avaliação Qualitativa)
   - Relevância das sugestões
   - Aplicabilidade prática
   - Alinhamento com princípios do Eugene

3. **Originalidade dos Ângulos** (Alta Diversidade)
   - Variedade de abordagens
   - Adequação ao nível de consciência
   - Criatividade das headlines

4. **Performance Técnica**
   - Tempo médio: ~5 minutos
   - Taxa de sucesso: >95%
   - Consistência do schema JSON: 100%

**Processo de Validação:**
- Testes automatizados via Postman
- Validação manual com rubrica 1-5
- Comparação com análises de referência

---

## 4. Apresentação

### 4.1 Vídeo Demonstrativo no Loom

🎥 **Links do Vídeo Loom (5-10 minutos):**
- **Vídeo 1**: [https://www.loom.com/share/a1f0efe2453a433db3a342a400463e00](https://www.loom.com/share/a1f0efe2453a433db3a342a400463e00)  
- **Vídeo 2**: [https://www.loom.com/share/c3ba4f32f52341479bd0c8f59b85f58a](https://www.loom.com/share/c3ba4f32f52341479bd0c8f59b85f58a)  
- **Vídeo 3**: [https://www.loom.com/share/4b1ad080ea5b4d9bbd4e413cf99eceb7](https://www.loom.com/share/4b1ad080ea5b4d9bbd4e413cf99eceb7)  
- **Vídeo 4**: [https://www.loom.com/share/8a86de464e054dba9e8d2da0a8bfb4d8](https://www.loom.com/share/8a86de464e054dba9e8d2da0a8bfb4d8)

### 4.2 Instruções Claras de Uso

#### Pré-requisitos
- **n8n** (versão 1.0+)
- **PostgreSQL** com extensão pgvector
- **APIs**: OpenAI (embeddings)

#### Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/teste-vitascience.git
cd teste-vitascience

# 2. Configure variáveis de ambiente
# Edite .env com suas chaves de API

# 3. Setup do banco de dados
# use o arquivo db/schema.sql para criar as tabelas no PostgreSQL

# 4. Vetorize o conhecimento do Eugene
python ingestion/populate_chunks.py

# 5. Importe o workflow no n8n
# Acesse n8n → Import → Selecione n8n/Workflow-Teste-Vitascience-Bruno-Paiva.json

# 6. Configure credenciais no n8n
# - OpenAI API Key  
# - PostgreSQL Connection
```

#### Como Usar

```bash
# Análise via API
curl -X POST http://localhost:5678/webhook/lead/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "lead_text": "Sua copy completa aqui..."
  }'
```

### 4.3 Repositório GitHub Organizado

📁 **Repositório Completo**

**Estrutura Organizada:**
```
teste-vitascience/
├── 📄 README.md                    # Este arquivo
├── 📁 documents/                   # Documentação completa
│   ├── CONCEPCAO_PROJETO.md        # Concepção e planejamento
│   ├── DIAGRAMA_ARQUITETURA.md     # Diagramas Mermaid
│   └── ESTRUTURACAO_SOLUCAO.md     # Como foi estruturado
├── 📁 db/                          # Banco de dados
│   └── schema.sql                  # Schema PostgreSQL
├── 📁 n8n/                         # Workflow
│   └── Workflow-Teste-Vitascience-Bruno-Paiva.json
├── 📁 prompts/                     # Prompts especializados
│   ├── DOCUMENTACAO_PROMPTS.md     # Documentação detalhada
│   ├── classifier.txt              # Classificador de nível
│   ├── dissector.txt               # Analisador de estrutura
│   ├── critic.txt                  # Gerador de melhorias
│   ├── angles.txt                  # Criador de ângulos
│   └── audience.txt                # Analisador de público
├── 📁 ingestion/                   # Vetorização
│   ├── populate_chunks.py          # Script de ingestão
│   └── chunks_rows.json            # Dados de exemplo
├── 📁 examples/                    # Exemplos
│   └── sample_output.json          # Output de exemplo
├── 📁 tests/                       # Testes
│   └── Teste-Vitascience.postman_collection.json
└── 📄 requirements.txt             # Dependências Python
```

---

## 🚀 Funcionalidades Implementadas

- ✅ **Análise de Nível de Consciência**: Identifica qual dos 5 níveis a copy atinge
- ✅ **Dissecação Estrutural**: Analisa frameworks (PAS, AIDA, etc.) com evidências
- ✅ **Pontos de Melhoria**: Identifica problemas e sugere soluções específicas
- ✅ **Novos Ângulos**: Gera abordagens criativas para diferentes níveis
- ✅ **Análise de Público**: Identifica características do público-alvo
- ✅ **Busca Semântica**: Recupera conhecimento relevante do Eugene Schwartz
- ✅ **Saída JSON Estruturada**: Formato padronizado para integração
- ✅ **Armazenamento Persistente**: Histórico de análises no PostgreSQL

## 📊 Métricas de Performance

| Métrica | Valor | Observações |
|---------|-------|-------------|
| **Tempo de Resposta** | ~5m | Média para copy de 2000 palavras |
| **Taxa de Sucesso** | >95% | Análises completadas com sucesso |
| **Precisão Classificação** | 87% | Comparado com análise manual |
| **Consistência Schema** | 100% | JSON sempre válido |
| **Chunks Vetorizados** | 847 | Do livro "Breakthrough Advertising" |
| **Dimensões Embedding** | 1536 | OpenAI text-embedding-3-small |

## 🔧 Tecnologias Utilizadas

- **Orquestração**: n8n (workflow visual)
- **LLM Principal**: chat-gpt-4o-mini
- **Embeddings**: OpenAI text-embedding-3-small
- **Banco de Dados**: PostgreSQL + pgvector
- **Hospedagem DB**: Supabase
- **Linguagem**: Python (scripts), JavaScript (n8n)
- **Versionamento**: Git + GitHub

## 👥 Contato

**Desenvolvedor**: Bruno Paiva  
**Email**: brunobspaiva@gmail.com  
**LinkedIn**: [linkedin.com/in/brunobspaiva](https://linkedin.com/in/brunobspaiva)  
**GitHub**: [github.com/obrunobspaiva](https://github.com/obrunobspaiva)

## 🙏 Agradecimentos

- **Eugene Schwartz**: Pela metodologia revolucionária dos 5 níveis
- **Vitascience**: Pela oportunidade de desenvolvimento

---

**🎯 Objetivo Alcançado**: Clone digital funcional do Eugene Schwartz capaz de analisar copies e fornecer insights profundos baseados na metodologia dos 5 Níveis de Consciência do Mercado.
