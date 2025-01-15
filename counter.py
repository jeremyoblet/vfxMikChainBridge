import os

def count_python_lines(directory):
    """
    Parcourt un répertoire et ses sous-répertoires pour lister tous les fichiers .py
    et compter le total des lignes de code.

    :param directory: Chemin du répertoire à analyser.
    :return: Tuple contenant la liste des fichiers trouvés et le total des lignes de code.
    """
    py_files = []
    total_lines = 0

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                py_files.append(file_path)
                with open(file_path, 'r', encoding='utf-8') as f:
                    try:
                        lines = f.readlines()
                        total_lines += len(lines)
                    except Exception as e:
                        print(f"Impossible de lire {file_path}: {e}")

    return py_files, total_lines

if __name__ == "__main__":
    directory = input("Entrez le chemin du répertoire à analyser : ").strip()
    if not os.path.isdir(directory):
        print(f"Le chemin spécifié n'est pas un répertoire valide : {directory}")
    else:
        files, lines_count = count_python_lines(directory)
        print(f"\nFichiers Python trouvés ({len(files)}):")
        for file in files:
            print(f"  - {file}")
        print(f"\nNombre total de lignes de code : {lines_count}")
