# 🔥 FURIA FAN INSIGHTS - Sistema de Verificação e Engajamento

<div align="center">
  <img src="https://apiesltv.imgix.net/images/team/logo/180_6389fd40-d1b3-4bd3-9a64-6ede7e24bd38.png" alt="FURIA Logo" width="200"/>
  <h3>📊 Conhecendo e Conectando os Fãs da FURIA Esports 📊</h3>
  <p><i>Solução completa para verificação de identidade e análise de perfil de fãs</i></p>
</div>

## 📋 Visão Geral do Projeto

O FURIA Fan Insights é um sistema interativo que permite coletar, validar e analisar informações sobre os fãs da FURIA Esports. Usando tecnologias de inteligência artificial, o sistema:

1. **Coleta dados pessoais** e interesses dos fãs
2. **Valida documentos** utilizando detecção facial
3. **Verifica identidade** por comparação biométrica
4. **Analisa perfis** em redes sociais e sites de esports
5. **Gera relatórios** personalizados sobre o engajamento dos fãs

Esta solução permite que a FURIA conheça melhor seu público e ofereça experiências exclusivas baseadas no perfil e nível de engajamento de cada fã.

## 💡 Principais Funcionalidades

### 👤 Validação de Identidade

- Upload de documentos com detecção facial
- Verificação biométrica por comparação entre selfie e documento
- Validação de CPF em tempo real

### 📱 Análise de Redes Sociais

- Vinculação de perfis sociais ao cadastro do fã
- Análise de interações relacionadas a esports
- Verificação de relevância de conteúdo compartilhado

### 📊 Perfil de Engajamento

- Pontuação baseada em múltiplos fatores de engajamento
- Classificação em categorias: FÃ INICIANTE, FÃ LEAL, FÃ SUPERFURIA
- Recomendação de benefícios personalizados

### 📁 Gestão de Dados

- Armazenamento seguro de informações dos fãs
- Processamento local com foco em privacidade
- Exportação de relatórios em formato JSON

## 📸 Demonstração

<div align="center">
  <h3>📊 Telas do Sistema</h3>
  <div style="display: flex; justify-content: center; gap: 20px;">
    <div>
      <img src="https://i.imgur.com/UwRMfp3.png" alt="Formulário de Dados" width="400"/>
      <p><i>Formulário de coleta de dados</i></p>
    </div>
    <div>
      <img src="https://i.imgur.com/xWMRCuh.png" alt="Relatório de Engajamento" width="400"/>
      <p><i>Relatório de engajamento do fã</i></p>
    </div>
  </div>
</div>

## 🧠 Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto
- **Jupyter Notebook**: Interface interativa para coleta de dados
- **OpenCV & face_recognition**: Detecção facial e biometria
- **IPyWidgets**: Componentes interativos para o formulário
- **BeautifulSoup**: Web scraping para análise de perfis
- **NumPy & PIL**: Processamento de imagens
- **JSON**: Armazenamento de dados dos fãs

## ⚙️ Como Executar

### Pré-requisitos

- Python 3.13+
- Dependências listadas no arquivo pyproject.toml

### Instalação

1. **Clone o repositório**

   ```bash
   git clone https://github.com/PedroSmaxY/furia-fan-insights.git
   cd furia-fan-insights
   ```

2. **Instale as dependências**

   ```bash
   pip install -e .
   ```

3. **Execute o notebook**

   ```bash
   jupyter notebook notebook/know_your_fan.ipynb
   ```

## 📖 Guia de Uso

1. **Dados Pessoais**: Insira seu nome, endereço e CPF nos campos fornecidos.
2. **Interesses**: Descreva seus interesses em esports, como jogos favoritos, times (ex: FURIA), eventos e compras relacionadas.
3. **Upload de Documento**: Faça upload de uma imagem de um documento de identificação. A IA detectará se há um rosto na imagem.
4. **Redes Sociais**: Insira seu perfil de rede social (ex: Twitter, Instagram). A simulação exibirá interações relacionadas a esports.
5. **Links de Perfis**: Insira um link para seu perfil em um site de esports. A IA verificará se o conteúdo é relevante com base nos seus interesses.
6. **Verificação de Identidade**: Faça upload de uma selfie e clique em "Verificar Identidade" para comparar seu rosto com o documento fornecido.
7. **Gerar Relatório**: Visualize um relatório completo com sua classificação como fã e benefícios disponíveis.
8. **Salvar Dados**: Armazene suas informações para uso futuro pela FURIA.

## 🛠️ Estrutura do Projeto

```
furia-fan-insights/
├── notebook/              # Notebooks Jupyter
│   └── know_your_fan.ipynb    # Aplicação principal interativa
│
├── fan_data/              # Dados salvos dos fãs
│   └── fan_<cpf>.json     # Arquivo JSON para cada fã
│
├── pyproject.toml         # Configuração do projeto e dependências
├── README.md              # Documentação principal
└── .gitignore             # Arquivos ignorados pelo git
```

## 🔒 Segurança e Privacidade

- Todos os dados são processados localmente
- Nenhuma informação pessoal é enviada para servidores externos
- Os dados biométricos são utilizados apenas para verificação, não são armazenados
- CPFs são validados através de algoritmo, sem consulta a bases externas

## 👨‍💻 Desenvolvedor

**Pedro Henrique**  
GitHub: [PedroSmaxY](https://github.com/PedroSmaxY)

## 🏆 Status do Projeto

Este projeto foi desenvolvido para o desafio Know Your Fan da FURIA Esports:

✅ Coleta de dados e interesses dos fãs  
✅ Validação de identidade com IA  
✅ Análise de perfis em redes sociais  
✅ Verificação de links de perfis  
✅ Geração de relatórios de engajamento  
✅ Sistema de categorização de fãs  
✅ Armazenamento seguro de dados

---

<div align="center">
  <h3>🔥 FURIA FAN INSIGHTS 🔥</h3>
  <p><i>Este projeto foi desenvolvido para o desafio "Know Your Fan" da FURIA Esports, demonstrando habilidades em desenvolvimento Python e análise de dados com inteligência artificial.</i></p>
</div>
