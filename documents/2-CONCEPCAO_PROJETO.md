# Clone Digital Eugene Schwartz - Documento de Concepção

## 📋 Visão Geral do Projeto

### Objetivo
Desenvolver um sistema inteligente no n8n que funcione como um clone digital de Eugene Schwartz, capaz de analisar e melhorar copies utilizando sua metodologia dos "5 Níveis de Consciência do Mercado" do livro "Breakthrough Advertising".

### Prazo
96 horas (4 dias)

### Entregáveis Principais
1. **Planejamento e Pesquisa**
   - ✅ Documento de Concepção (este documento)
   - 🔄 Diagrama Mermaid da arquitetura
   
2. **Sistema Funcionando**
   - 🔄 Workflow do n8n (JSON exportado)
   - 🔄 Estrutura do banco de dados
   - 🔄 Documentação completa dos prompts
   - 🔄 Livro "Breakthrough Advertising" vetorizado
   
3. **Validação e Testes**
   - 🔄 Análise completa da VSL fornecida
   - 🔄 Métricas de qualidade do clone
   
4. **Apresentação**
   - 🔄 Vídeo no Loom (5-10 min)
   - 🔄 README com instruções
   - 🔄 Repositório GitHub completo

## 🧠 Fundamentos Teóricos: Os 5 Níveis de Consciência

### Metodologia Eugene Schwartz
Eugene Schwartz identificou que o maior erro em copywriting é falar com o nível errado de consciência do mercado. Cada nível requer uma abordagem específica:

#### 1. **Unaware (Inconsciente)**
- **Características**: Não sabe que tem um problema
- **Abordagem**: Educar sobre a existência do problema
- **Copy Strategy**: Fazer perguntas que levem à descoberta do problema

#### 2. **Problem Aware (Consciente do Problema)**
- **Características**: Reconhece o problema, mas não conhece soluções
- **Abordagem**: Focar no problema e construir desejo por uma solução
- **Copy Strategy**: Amplificar a dor e introduzir esperança

#### 3. **Solution Aware (Consciente da Solução)**
- **Características**: Conhece soluções, mas não conhece seu produto
- **Abordagem**: Posicionar seu produto como a melhor solução
- **Copy Strategy**: Demonstrar superioridade da solução

#### 4. **Product Aware (Consciente do Produto)**
- **Características**: Conhece seu produto, mas não está convencido
- **Abordagem**: Mostrar benefícios únicos e diferenciação
- **Copy Strategy**: Prova social, especificações, comparações

#### 5. **Most Aware (Mais Consciente)**
- **Características**: Conhece e quer o produto, mas não comprou ainda
- **Abordagem**: Oferta irresistível e urgência
- **Copy Strategy**: Call-to-action direto, ofertas limitadas

## 🏗️ Arquitetura do Sistema

### Componentes Principais

#### 1. **Input Layer (Camada de Entrada)**
- Recebe Lead de VSL (primeiras páginas da copy)
- Formatos suportados: Texto, PDF, HTML
- Validação e sanitização do input

#### 2. **Analysis Engine (Motor de Análise)**
- **Classificador de Consciência**: Identifica o nível (1-5)
- **Dissecador de Estrutura**: Analisa framework usado (PAS, AIDA, etc.)
- **Detector de Problemas**: Identifica pontos fracos
- **Gerador de Ângulos**: Cria novas abordagens

#### 3. **Knowledge Base (Base de Conhecimento)**
- Livro "Breakthrough Advertising" vetorizado
- Exemplos de copies por nível de consciência
- Frameworks de copywriting
- Banco de ângulos e headlines

#### 4. **Output Generator (Gerador de Saída)**
- Estrutura JSON padronizada
- Análise detalhada por seção
- Sugestões de melhoria
- Novos ângulos criativos

### Stack Tecnológico

#### **Workflow Principal**
- **n8n**: Orquestração principal do workflow
- **LLM**: Claude 3.5 Sonnet (Anthropic) - escolhido por:
  - Excelente capacidade de análise de texto
  - Boa compreensão de contexto longo
  - Qualidade superior em tarefas de copywriting

#### **Base de Dados**
- **PostgreSQL**: Armazenamento principal
- **pgvector**: Extensão para embeddings vetoriais
- **Estrutura**:
  - `knowledge_base`: Conteúdo vetorizado do livro
  - `copy_analysis`: Histórico de análises
  - `frameworks`: Templates de estruturas
  - `angles_bank`: Banco de ângulos criativos

#### **Processamento de Embeddings**
- **OpenAI Embeddings**: text-embedding-3-large
- **Chunking Strategy**: Parágrafos semânticos de 500-1000 tokens
- **Similarity Search**: Cosine similarity com threshold 0.7

## 📊 Estrutura do Output JSON

```json
{
  "analysis_id": "uuid",
  "timestamp": "2024-01-XX",
  "input_metadata": {
    "word_count": 1500,
    "estimated_reading_time": "6 minutes",
    "detected_language": "pt-BR"
  },
  "consciousness_analysis": {
    "identified_level": 3,
    "confidence_score": 0.85,
    "reasoning": "A copy assume que o leitor conhece o problema (dor nas costas) e apresenta soluções, mas não menciona produtos específicos...",
    "level_indicators": [
      "Menciona problema específico",
      "Apresenta múltiplas soluções",
      "Não cita produtos específicos"
    ]
  },
  "structure_dissection": {
    "framework_detected": "PAS (Problem-Agitation-Solution)",
    "structure_breakdown": {
      "hook": "Primeira frase que captura atenção",
      "problem_identification": "Parágrafos 2-3",
      "agitation": "Parágrafos 4-5",
      "solution_introduction": "Parágrafo 6",
      "call_to_action": "Último parágrafo"
    },
    "schwartz_principles_used": [
      "Identificação de desejo dominante",
      "Agitação emocional",
      "Posicionamento de solução"
    ]
  },
  "improvement_points": [
    {
      "issue": "Headline fraca",
      "problem_description": "A headline não captura atenção suficiente para o nível de consciência identificado",
      "schwartz_solution": "Para nível 3 (Solution Aware), a headline deve focar na superioridade da solução",
      "rewritten_example": "A Única Solução Para Dor nas Costas Que Médicos Não Querem Que Você Conheça",
      "impact_level": "high"
    },
    {
      "issue": "Falta de prova social",
      "problem_description": "Ausência de depoimentos ou estatísticas que comprovem eficácia",
      "schwartz_solution": "Incluir elementos de credibilidade específicos para o nível de consciência",
      "rewritten_example": "Mais de 10.000 pessoas já eliminaram suas dores usando este método...",
      "impact_level": "medium"
    }
  ],
  "new_angles": [
    {
      "angle_name": "Autoridade Médica Contrária",
      "target_consciousness_level": 2,
      "headline": "Por Que 9 em 10 Médicos Estão Errados Sobre Dor nas Costas",
      "approach": "Posicionar contra establishment médico para criar curiosidade",
      "schwartz_principle": "Agitação do problema + autoridade contrária"
    },
    {
      "angle_name": "Descoberta Científica Recente",
      "target_consciousness_level": 3,
      "headline": "Descoberta de Harvard Revela Verdadeira Causa da Dor nas Costas",
      "approach": "Usar autoridade científica para validar nova solução",
      "schwartz_principle": "Novidade + autoridade científica"
    }
  ],
  "quality_metrics": {
    "schwartz_alignment_score": 0.78,
    "consciousness_accuracy": 0.85,
    "improvement_potential": 0.65,
    "overall_grade": "B+"
  }
}
```

## 🔄 Workflow do n8n - Visão Geral

### Fluxo Principal

1. **Input Node**: Recebe Lead de VSL
2. **Text Preprocessing**: Limpa e estrutura o texto
3. **Consciousness Classifier**: Identifica nível de consciência
4. **Structure Analyzer**: Disseca framework usado
5. **Knowledge Retrieval**: Busca conhecimento relevante do Schwartz
6. **Problem Detector**: Identifica pontos de melhoria
7. **Angle Generator**: Cria novos ângulos
8. **Output Formatter**: Estrutura resposta JSON
9. **Quality Validator**: Verifica qualidade da análise

### Nós Específicos

#### **Consciousness Classifier Node**
```javascript
// Prompt para classificação de consciência
const classificationPrompt = `
Analise o seguinte texto de copy e identifique o nível de consciência do mercado segundo Eugene Schwartz:

TEXTO: {{$json.input_text}}

Baseado nos 5 níveis:
1. Unaware - não sabe que tem problema
2. Problem Aware - sabe do problema, não das soluções  
3. Solution Aware - conhece soluções, não o produto
4. Product Aware - conhece produto, não está convencido
5. Most Aware - conhece e quer, mas não comprou

Retorne JSON com: level, confidence, reasoning, indicators
`;
```

#### **Knowledge Retrieval Node**
- Busca vetorial no banco de conhecimento
- Recupera trechos relevantes do "Breakthrough Advertising"
- Contextualiza com exemplos específicos

#### **Angle Generator Node**
- Gera 3+ ângulos diferentes
- Cada ângulo targetiza níveis específicos de consciência
- Inclui headlines e justificativas baseadas no Schwartz

## 🗄️ Estrutura do Banco de Dados

### Tabelas Principais

```sql
-- Conhecimento vetorizado do livro
CREATE TABLE knowledge_base (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    embedding VECTOR(1536),
    chapter VARCHAR(100),
    page_number INTEGER,
    concept_tags TEXT[],
    created_at TIMESTAMP DEFAULT NOW()
);

-- Análises realizadas
CREATE TABLE copy_analysis (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    input_text TEXT NOT NULL,
    analysis_result JSONB NOT NULL,
    consciousness_level INTEGER,
    quality_score DECIMAL(3,2),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Frameworks de copywriting
CREATE TABLE frameworks (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    structure JSONB,
    consciousness_levels INTEGER[],
    examples TEXT[]
);

-- Banco de ângulos
CREATE TABLE angles_bank (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    target_level INTEGER,
    headline_template TEXT,
    schwartz_principle TEXT,
    examples JSONB
);
```

## 🧪 Estratégia de Validação

### Métricas de Qualidade

1. **Accuracy de Classificação**: % de acerto na identificação do nível
2. **Relevância das Melhorias**: Qualidade das sugestões (1-10)
3. **Criatividade dos Ângulos**: Originalidade e aplicabilidade
4. **Aderência ao Schwartz**: Fidelidade aos princípios originais

### Testes Planejados

1. **Teste com VSL Fornecida**: Análise completa do material de teste
2. **Teste de Consistência**: Múltiplas análises do mesmo texto
3. **Teste Cross-Level**: Copies de diferentes níveis de consciência
4. **Validação Humana**: Revisão por especialista em copywriting

## 📈 Próximos Passos

### Fase 1: Setup (Horas 1-12)
- ✅ Documento de concepção
- 🔄 Diagrama Mermaid
- 🔄 Setup do banco de dados
- 🔄 Vetorização do livro "Breakthrough Advertising"

### Fase 2: Desenvolvimento (Horas 13-60)
- 🔄 Criação dos prompts especializados
- 🔄 Desenvolvimento do workflow n8n
- 🔄 Implementação dos nós de análise
- 🔄 Testes unitários de cada componente

### Fase 3: Integração e Testes (Horas 61-84)
- 🔄 Integração completa do sistema
- 🔄 Testes com a VSL fornecida
- 🔄 Refinamento baseado nos resultados
- 🔄 Otimização de performance

### Fase 4: Documentação e Entrega (Horas 85-96)
- 🔄 README completo
- 🔄 Vídeo demonstrativo no Loom
- 🔄 Preparação do repositório GitHub
- 🔄 Documentação final

## 🎯 Critérios de Sucesso

### Funcionais
- [ ] Sistema analisa qualquer copy em < 30 segundos
- [ ] Identifica nível de consciência com 80%+ de precisão
- [ ] Gera mínimo 5 pontos de melhoria relevantes
- [ ] Cria mínimo 3 ângulos criativos diferentes
- [ ] Output em JSON estruturado e válido

### Técnicos
- [ ] Workflow n8n exportável e importável
- [ ] Banco de dados com schema documentado
- [ ] Prompts documentados e versionados
- [ ] Sistema escalável para múltiplas análises
- [ ] Logs e métricas de qualidade

### Negócio
- [ ] Demonstra compreensão profunda do Schwartz
- [ ] Produz insights acionáveis para copywriters
- [ ] Interface simples e intuitiva
- [ ] Documentação clara para uso e manutenção

---

**Autor**: [Seu Nome]  
**Data**: Janeiro 2024  
**Versão**: 1.0  
**Status**: Em Desenvolvimento