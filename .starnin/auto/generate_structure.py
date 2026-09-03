import os
import json

# Como o script está em /.starsnin/auto/, precisamos subir dois níveis 
# para alcançar a raiz do repositório onde estão as pastas de pesquisa.
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
index_data = []

# Varre os diretórios a partir da raiz do projeto
for root, dirs, files in os.walk(ROOT_DIR):
    # Ignora pastas ocultas, o diretório do próprio starnin e o .git
    if ".git" in root or ".starsnin" in root:
        continue
        
    for file in files:
        if file.endswith(".json") and file != "index.json":
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, ROOT_DIR).replace("\\", "/")
            
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = json.load(f)
                    
                    index_data.append({
                        "path": relative_path,
                        "data": content
                    })
            except Exception as e:
                print(f"Erro ao ler {file_path}: {e}")

# Salva o index.json na raiz do repositório
output_path = os.path.join(ROOT_DIR, "index.json")
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(index_data, f, ensure_ascii=False, indent=2)

print("index.json gerado com sucesso na raiz do Starnin!")
