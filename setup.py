from setuptools import setup, find_packages

setup(
    name='pacote_processamento',  # Nome do seu pacote
    version='0.1.0',  # Versão do seu pacote
    author='sulamy',  # Nome do autor
    author_email='sulamy.lobato34@gmail.com',  # Email do autor
    description='Um pacote Python para processamento de imagens.',  # Breve descrição do seu pacote
    long_description=open('README.md').read(),  # Descrição longa do seu pacote (do README)
    long_description_content_type='text/markdown',  # Tipo do conteúdo da descrição longa
    url='https://github.com/sulamyLobato/Pacote_Imagens',  # URL do repositório do projeto
    packages=find_packages(),  # Encontra e inclui automaticamente todos os pacotes
    install_requires=[  # Dependências do pacote
        'Pillow>=8.0.0',  # Inclua suas dependências aqui
    ],
    classifiers=[  # Classificadores para ajudar na categorização do pacote
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versão mínima do Python requerida
)
