# Documentação de Prompts - Sistema de Análise de Copy Eugene Schwartz

## Visão Geral

Este documento contém a documentação de todos os prompts utilizados para análise de copy baseado na metodologia de Eugene Schwartz. Cada arquivo de prompt tem uma função específica no processo de análise.

## Arquivos de Prompts

### 1. audience.txt

**Função**: Classificar a audiência principal do texto

**Conteúdo do Prompt**:
```
Você é um classificador de audiência. Leia o texto fornecido e identifique a audiência principal. Responda SOMENTE em JSON no formato: {"audience":"[sexo] [range-idade], [objetivo]"}
```

**Objetivo**: Identificar o público-alvo do copy analisado
**Formato de Saída**: JSON com audiência identificada

---

### 2. classifier.txt

**Função**: Classificar o nível de consciência segundo Eugene Schwartz

**Conteúdo do Prompt**:
```
Você é um avaliador de copy no estilo Eugene Schwartz. Escala: 1=Mais consciente, 2=Produto-consciente, 3=Solução-consciente, 4=Problema-consciente, 5=Desconhecedor. Responda SOMENTE JSON: {"level":<int>,"reason":"..."}.
```

**Objetivo**: Determinar o nível de consciência do público-alvo
**Formato de Saída**: JSON com nível (1-5) e justificativa

**Escala de Consciência**:
- 1 = Mais Consciente (Product-aware/Most aware)
- 2 = Produto-consciente
- 3 = Solução-consciente
- 4 = Problema-consciente
- 5 = Desconhecedor (Unaware)

---

### 3. dissector.txt

**Função**: Identificar frameworks de copywriting presentes

**Conteúdo do Prompt**:
```
Identifique frameworks de copy presentes (PAS, AIDA, 4P, BAB, Big Idea). Responda SOMENTE JSON: {"frameworks_detected":[...],"evidence":[{"framework":"AIDA","snippet":"..."}]}.
```

**Objetivo**: Detectar estruturas e frameworks utilizados no copy
**Formato de Saída**: JSON com frameworks detectados e evidências

**Frameworks Suportados**:
- PAS (Problem-Agitation-Solution)
- AIDA (Attention-Interest-Desire-Action)
- 4P (Picture-Promise-Prove-Push)
- BAB (Before-After-Bridge)
- Big Idea

---

### 4. critic.txt

**Função**: Gerar melhorias no estilo Eugene Schwartz

**Conteúdo do Prompt**:
```
Atue como Eugene Schwartz. Liste no mínimo 5 melhorias. Responda SOMENTE JSON como array: [{"issue":"...","why":"...","how_eugene_fixes":"...","rewrite_example":"..."}]. Foque clareza, prova, mecanismo, especificidade, ética.
```

**Objetivo**: Sugerir melhorias baseadas na metodologia de Eugene Schwartz
**Formato de Saída**: Array JSON com melhorias detalhadas

**Focos de Melhoria**:
- Clareza
- Prova
- Mecanismo
- Especificidade
- Ética

---

### 5. angles.txt

**Função**: Criar novos ângulos para diferentes níveis de consciência

**Conteúdo do Prompt**:
```
Crie no mínimo 3 novos ângulos para níveis diferentes. Responda SOMENTE JSON: [{"level_target":<int>,"angle":"...","headlines":["..."],"rationale":"..."}].
```

**Objetivo**: Desenvolver abordagens alternativas para diferentes públicos
**Formato de Saída**: Array JSON com novos ângulos

**Estrutura do Ângulo**:
- level_target: Nível de consciência alvo (1-5)
- angle: Descrição do ângulo
- headlines: Array de headlines sugeridas
- rationale: Justificativa do ângulo

---

## Estruturas de Dados

### Formato de Saída - Audience
```json
{
  "audience": "[sexo] [range-idade], [objetivo]"
}
```

### Formato de Saída - Classifier
```json
{
  "level": 3,
  "reason": "Justificativa do nível identificado"
}
```

### Formato de Saída - Dissector
```json
{
  "frameworks_detected": ["AIDA", "PAS"],
  "evidence": [
    {
      "framework": "AIDA",
      "snippet": "Trecho que evidencia o framework"
    }
  ]
}
```

### Formato de Saída - Critic
```json
[
  {
    "issue": "Problema identificado",
    "why": "Por que é um problema",
    "how_eugene_fixes": "Como Eugene resolveria",
    "rewrite_example": "Exemplo reescrito"
  }
]
```

### Formato de Saída - Angles
```json
[
  {
    "level_target": 2,
    "angle": "Descrição do ângulo",
    "headlines": ["Headline 1", "Headline 2"],
    "rationale": "Justificativa do ângulo"
  }
]
```

## Uso dos Prompts

### Características Gerais
- Todos os prompts retornam respostas em formato JSON
- Baseados na metodologia de Eugene Schwartz
- Focados em análise de copy e copywriting
- Projetados para análise sequencial e complementar

### Aplicação
Estes prompts podem ser utilizados individualmente ou em conjunto para uma análise completa de copy, seguindo a sequência:
1. **Audience** → Identificação do público
2. **Classifier** → Nível de consciência
3. **Dissector** → Frameworks utilizados
4. **Critic** → Pontos de melhoria
5. **Angles** → Novas abordagens