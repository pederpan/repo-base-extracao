# Extração de Conteúdo e Categorização de Questões do ENEM

## 📋 Descrição do Projeto

Este repositório é dedicado à **extração de conteúdo textual** de imagens de questões do ENEM utilizando técnicas de OCR (Optical Character Recognition). 

O projeto complementa o trabalho realizado em [PreTratamento_CategorizacaoQuestoesENEM](https://github.com/AlexandreNP9/PreTratamento_CategorizacaoQuestoesENEM), onde os cadernos em PDF são pré-processados e cada questão é convertida em uma imagem individual.

## 🎯 Objetivos

- [ ] Implementar e comparar diferentes APIs de OCR
- [ ] Extrair o conteúdo textual de imagens de questões do ENEM
- [ ] Gerar arquivos `.txt` correspondentes a cada imagem processada
- [ ] Avaliar a precisão e eficiência de cada solução de OCR
- [ ] Preparar os dados para futura categorização e análise

## 🔧 Tecnologias e APIs em Teste

### APIs de OCR
- [ ] **Google Cloud Vision API**
- [ ] **Amazon Textract**
- [ ] **Microsoft Azure Computer Vision**
- [ ] **OCR.space** (API gratuita)
- [ ] **Tesseract OCR** (solução local)

### Linguagens e Ferramentas
- Python 3.12.3
- Jupyter Notebook para análise
- Bibliotecas: PIL, pytesseract, requests, os, pathlib

## 📁 Estrutura do Projeto
ExtracaoConteudo_CategorizacaoQuestoesENEM/  
│  
├── 📊 notebooks/ # Análises e testes comparativos  
├── 🔧 src/ # Códigos de extração  
├── 📁 imagens/ # Imagens de entrada (questões)  
├── 📁 resultados/ # Textos extraídos (.txt)  
├── 📋 metricas/ # Métricas de avaliação  
└── 📚 docs/ # Documentação  

## 📊 Métricas de Avaliação
As APIs serão avaliadas com base em:

### ✅ Precisão do texto extraído
⚡ Velocidade de processamento  
💰 Custo por imagem processada  
🔄 Suporte a caracteres especiais e fórmulas matemáticas  

## 🔗 Projeto Relacionado
PreTratamento_CategorizacaoQuestoesENEM → Pré-processamento de PDFs e segmentação de questões

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para:  
Sugerir novas APIs de OCR  
Reportar problemas ou melhorias  
Compartilhar resultados de testes  

## 📄 Licença
MIT License

# OBSERVAÇÕES técnicas
Distribuição do S.O. utilizado:  Linux Mint 22  

## 🚀 Como Usar
### No Linux Mint
#### Criar variável de ambiente
```bash
python3 -m venv venv  
source venv/bin/activate  
```
#### Para instalar o tesseract
```bash
sudo apt update
sudo apt install tesseract-ocr
sudo apt install tesseract-ocr-por  // Para português
sudo apt install tesseract-ocr-eng  // Para inglês
tesseract --version                 // Verificar instalação
```

### Pré-requisitos
```bash
pip install -r requirements.txt

from src.ocr_processor import processar_lote

# Processar todas as imagens de uma pasta
processar_lote('imagens/questoes', 'resultados/textos')
```