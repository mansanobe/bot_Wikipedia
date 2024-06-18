Esse projeto busca automatizar a pesquisa e extração de dados de paginas de wikípedia.

Para realizar a pesquisa, o programa recebe do usuário os termos da pesquisa a ser feita e os envia para a wikípedia.
A wikípedia possui tres possiveis páginas para o resultado de alguma pesquisa, a página a ser mostrada depende da natureza da pesquisa feita.
Esses casos são:
Diretamente a página que você busca, em caso de pesquisa mais especifica.
Em caso de pesquisa genérica, é exibida a pagina de resultados de pesquisa, onde aparecem diversos resultados de páginas relacionadas ao que foi pesquisado.
Também existe a chamada "página de desambiguação", que lista os artigos que podem ser associados a um ou vários títulos.

Cada um desses casos foi tratado dentro do código, buscando alguma caracteristica única de cada uma dessas páginas para conseguir identifica-las.
Nos casos das páginas de resultados de pesquisa e página de desambiguação, o link acessado é sempre o primeiro, o que pode fazer com que o resultado final não seja o esperado pelo usuário, portanto o interessante é ser o mais especifico possivel.
Ao final do código, é extraida a data da última modificação realizada na página e essa data é impressa para o usuário.
