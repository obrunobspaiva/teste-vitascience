# Diagramas de Arquitetura - Clone Digital Eugene Schwartz

Este documento contém todos os diagramas Mermaid que ilustram a arquitetura e fluxos do sistema Clone Digital Eugene Schwartz.

## 1. Fluxo Principal do Sistema

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
    
    style A fill:#e1f5fe
    style K fill:#e8f5e8
    style E fill:#fff3e0
    style H fill:#f3e5f5
```

## 2. Arquitetura Detalhada do n8n Workflow

```mermaid
flowchart LR
    subgraph "Input Layer"
        WH[Webhook /lead/analyze]
        SAN[Fn Sanitize & Meta]
    end
    
    subgraph "Analysis Layer"
        EMB[LLM Embedding lead]
        MATCH[Supabase Match BA]
        CLASS[LLM Classifier]
        DISS[LLM Dissector]
        CRIT[LLM Critic]
        ANG[LLM Angles]
        AUD[LLM Audience]
    end
    
    subgraph "Knowledge Layer"
        SUPA[(Supabase/PostgreSQL)]
        CHUNKS[BA Chunks + Embeddings]
    end
    
    subgraph "Generation Layer"
        MERGE[Fn Merge Output]
        HASH[Fn Lead Hash]
    end
    
    subgraph "Output Layer"
        UPSERT[Supabase Upsert]
        RESP[JSON Response]
    end
    
    WH --> SAN
    SAN --> EMB
    EMB --> MATCH
    MATCH --> CLASS
    CLASS --> DISS
    CLASS --> CRIT
    DISS --> ANG
    CRIT --> MERGE
    ANG --> MERGE
    SAN --> AUD
    AUD --> MERGE
    SAN --> HASH
    MERGE --> UPSERT
    UPSERT --> RESP
    
    MATCH <--> SUPA
    SUPA <--> CHUNKS
    UPSERT --> SUPA
    
    style WH fill:#e3f2fd
    style RESP fill:#e8f5e8
    style SUPA fill:#fff3e0
    style MERGE fill:#f3e5f5
```

## 3. Estrutura de Dados - Relacionamentos

```mermaid
erDiagram
    SOURCES {
        uuid id PK
        text name
        timestamp created_at
    }
    
    CHUNKS {
        bigserial id PK
        uuid source_id FK
        int idx
        text content
        vector embedding
        jsonb meta
    }
    
    ANALYSES {
        bigserial id PK
        text lead_text
        jsonb meta
        jsonb analysis
        timestamp created_at
    }
    
    SOURCES ||--o{ CHUNKS : contains
    CHUNKS ||--o{ ANALYSES : "used in"
```

## 4. Fluxo de Processamento de Consciência

```mermaid
stateDiagram-v2
    [*] --> InputReceived
    InputReceived --> TextAnalysis
    TextAnalysis --> ConsciousnessClassification
    
    ConsciousnessClassification --> Unaware : Level 5
    ConsciousnessClassification --> ProblemAware : Level 4
    ConsciousnessClassification --> SolutionAware : Level 3
    ConsciousnessClassification --> ProductAware : Level 2
    ConsciousnessClassification --> MostAware : Level 1
    
    Unaware --> KnowledgeRetrieval
    ProblemAware --> KnowledgeRetrieval
    SolutionAware --> KnowledgeRetrieval
    ProductAware --> KnowledgeRetrieval
    MostAware --> KnowledgeRetrieval
    
    KnowledgeRetrieval --> ImprovementGeneration
    ImprovementGeneration --> AngleCreation
    AngleCreation --> OutputFormatting
    OutputFormatting --> [*]
```

## 5. Arquitetura de Prompts

```mermaid
mindmap
  root((Prompts Eugene))
    Consciousness Classifier
      Level Detection
      Confidence Score
      Reasoning
    Structure Analyzer
      Framework Detection
      Evidence Extraction
      Pattern Recognition
    Problem Detector
      Issue Identification
      Impact Assessment
      Eugene Solutions
    Angle Generator
      Creative Angles
      Target Levels
      Headlines
    Quality Validator
      Consistency Check
      Output Validation
      Score Assignment
```

## 6. Integração com Sistemas Externos

```mermaid
sequenceDiagram
    participant User
    participant n8n
    participant OpenAI
    participant Supabase
    participant PostgreSQL
    
    User->>n8n: POST /lead/analyze
    n8n->>n8n: Sanitize & Extract Meta
    n8n->>OpenAI: Generate Embeddings
    OpenAI-->>n8n: Embedding Vector
    n8n->>Supabase: Search Similar Chunks
    Supabase->>PostgreSQL: Vector Search
    PostgreSQL-->>Supabase: Matching Chunks
    Supabase-->>n8n: Context Data
    
    loop LLM Analysis
        n8n->>OpenAI: Classifier Prompt
        OpenAI-->>n8n: Consciousness Level
        n8n->>OpenAI: Dissector Prompt
        OpenAI-->>n8n: Structure Analysis
        n8n->>OpenAI: Critic Prompt
        OpenAI-->>n8n: Improvements
        n8n->>OpenAI: Angles Prompt
        OpenAI-->>n8n: New Angles
    end
    
    n8n->>n8n: Merge Analysis Results
    n8n->>Supabase: Store Analysis
    Supabase->>PostgreSQL: Insert/Update
    n8n-->>User: JSON Response
```

## 7. Monitoramento e Métricas

```mermaid
dashboard
    title "Sistema Eugene Schwartz - Dashboard"
    
    card "Análises Hoje" {
        value 47
        delta +12%
    }
    
    card "Tempo Médio" {
        value "23s"
        delta -5s
    }
    
    card "Precisão Nível" {
        value "87%"
        delta +2%
    }
    
    card "Satisfação" {
        value "4.6/5"
        delta +0.2
    }
    
    chart "Distribuição por Nível" {
        x-axis ["Nível 1", "Nível 2", "Nível 3", "Nível 4", "Nível 5"]
        y-axis "Quantidade" 0 --> 20
        bar [8, 15, 18, 12, 6]
    }
    
    chart "Performance Temporal" {
        x-axis ["00:00", "06:00", "12:00", "18:00", "24:00"]
        y-axis "Tempo (s)" 0 --> 60
        line [25, 22, 28, 31, 24]
    }
```

## 8. Legenda de Componentes

### Cores dos Componentes
- 🔵 **Azul**: Entrada de dados e interfaces
- 🟢 **Verde**: Saída e resultados finais  
- 🟠 **Laranja**: Processamento e análise
- 🟣 **Roxo**: Geração criativa e ângulos
- 🟡 **Amarelo**: Armazenamento e dados

### Símbolos
- 📥 **Input**: Entrada de dados
- 📤 **Output**: Saída de dados
- 🧠 **LLM**: Processamento de linguagem
- 📚 **Knowledge**: Base de conhecimento
- 🔍 **Search**: Busca e recuperação
- ⚙️ **Process**: Processamento interno
- 💾 **Storage**: Armazenamento persistente

---

## Observações Técnicas

### Escalabilidade
- Workflow n8n permite processamento paralelo
- PostgreSQL com pgvector otimizado para buscas vetoriais
- Cache de embeddings para evitar recálculos

### Modularidade  
- Cada nó do n8n é independente e testável
- Prompts versionados e configuráveis
- Estrutura de dados flexível via JSONB

### Observabilidade
- Logs detalhados em cada etapa
- Métricas de performance e qualidade
- Dashboard para monitoramento em tempo real

### Flexibilidade
- Suporte a múltiplos modelos LLM
- Configuração via variáveis de ambiente
- Extensível para novos tipos de análise