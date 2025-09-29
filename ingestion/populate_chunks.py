import os
import psycopg2
import fitz  # PyMuPDF
from openai import OpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# ========= CONFIG =========
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT"))

TABLE_NAME = os.getenv("TABLE_NAME")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))
# ==========================

# Inicializar cliente OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def chunk_text(text, size=CHUNK_SIZE):
    """Divide texto em pedaços de tamanho fixo (aprox. por palavras)."""
    words = text.split()
    for i in range(0, len(words), size):
        yield " ".join(words[i:i+size])

def embed_text(text):
    """Gera embedding usando OpenAI."""
    try:
        resp = client.embeddings.create(
            model="text-embedding-3-small",
            input=text
        )
        return resp.data[0].embedding
    except Exception as e:
        print(f"❌ Erro ao gerar embedding: {e}")
        return None

def main():
    # Verificar se as variáveis necessárias estão definidas
    if not OPENAI_API_KEY:
        print("❌ OPENAI_API_KEY não encontrada. Configure no arquivo .env")
        return
    
    if not DB_PASSWORD:
        print("❌ DB_PASSWORD não encontrada. Configure no arquivo .env")
        return

    # 1. Verificar se o PDF existe
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, "Breakthrough_Advertising.pdf")
    if not os.path.exists(pdf_path):
        print(f"❌ Arquivo {pdf_path} não encontrado!")
        return

    print("📖 Lendo PDF...")
    try:
        pdf_document = fitz.open(pdf_path)
        full_text = ""
        page_count = pdf_document.page_count
        
        for page_num in range(page_count):
            page = pdf_document[page_num]
            text = page.get_text()
            full_text += text + "\n"
            
        pdf_document.close()
        print(f"📄 Texto extraído: {len(full_text)} caracteres de {page_count} páginas")
        
        if len(full_text.strip()) == 0:
            print("⚠️ Nenhum texto foi extraído do PDF. Verifique se o arquivo não está protegido ou corrompido.")
            return
            
    except Exception as e:
        print(f"❌ Erro ao ler PDF: {e}")
        return

    # 2. Quebrar em chunks
    print("✂️ Dividindo em chunks...")
    chunks = list(chunk_text(full_text))
    print(f"📦 {len(chunks)} chunks criados")

    # 3. Conectar ao banco de dados
    try:
        print("🔌 Conectando ao banco de dados...")
        print(f"Host: {DB_HOST}")
        print(f"Database: {DB_NAME}")
        print(f"User: {DB_USER}")
        print(f"Port: {DB_PORT}")
        
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
            sslmode='require'
        )
        cur = conn.cursor()
        print("✅ Conectado ao banco de dados")
    except Exception as e:
        print(f"❌ Erro ao conectar ao banco: {e}")
        print("💡 Verifique se as credenciais do Supabase estão corretas")
        return

    # 4. Primeiro, criar/verificar source
    print("📋 Criando source...")
    try:
        cur.execute(
            "INSERT INTO sources (title, origin) VALUES (%s, %s) ON CONFLICT DO NOTHING RETURNING id",
            ("Breakthrough Advertising", "PDF")
        )
        result = cur.fetchone()
        if result:
            source_id = result[0]
        else:
            # Source já existe, buscar ID
            cur.execute("SELECT id FROM sources WHERE title = %s", ("Breakthrough Advertising",))
            result = cur.fetchone()
            if result:
                source_id = result[0]
            else:
                # Se não existe, criar sem ON CONFLICT
                cur.execute(
                    "INSERT INTO sources (title, origin) VALUES (%s, %s) RETURNING id",
                    ("Breakthrough Advertising", "PDF")
                )
                source_id = cur.fetchone()[0]
        print(f"✅ Source ID: {source_id}")
    except Exception as e:
        print(f"❌ Erro ao criar source: {e}")
        return

    # 5. Inserir chunks
    print("🚀 Iniciando inserção dos chunks...")
    success_count = 0
    for idx, chunk in enumerate(chunks):
        try:
            embedding = embed_text(chunk)
            if embedding is None:
                continue
                
            cur.execute(
                """
                INSERT INTO chunks (source_id, idx, content, embedding, meta)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (source_id, idx, chunk, embedding, '{"tag": "book", "source": "Breakthrough Advertising"}')
            )
            success_count += 1
            print(f"✅ Inserido chunk {success_count}/{len(chunks)} (ID: {idx})")
        except Exception as e:
            print(f"❌ Erro no chunk {idx}: {e}")

    try:
        conn.commit()
        print(f"💾 Dados salvos no banco de dados")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")
    finally:
        cur.close()
        conn.close()
        
    print(f"🔥 População concluída! {success_count}/{len(chunks)} chunks inseridos com sucesso!")

if __name__ == "__main__":
    main()
