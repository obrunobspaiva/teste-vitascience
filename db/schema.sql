-- Extensão pgvector para embeddings
create extension if not exists vector;

-- ========================
-- TABELA: sources
-- ========================
create table if not exists sources (
    id uuid primary key default gen_random_uuid(),
    name text not null,
    created_at timestamp with time zone default now()
);

-- ========================
-- TABELA: chunks
-- ========================
create table if not exists chunks (
    id bigserial primary key,
    source_id uuid references sources(id) on delete cascade,
    idx int not null,
    content text not null,
    embedding vector(1536) not null,
    meta jsonb default '{}'
);

-- Index vetorial para busca rápida
create index if not exists idx_chunks_embedding
    on chunks
    using ivfflat (embedding vector_cosine_ops)
    with (lists = 100);

-- ========================
-- TABELA: analyses
-- ========================
create table if not exists analyses (
    id bigserial primary key,
    lead_text text not null,
    meta jsonb default '{}',
    analysis jsonb not null,
    created_at timestamp with time zone default now()
);

-- ========================
-- FUNÇÃO: match_ba_chunks
-- ========================
create or replace function match_ba_chunks(
  query_embedding vector,
  match_count int default 8
)
returns table(content text, similarity float)
language sql stable as $$
  select
    c.content,
    1 - (c.embedding <=> query_embedding) as similarity
  from chunks c
  order by c.embedding <=> query_embedding
  limit match_count;
$$;
