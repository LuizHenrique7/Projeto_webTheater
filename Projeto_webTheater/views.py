
from django.shortcuts import render
from Projeto_webTheater.entity.categoria import Categoria


categoria1 = Categoria(1, 'Ação', 'Resgate', 'https://i.ytimg.com/vi/GMKKq_bYd0E/maxresdefault.jpg', 'O destemido mercenário Tyler Rake (Chris Hemsworth) enfrenta sua missão mais perigosa ao tentar resgatar o filho sequestrado de um chefe do crime internacional. Com direção de Sam Hargrave, Resgate é um filme de ação produzido por Joe e Anthony Russo, os visionários diretores de Vingadores: Ultimato.', 'https://www.youtube.com/embed/GMKKq_bYd0E')
categoria2 = Categoria(2, 'Roamance', 'Como Eu Era Antes de Você ', 'https://i.ytimg.com/vi/PnqUs3xiAVI/maxresdefault.jpg', 'Emilia Clarke e Sam Claflin estrelam em COMO EU ERA ANTES DE VOCÊ, filme baseado no romance de sucesso de JoJo Moyes! Estreia em 16 de junho nos cinemas.', 'https://www.youtube.com/embed/PnqUs3xiAVI')
categoria3 = Categoria(3, 'Ficção cientifica', 'Star Wars Episode IV: A New Hope', 'https://i.ytimg.com/vi/Po1Z_X0FpzY/maxresdefault.jpg', 'Dezenove anos após a formação do Império, Luke Skywalker entra na luta da Aliança Rebelde quando encontra Obi-Wan Kenobi, que viveu durante anos isolado no planeta deserto de Tatooine. Obi-Wan inicia o treinamento Jedi de Luke, quando Luke junta-se a ele em uma ousada missão para resgatar a bela Princesa Leia, líder dos Rebeldes, das garras de Darth Vader e do terrível Império.', 'https://www.youtube.com/embed/vZ734NWnAHA')

categorias = [categoria1, categoria2, categoria3]



def home(request):
    return render(request, 'home.html', {'categorias':categorias})

def ver_video(request, id:int):
    for categoria in categorias:
        if categoria.id == id:
            return render(request, 'video.html', {'categoria':categoria})
