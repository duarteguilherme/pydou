# PyDOU - Crawler para o Diário Oficial da União

Este é um crawler para o Diário Oficial da União, feito em python.



-----------------
Para baixar os links do dia, use:

    from crawlerDOU import crawlerDOU
    x = crawlerDOU()
    x.baixa_links_ultima()

Ainda falta implementar a coleta dos atos propriamente dita.

Também implementarei coleta assíncrona.
