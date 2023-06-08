<div>
  <a href="https://www.linkedin.com/in/júlio-cézar-de-paula-0b64b8226" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href = "mailto:jcp.paula17@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://medium.com/@jcp.paula17" target="_blank"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white"></a>
</div>
<br/>

# Tecnicas de Keying com OpenCV: Criação de Cenários Virtuais

Esse programa usa Técnincas de Keying e a bibliotéca OpenCV, para remover o fundo verde do vídeo de uma pessoa em um escritório e colocar um fundo de praia.

<p align="center">
  <img src="Fundo_Verde_GIF.gif" style="width: 700px; height: 400px;">
</p>

## Estrutura do Projeto

A estrutura do projeto é a seguinte:
```
.
├── data
│   ├── praia.mp4
│   └── webcam.mp4
├── projeto_01.py
└── requirements.txt
```

## Descrição dos arquivos:

* `praia.mp4`: fundo da praia que sera usado no projeto.
* `webcam.mp4`: video com uma pessoa e um fundo verde. 
* `projeto_01.py`: código fonte do projeto.  
* `requirements.txt`: arquivo que lista as dependências necessárias para executar o programa.

## Pré-requisitos
Para executar este projeto, você precisa ter o Python instalado em seu sistema, eu estou usando a versão *3.8.5*. As dependências do projeto são listadas no arquivo requirements.txt e podem ser instaladas com o seguinte comando:

```
pip install -r requirements.txt
```
## Execução do Projeto

Para executar o projeto, basta executar o código na IDE de sua preferencia.

Este comando irá iniciar o programa que exibirá o vídeo com o fundo alterado na tela e salvará o output na pasta do projeto.

## Detalhes do Projeto

Este programa altera o fundo de um vídeo com fundo verde. O processo ocorre nas seguintes etapas:

1. Captação do fluxo de vídeo em tempo real através da webcam.
2. Define os limites da cor verde em RGB.
3. Cria uma máscara com os pixels que estão dentro da faixa de cor verde.
4. Usa a máscara para extrair os pixels da praia que correspondem ao fundo verde da webcam.
5. Inverte a máscara para obter os pixels que não estão na faixa de cor verde
6. Usa a máscara invertida para extrair os pixels da webcam que não são verdes.
7. Escreve os quadros nos arquivos de vídeo correspondentes.

### Sobre mim:
* [LinkedIn](https://www.linkedin.com/in/j%C3%BAlio-c%C3%A9zar-de-paula-0b64b8226/)
* [Medium](https://medium.com/@jcp.paula17)
* [Portfólio](https://github.com/jcppaula/Portfolio)
