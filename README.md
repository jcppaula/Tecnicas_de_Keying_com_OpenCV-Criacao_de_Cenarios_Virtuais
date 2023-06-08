<div>
  <a href="https://www.linkedin.com/in/júlio-cézar-de-paula-0b64b8226" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href = "mailto:jcp.paula17@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
  <a href="https://medium.com/@jcp.paula17" target="_blank"><img src="https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white"></a>
</div>
<br/>

# Tecnicas de Keying com OpenCV: Criação de Cenarios Virtuais

Este é um projeto de Detector de Fadiga desenvolvido para a Especialização em Visão Computacional. O programa utiliza técnicas de Visão Computacional e Aprendizado de Máquina para detectar sinais de fadiga (como fechamento prolongado dos olhos) em um fluxo de vídeo em tempo real.

<p align="center">
  <img src="Detector de Fadiga.gif" style="width: 800px; height: 500px;">
</p>

## Estrutura do Projeto

A estrutura do projeto é a seguinte:
```
.
├── alarm.wav
├── main.py
├── requirements.txt
└── shape_predictor_68_face_landmarks.dat
```

## Descrição dos arquivos:

* `alarm.mp3`: som de alarme que será tocado quando sinais de fadiga são detectados.
* `main.py`: script Python principal que contém a lógica do detector facial.
* `requirements.txt`: arquivo que lista as dependências necessárias para executar o programa.
* `shape_predictor_68_face_landmarks.dat`: arquivo de dados usado pelo detector de marcos faciais do dlib.  

## Pré-requisitos
Para executar este projeto, você precisa ter o Python instalado em seu sistema, eu estou usando a versão *3.8.5*. As dependências do projeto são listadas no arquivo requirements.txt e podem ser instaladas com o seguinte comando:

```
pip install -r requirements.txt
```
## Execução do Projeto

Para executar o projeto, você precisa passar algumas opções para o `script main.py`. As opções disponíveis são:

* `-a` ou `--alarme`: define se o programa deve tocar um alarme sonoro quando detectar sinais de fadiga. Se definido como 1, o alarme será tocado. Se definido como 0, nenhum alarme será tocado. O padrão é 0.
* `-w` ou `--webcam`: define o índice da webcam a ser usado para o fluxo de vídeo. O padrão é 0.
Aqui está um exemplo de como executar o script `main.py`:
```
python main.py -a 1 -w 0
```
Este comando irá iniciar o detector de fadiga com um alarme sonoro e usará a webcam de índice 0 para o fluxo de vídeo.

Nota: O arquivo `shape_predictor_68_face_landmarks.dat` pode ser baixado clicando [neste link](https://github.com/italojs/facial-landmarks-recognition/raw/master/shape_predictor_68_face_landmarks.dat).

## Detalhes do Projeto

Este programa detecta sinais de fadiga monitorando o estado dos olhos de uma pessoa em um fluxo de vídeo. O processo ocorre nas seguintes etapas:

1. Captação do fluxo de vídeo em tempo real através da webcam.
2. Detecção de rostos na imagem utilizando o detector de rostos do dlib.
3. Detecção dos marcos faciais (em particular, os olhos) usando o preditor de marcos faciais do dlib.
4. Cálculo da Relação de Aspecto dos Olhos (EAR) baseado na posição dos marcos dos olhos.
5. Verificação se a EAR está abaixo do limiar definido por um determinado número de quadros consecutivos. Isso indica que a pessoa pode estar com sono.
6. Se a condição acima for satisfeita, um alarme sonoro é acionado para alertar a pessoa.

O programa utiliza o detector de marcos faciais do dlib para determinar a posição dos olhos e calcular a EAR. A EAR é uma medida que indica o grau de abertura dos olhos. Quando a EAR está abaixo de um limiar definido durante um número específico de quadros consecutivos, o programa considera que a pessoa está com sono e aciona um alarme.

## Referências Bibliográficas

SOUKUPOVA, Tereza; CECH, Jan. [Real-time eye blink detection using facial landmarks](https://vision.fe.uni-lj.si/cvww2016/proceedings/papers/05.pdf). In: 21st computer vision winter workshop, Rimske Toplice, Slovenia. 2016.


### Sobre mim:
* [LinkedIn](https://www.linkedin.com/in/j%C3%BAlio-c%C3%A9zar-de-paula-0b64b8226/)
* [Medium](https://medium.com/@jcp.paula17)
* [Portfólio](https://github.com/jcppaula/Portfolio)
