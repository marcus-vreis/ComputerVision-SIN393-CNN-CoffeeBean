![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Anaconda](https://img.shields.io/badge/Anaconda-%2344A833.svg?style=for-the-badge&logo=anaconda&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
# Projeto SIN393 - Visão Computacional

## Tecnologias Utilizadas

As seguintes tecnologias foram empregadas no projeto:

- **Python**: Linguagem de programação base para o desenvolvimento.
- **Conda**: Gerenciador de pacotes e ambientes virtuais.
- **PyTorch**: Framework para construção e treinamento de modelos de redes neurais.
- **Matplotlib**: Biblioteca para criação de gráficos e visualização de dados.
- **NumPy**: Biblioteca para manipulação de arrays e operações numéricas de alto desempenho.
- **Scikit-Learn**: Ferramentas para análise de dados e aprendizado de máquina.
- **Jupyter Notebook**: Ambiente para execução interativa de códigos e visualização de resultados.

## Artigo Científico

Um artigo detalhando os experimentos realizados foi elaborado e está disponível no repositório com o nome `Artigo.pdf`. Este documento inclui a metodologia, resultados e discussões referentes ao projeto.

---

## Vídeo Explicativo

Para complementar a documentação, foi criado um vídeo explicativo do trabalho, disponível neste **[Link](https://www.youtube.com/watch?v=mVWqjKUZZsI)**. O vídeo aborda as etapas principais do projeto e os resultados obtidos.

---



## Descrição

Este repositório abriga o código-fonte do projeto elaborado durante a disciplina **SIN393 - Visão Computacional**. O escopo do projeto envolve a implementação e avaliação de alguns modelos de rede neural aplicados a uma base de dados de grãos de café.

O objetivo principal é explorar e analisar as capacidades desses modelos no contexto da visão computacional, proporcionando uma experiência prática e aprofundada aos participantes da disciplina. O código disponível aqui oferece uma visão transparente do processo de desenvolvimento, permitindo revisão, replicação e compreensão mais aprofundada do trabalho realizado.

---

## Arquivos

1. **`Converte_Dataset.py`**: Script para manipulação e ajuste do banco de dados utilizado.
2. **`AlexNet_Model.ipynb`**: Notebook para execução do modelo de rede neural AlexNet.
3. **`Resnet18_Model.ipynb`**: Notebook para execução do modelo de rede neural ResNet18.
4. **`Resnet50_Model.ipynb`**: Notebook para execução do modelo de rede neural ResNet50.

---

## Replicação dos Experimentos



## Replicação dos Experimentos

### 1. Baixe e Instale o Anaconda

Certifique-se de que o Anaconda está instalado em sua máquina. Caso não tenha, siga os passos abaixo:

- Acesse o site oficial do Anaconda: **[Anaconda Download](https://www.anaconda.com/products/distribution)**.
- Baixe a versão compatível com o seu sistema operacional.
- Siga as instruções do instalador para concluir a instalação.

Após instalado, abra o **Anaconda Prompt** pesquisando "Anaconda Prompt" no menu iniciar (Windows) ou via terminal no macOS/Linux.

### 2. Download do Banco de Dados

Banco de dados utilizado: **[USK-COFFEE](https://comvis.unsyiah.ac.id/usk-coffee/)**

Para baixar, siga os passos abaixo:

- Acesse o link fornecido.
- Desça a página até encontrar o botão **DATA AND CODE**.
- Preencha o formulário e realize o download do banco de dados.

### 3. Criação de Ambiente Virtual (Opcional, mas Recomendado)

Para garantir um ambiente isolado, recomenda-se criar um ambiente virtual utilizando o Conda:

```bash
conda create --name nome_do_seu_ambiente python=3.8
```

Ative o ambiente virtual recém-criado:

```bash
conda activate nome_do_seu_ambiente
```

### 4. Instalação do Jupyter Notebook

Instale o Jupyter Notebook no ambiente virtual:

```bash
conda install jupyter
```

### 5. Instalação das Bibliotecas Necessárias

Utilize o comando abaixo para instalar as dependências:

```bash
conda install numpy matplotlib scikit-learn tqdm pytorch torchvision -c pytorch
```

Certifique-se de que tudo está atualizado:

```bash
conda update --all
```

### 6. Clonagem do Repositório

Antes de clonar o repositório, certifique-se de que o **Git** está instalado em sua máquina. Caso não tenha o Git, siga as instruções abaixo:

- **Windows**: Baixe o instalador em [git-scm.com](https://git-scm.com/) e siga as instruções.
- **Linux**: Use o gerenciador de pacotes da sua distribuição. Por exemplo:

  ```bash
  sudo apt install git
  ```

Verifique a instalação:

```bash
git --version
```

Clone o repositório com o comando:

```bash
git clone https://github.com/marcus-vreis/ComputerVision-SIN393-CNN-CoffeeBean.git
```

### 7. Organização do Banco de Dados

Coloque o banco de dados na pasta do repositório clonado. Certifique-se de que os arquivos do dataset estão no mesmo diretório dos notebooks `.ipynb`.

### 8. Execução do Jupyter Notebook

Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

Isso abrirá uma nova janela ou guia no navegador padrão, onde você poderá navegar até o diretório do projeto e abrir os notebooks.

### 9. Preparação do Dataset

Execute o arquivo `Converte_Dataset.py` para ajustar o dataset. O script remove classes desnecessárias, mantendo apenas as duas classes utilizadas no projeto.

### 10. Execução dos Modelos

Após a preparação do dataset, execute os notebooks dos modelos (`AlexNet_Model.ipynb`, `Resnet18_Model.ipynb` e `Resnet50_Model.ipynb`). Não são necessárias alterações adicionais no código.

### 11. Estrutura de Saída

- Os **pesos dos modelos** serão salvos em uma pasta chamada `modelos`.
- Os **resultados e gráficos** serão armazenados em uma pasta chamada `Gráficos`.

---

## Participantes

- [Brenno Alves Silva](https://github.com/BrennoA1ves)
- [Marcus Vinicius Diniz dos Reis](https://github.com/marcus-vreis)
---

## Agradecimentos

Queremos expressar nossa gratidão ao professor **João Mari** pelo valioso conhecimento compartilhado conosco, bem como pelo suporte contínuo ao longo da execução do projeto. 