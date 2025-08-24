# NotionToGithubPageJekyll

Repositório para exportar página de notion para Jekyll e subir para GithubPages.

Para isso, é preciso primeiro setar a variável de ambiente NOTION_TOKEN. Para maisn informações sobre como configurar esse token [Integration](https://www.notion.so/profile/integrations).

Depois, é preciso setar o ambiente do Python para execução. Recomendamos utilizar o [Poetry](https://python-poetry.org/) para gerenciar dependências e ambientes isolados.

Se ainda não tiver o Poetry instalado, faça:

    curl -sSL https://install.python-poetry.org | python3 -

Instale as dependências do projeto com:

    poetry install

Para executar, basta executar o seguinte comando:

    poetry run python script.py <PAGE_URL>
