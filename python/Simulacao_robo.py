# -*- coding: utf-8 -*-
import math
from tkinter import *
from Robo import *


class Janela:
    """
        Janela principal de simulacao
    """
    def __init__(self, janela_raiz):
        self.robo = None
        self.obstaculos = []

        self.ligado = False
        self.intervalo_de_simulacao = 30

        self.tipo_mapa = 0
        self.altura_labirinto = 430  # pixels
        self.largura_labirinto = 400  # pixels
        self.largura_mapa = 300

        janela_raiz.title('Simulator de Robos')
        self.canvas = Canvas(janela_raiz, width=self.largura_labirinto + self.largura_mapa, height=self.altura_labirinto)
        self.canvas.pack()
        self.frame = Frame(janela_raiz)
        self.frame.pack()
        self.janela_raiz = janela_raiz

        self.botao_liga_desliga = Button(self.frame, text='Liga', background='blue', command=self.liga_desliga)
        self.botao_liga_desliga.pack(side=LEFT)
        self.botao_tipo_mapa = Button(self.frame, text='Mapa 0', background='blue', command=self.troca_mapa)
        self.botao_tipo_mapa.pack(side=LEFT)
        self.botao_modo = Button(self.frame, text='Ideal', background='blue', command=self.troca_modo)
        self.botao_modo.pack(side=LEFT)
        self.botao_sensores = Button(self.frame, text='Sensores', background='blue', command=self.troca_exibicao_sensores)
        self.botao_sensores.pack(side=LEFT)
        self.botao_grid = Button(self.frame, text='Celulas', background='blue', command=self.troca_exibicao_grid)
        self.botao_grid.pack(side=LEFT)

        self.mostra_sensores = False
        self.mostra_celulas = False

        self.monta_simulacao()

    def liga_desliga(self):
        if not self.ligado:
            self.ligado = True
            self.botao_liga_desliga["text"] = "Desliga"
            self.janela_raiz.after(self.intervalo_de_simulacao, self.executa)
        else:
            self.ligado = False
            self.botao_liga_desliga["text"] = "Liga"

    def troca_mapa(self):
        if self.tipo_mapa == 0:
            self.tipo_mapa = 1
            self.botao_tipo_mapa["text"] = "Mapa 1"
        elif self.tipo_mapa == 1:
            self.tipo_mapa = 2
            self.botao_tipo_mapa["text"] = "Mapa 2"
        elif self.tipo_mapa == 2:
            self.tipo_mapa = 3
            self.botao_tipo_mapa["text"] = "Mapa 3"
        elif self.tipo_mapa == 3:
            self.tipo_mapa = 4
            self.botao_tipo_mapa["text"] = "Mapa 4"
        elif self.tipo_mapa == 4:
            self.tipo_mapa = 0
            self.botao_tipo_mapa["text"] = "Mapa 0"

        self.botao_modo["text"] = "Ideal"

        self.monta_simulacao()

    def troca_modo(self):
        if self.robo.ideal:
            self.robo.ideal = False
            self.botao_modo["text"] = "Real"
        else:
            self.robo.ideal = True
            self.botao_modo["text"] = "Ideal"

    def troca_exibicao_sensores(self):
        if self.mostra_sensores:
            self.mostra_sensores = False
        else:
            self.mostra_sensores = True

    def troca_exibicao_grid(self):
        if self.mostra_celulas:
            self.mostra_celulas = False
        else:
            self.mostra_celulas = True

    def monta_obstaculos(self):
        """
            Adiciona as paredes do labirinto
        """
        self.obstaculos = []

        # Moldura
        self.obstaculos.append([0, 0, 5, -self.altura_labirinto])
        self.obstaculos.append([self.largura_labirinto - 5, 0, self.largura_labirinto, -self.altura_labirinto])
        self.obstaculos.append([0, 0, self.largura_labirinto, -5])
        self.obstaculos.append([0, -(self.altura_labirinto - 5), self.largura_labirinto, -self.altura_labirinto])

        if self.tipo_mapa == 0:
            # Barreiras - Conjunto 1
            self.obstaculos.append([0, -60, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -120, self.largura_labirinto, -125])
            self.obstaculos.append([0, -180, self.largura_labirinto - 60, -185])
            self.obstaculos.append([60, -240, self.largura_labirinto, -245])
            self.obstaculos.append([0, -300, self.largura_labirinto - 60, -305])
            self.obstaculos.append([60, -360, self.largura_labirinto, -365])

        if self.tipo_mapa == 1:
            # Barreiras - Conjunto 2
            self.obstaculos.append([self.largura_labirinto - 65, 0, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -self.altura_labirinto + 65, 65, -self.altura_labirinto])
            self.obstaculos.append([0, -60, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -120, self.largura_labirinto, -125])
            self.obstaculos.append([self.largura_labirinto / 2 + 30, -180, self.largura_labirinto, -185])
            self.obstaculos.append([0, -180, self.largura_labirinto / 2 - 30, -185])
            self.obstaculos.append([self.largura_labirinto / 2 + 30, -240, self.largura_labirinto, -245])
            self.obstaculos.append([0, -240, self.largura_labirinto / 2 - 30, -245])
            self.obstaculos.append([0, -300, self.largura_labirinto - 60, -305])
            self.obstaculos.append([60, -360, self.largura_labirinto, -365])

        if self.tipo_mapa == 2:
            # Barreiras - Conjunto 3
            self.obstaculos.append([self.largura_labirinto - 65, 0, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -self.altura_labirinto + 65, 65, -self.altura_labirinto])
            self.obstaculos.append([0, -60, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -120, self.largura_labirinto, -125])
            self.obstaculos.append([60, -180, self.largura_labirinto - 60, -185])
            self.obstaculos.append([60, -240, self.largura_labirinto - 60, -245])
            self.obstaculos.append([0, -300, self.largura_labirinto - 60, -305])
            self.obstaculos.append([60, -360, self.largura_labirinto, -365])

        if self.tipo_mapa == 3:
            # Barreiras - Conjunto 4
            self.obstaculos.append([self.largura_labirinto - 65, 0, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -self.altura_labirinto + 65, 65, -self.altura_labirinto])
            self.obstaculos.append([self.largura_labirinto / 2, -180, self.largura_labirinto / 2 + 5, -240])
            self.obstaculos.append([0, -60, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -120, self.largura_labirinto, -125])
            self.obstaculos.append([60, -180, self.largura_labirinto - 60, -185])
            self.obstaculos.append([60, -240, self.largura_labirinto - 60, -245])
            self.obstaculos.append([0, -300, self.largura_labirinto - 60, -305])
            self.obstaculos.append([60, -360, self.largura_labirinto, -365])

        if self.tipo_mapa == 4:
            # Barreiras - Conjunto 5
            self.obstaculos.append([0, -60, self.largura_labirinto - 60, -65])
            self.obstaculos.append([60, -360, self.largura_labirinto, -365])

    def monta_simulacao(self):
        self.robo = None

        if self.tipo_mapa == 0:
            self.robo = Robo(30, -30, 0, 10)
        elif self.tipo_mapa == 1:
            self.robo = Robo(370, -30, -math.pi / 2, 10)
        elif self.tipo_mapa == 2:
            self.robo = Robo(30, -270, 0, 10)
        elif self.tipo_mapa == 3:
            self.robo = Robo(30, -270, 0, 10)
        elif self.tipo_mapa == 4:
            self.robo = Robo(30, -30, 0, 10)

        self.canvas.delete("all")
        self.monta_obstaculos()
        self.desenha_obstaculos()
        self.desenha_robo()

    def executa(self):
        """
            Laco principal da simulacao.
        """
        if not self.ligado:
            return()

        # Simulacao do movimento do robo
        self.desenha_robo()
        self.desenha_mapa()
        self.robo.dinamica_robo(self.obstaculos)

        # Atualiza tela
        self.canvas.update()
        self.janela_raiz.after(self.intervalo_de_simulacao, self.executa)

    def desenha_robo(self):
        """
            Desenha um robo na janela principal.
            Y cresce para baixo na tela
        """
        coord_x = self.robo.coord_x
        coord_y = self.robo.coord_y
        angulo = self.robo.angulo
        raio = self.robo.raio

        for reta in self.robo.retas:
            x1, y1 = self.robo.rotaciona(reta[0], reta[1], angulo)
            x2, y2 = self.robo.rotaciona(reta[2], reta[3], angulo)
            if reta[4] is None:
                reta[4] = self.canvas.create_line(coord_x + x1, -coord_y - y1, coord_x + x2, -coord_y - y2)
            else:
                self.canvas.coords(reta[4], coord_x + x1, -coord_y - y1, coord_x + x2, -coord_y - y2)

        if self.mostra_sensores:
            for sensor in self.robo.sensores_distancia:
                x1 = sensor.coord_x_ini_varredura
                y1 = sensor.coord_y_ini_varredura
                x2 = sensor.coord_x_fim_varredura
                y2 = sensor.coord_y_fim_varredura
                if sensor.referencia_figura is None:
                    sensor.referencia_figura = self.canvas.create_line(x1, -y1, x2, -y2)
                else:
                    self.canvas.coords(sensor.referencia_figura, x1, -y1, x2, -y2)
        else:
            for sensor in self.robo.sensores_distancia:
                if sensor.referencia_figura is not None:
                    self.canvas.delete(sensor.referencia_figura)
                    sensor.referencia_figura = None

        # Corpo do robo
        x1 = coord_x - raio
        y1 = -coord_y + raio
        x2 = coord_x + raio
        y2 = -coord_y - raio
        if self.robo.referencia_figura is None:
            self.robo.referencia_figura = self.canvas.create_oval(x1, y1, x2, y2, fill='red')
        else:
            self.canvas.coords(self.robo.referencia_figura, x1, y1, x2, y2)

    def desenha_obstaculos(self):
        self.canvas.create_rectangle(0, 0, self.largura_labirinto, self.altura_labirinto, fill='white')
        self.canvas.create_rectangle(self.largura_labirinto, 0, self.largura_labirinto + self.largura_mapa, self.altura_labirinto, fill='black')

        for obstaculo in self.obstaculos:
            self.canvas.create_rectangle(obstaculo[0], -obstaculo[1], obstaculo[2], -obstaculo[3], fill='gray')

    def desenha_mapa(self):
        tamanho_celula = self.largura_mapa / (self.robo.mapa.largura_em_celulas - 1)
        for LY in range(0, self.robo.mapa.altura_em_celulas - 1):
            for LX in range(0, self.robo.mapa.largura_em_celulas - 1):
                coordenada_esquerda = self.largura_labirinto + LX * tamanho_celula
                coordenada_direita = self.largura_labirinto + (LX + 1) * tamanho_celula - 1
                coordenada_superior = LY * tamanho_celula
                coordenada_inferior = (LY + 1) * tamanho_celula - 1
                if not self.robo.mapa.celulas[LY][LX].aberto_leste:
                    coordenada_direita -= 1
                if not self.robo.mapa.celulas[LY][LX].aberto_oeste:
                    coordenada_esquerda += 1
                if not self.robo.mapa.celulas[LY][LX].aberto_norte:
                    coordenada_superior += 1
                if not self.robo.mapa.celulas[LY][LX].aberto_sul:
                    coordenada_inferior -= 1
                if (self.robo.mapa.indice_x_robo == LX) and (self.robo.mapa.indice_y_robo == LY):
                    preenchimento = 'red'
                else:
                    if self.robo.mapa.celulas[LY][LX].desconhecido:
                        preenchimento = 'gray'
                    else:
                        preenchimento = 'white'
                if self.robo.mapa.celulas[LY][LX].referencia_figura is None:
                    self.robo.mapa.celulas[LY][LX].referencia_figura = self.canvas.create_rectangle(coordenada_esquerda , coordenada_superior , coordenada_direita , coordenada_inferior , outline = preenchimento , fill = preenchimento)
                else:
                    self.canvas.coords(self.robo.mapa.celulas[LY][LX].referencia_figura, coordenada_esquerda, coordenada_superior, coordenada_direita, coordenada_inferior)
                    self.canvas.itemconfig(self.robo.mapa.celulas[LY][LX].referencia_figura, outline=preenchimento, fill=preenchimento)

        if self.mostra_celulas:
            for LY in range(0, self.robo.mapa.altura_em_celulas * self.robo.mapa.MARCADORES_POR_CELULA):
                for LX in range(0, self.robo.mapa.largura_em_celulas * self.robo.mapa.MARCADORES_POR_CELULA):
                    marcador = self.robo.mapa.marcadores[LY][LX]
                    coordenada_esquerda = marcador.coord_x - 1
                    coordenada_direita = marcador.coord_x + 1
                    coordenada_superior = marcador.coord_y - 1
                    coordenada_inferior = marcador.coord_y + 1
                    if not marcador.dentro:
                        if (coordenada_direita < self.largura_labirinto) and (coordenada_inferior < self.altura_labirinto):
                            preenchimento = 'green'
                            if marcador.referencia_figura is None:
                                self.robo.mapa.marcadores[LY][LX].referencia_figura = self.canvas.create_rectangle(coordenada_esquerda, coordenada_superior, coordenada_direita, coordenada_inferior,outline=preenchimento, fill=preenchimento)
                            else:
                                self.canvas.coords(marcador.referencia_figura,coordenada_esquerda, coordenada_superior, coordenada_direita,coordenada_inferior)
        else:
            for LY in range(0, self.robo.mapa.altura_em_celulas * self.robo.mapa.MARCADORES_POR_CELULA):
                for LX in range(0, self.robo.mapa.largura_em_celulas * self.robo.mapa.MARCADORES_POR_CELULA):
                    marcador = self.robo.mapa.marcadores[LY][LX]
                    if marcador.referencia_figura is not None:
                        self.canvas.delete(marcador.referencia_figura)
                        marcador.referencia_figura = None

if __name__ == '__main__':
    raiz = Tk()
    Janela(raiz)
    raiz.mainloop()
