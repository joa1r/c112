import os
import shutil

pasta_inicial = r'C:\Users\Acer\Documents\.Aulas python\PRO_1-4_C111_AtividadeDaProfessora2-main\downloads'

pasta_final = r'C:\Users\Acer\Documents\.Aulas python\PRO_1-4_C111_AtividadeDaProfessora2-main\imagens'


lista_de_arquivos = os.listdir(pasta_inicial)


for arquivo in lista_de_arquivos:
    nome, extensao = os.path.splitext(arquivo)
    
    if extensao == ' ':
        continue
    if extensao in ['.png', '.jpg', '.jfif']:
        pasta1 = pasta_inicial + '/' + arquivo
        pasta2 = pasta_final + '/' + arquivo

        print("Movendo " + arquivo + "para a pasta imagen...")
        shutil.move(pasta1, pasta2)

    if extensao in ['.gif']:
        pasta1 = pasta_inicial + '/' + arquivo
        pasta3 = 'Gifs'  

        if os.path.exists(pasta3):
            print("Movendo " + arquivo + "para a pasta gifs...")
            shutil.move(pasta1, pasta3)    
        else:
            os.makedirs(pasta3)
            print("Movendo " + arquivo + "para a pasta gifs...")
            shutil.move(pasta1, pasta3)
