# NotionToGithubPageJekyll

Repositório para exportar página de notion para Jekyll e subir para GithubPages.

Para isso, é preciso primeiro setar a variável de ambiente NOTION_TOKEN. Para descobrir o seu tokenV2 do notion, é preciso abrir o DevTools do seu navegador na aba aberta do notion. Em Aplicação > Cookies > https://www.notion.so você encontrará na lista o token, coloque no seu ambiente o valor encontrado.

Depois, é preciso setar o ambiente do python para execução. Recomendo usar o [virtualenv](https://virtualenv.pypa.io/en/latest/) para configurar o ambiente isolado.

Para instalar os pacotes que o projeto depende, basta executar:

    pip install -r requirements.txt

Para executar, basta executar o seguinte comando:

    python script.py <PAGE_URL>