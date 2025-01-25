import os
import shutil

def remover_classes(base_path, subpastas, classes_para_remover):
    for subpasta in subpastas:
        for classe in classes_para_remover:
            caminho_classe = os.path.join(base_path, subpasta, classe)
            if os.path.exists(caminho_classe):
                shutil.rmtree(caminho_classe)
                print(f"Pasta removida: {caminho_classe}")
            else:
                print(f"Pasta nao encontrada: {caminho_classe}")

# Caminho da pasta principal
caminho_principal = "USK-Coffee"

# Subpastas a serem processadas
subpastas = ["val", "test", "train"]

# Classes a serem removidas
classes_para_remover = ["peaberry", "longberry"]

# Executando a funcao
remover_classes(caminho_principal, subpastas, classes_para_remover)
