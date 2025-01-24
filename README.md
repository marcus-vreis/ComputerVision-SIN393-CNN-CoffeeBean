# Projeto SIN393 - Visão Computacional

## Tecnologias Utilizadas

As seguintes tecnologias foram empregadas no projeto:

- **Python**: Linguagem de programação base para o desenvolvimento.
- **Conda**: Gerenciador de pacotes e ambientes virtuais.
- **PyTorch**: Framework para construção e treinamento de modelos de redes neurais.
- **Matplotlib**: Biblioteca para criação de gráficos e visualização de dados.
- **Scikit-Learn**: Ferramentas para análise de dados e aprendizado de máquina.
- **TQDM**: Progress bar para acompanhamento de execuções.
- **Jupyter Notebook**: Ambiente para execução interativa de códigos e visualização de resultados.

## Artigo Científico

Um artigo detalhando os experimentos realizados foi elaborado e está disponível no repositório com o nome `Artigo.pdf`. Este documento inclui a metodologia, resultados e discussões referentes ao projeto.

---

## Vídeo Explicativo

Para complementar a documentação, foi criado um vídeo explicativo do trabalho, disponível neste **[link](https://www.youtube.com/watch?v=mVWqjKUZZsI)**. O vídeo aborda as etapas principais do projeto e os resultados obtidos.

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

### 1. Download do Banco de Dados

Banco de dados utilizado: **[USK-COFFEE](https://comvis.unsyiah.ac.id/usk-coffee/)**

Para baixar, siga os passos abaixo:

- Acesse o link fornecido.
- Desça a página até encontrar o botão **DATA AND CODE**.
- Preencha o formulário e realize o download do banco de dados.

### 2. Criação de Ambiente Virtual (Opcional, mas Recomendado)

Para garantir um ambiente isolado, recomenda-se criar um ambiente virtual utilizando o Conda:

```bash
conda create --name nome_do_seu_ambiente python=3.8
```

Ative o ambiente virtual recém-criado:

```bash
conda activate nome_do_seu_ambiente
```

### 3. Instalação do Jupyter Notebook

Instale o Jupyter Notebook no ambiente virtual:

```bash
conda install jupyter
```

### 4. Instalação das Bibliotecas Necessárias

Utilize o comando abaixo para instalar as dependências:

```bash
conda install numpy matplotlib scikit-learn tqdm pytorch torchvision -c pytorch
```

Certifique-se de que tudo está atualizado:

```bash
conda update --all
```

### 5. Clonagem do Repositório

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

### 6. Organização do Banco de Dados

Coloque o banco de dados na pasta do repositório clonado. Certifique-se de que os arquivos do dataset estão no mesmo diretório dos notebooks `.ipynb`.

### 7. Execução do Jupyter Notebook

Inicie o Jupyter Notebook:

```bash
jupyter notebook
```

Isso abrirá uma nova janela ou guia no navegador padrão, onde você poderá navegar até o diretório do projeto e abrir os notebooks.

### 8. Preparação do Dataset

Execute o arquivo `Converte_Dataset.py` para ajustar o dataset. O script remove classes desnecessárias, mantendo apenas as duas classes utilizadas no projeto.

### 9. Execução dos Modelos

Após a preparação do dataset, execute os notebooks dos modelos (`AlexNet_Model.ipynb`, `Resnet18_Model.ipynb` e `Resnet50_Model.ipynb`). Não são necessárias alterações adicionais no código.

### 10. Estrutura de Saída

- Os **pesos dos modelos** serão salvos em uma pasta chamada `modelos`.
- Os **resultados e gráficos** serão armazenados em uma pasta chamada `Gráficos`.

---

## Participantes

- [Brenno Alves Silva](https://github.com/BrennoA1ves)
- [Marcus Vinicius Diniz dos Reis](https://github.com/marcus-vreis)
---

## Agradecimentos

Queremos expressar nossa gratidão ao professor **João Mari** pelo valioso conhecimento compartilhado conosco, bem como pelo suporte contínuo ao longo da execução do projeto. 