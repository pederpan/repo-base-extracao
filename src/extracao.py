import os

def extrair_todas_imagens():
    # Pasta com imagens e pasta para resultados
    pasta_imagens = "../imagens/2024-1Dia-Caderno1-Azul-AplicaçãoRegular"
    pasta_resultados = "../resultados/2024-1Dia-Caderno1-Azul-AplicaçãoRegular"
    
    # Criar pasta de resultados se não existir
    if not os.path.exists(pasta_resultados):
        os.makedirs(pasta_resultados)
    
    # Processar cada arquivo na pasta
    for arquivo in os.listdir(pasta_imagens):
        if arquivo.endswith(('.png', '.jpg', '.jpeg')):
            print(f"Processando: {arquivo}")
            
            # Caminhos completos
            caminho_imagem = os.path.join(pasta_imagens, arquivo)
            nome_saida = arquivo.split('.')[0]
            caminho_saida = os.path.join(pasta_resultados, nome_saida)
            
            # Comando Tesseract simples
            comando = f'tesseract "{caminho_imagem}" "{caminho_saida}" -l por'
            
            # Executar e mostrar resultado
            os.system(comando)
            print(f"✅ Salvo: {nome_saida}")

if __name__ == "__main__":
    extrair_todas_imagens()