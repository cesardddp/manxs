json = [
    {
        "main": {
            "component_name": "main",
            "ID": 0,
            "texto": "",
            "html_template": '<div class="container-md marketing mt-4" > {{titulo}}{{banner}}{{texto_principal}}<hr class="m-5"><!-- card missão  -->{{card_missao}}<!-- card objetivo --><hr class="m-5">{{card_objetivo}}<!-- REDES SOCIAIS --><hr class="m-5"><!--Instagrams-->{{instagrams}}</div>',
            "titulo": {
                "component_name": "titulo",
                "ID": 1,
                "texto": "BIOGRAFIA",
                "html_template": '<h2 class="about" {{editor_macro(titulo_data,render_id)}}>{{texto}}</h2>',
            },
            "banner": {
                "component_name": "banner",
                "ID": 2,
                "foto": "bio_foto.jpeg",
                "alt": "Foto da Drag Ashilleyy em um vestido lindo, vermelho, perna esquerda de fora. Ela está ao centro, em um palco de teatro muito iluminado. Canto esquerdo inferior está o credito da foto: Paula Caldas 'videeverso'.",
                "html_template": '<div class="row featurette"><div class="col"><img loading=\'lazy\' src="{{url_for(\'static\', filename=\'imgs/\'+{{foto}})}}"{{editor_macro(banner_data,render_id)}} alt="{{alt}}" srcset=""class="my-5 bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="h-100"height="h-100"></div></div>',
            },
            "texto_principal": {
                "component_name": "texto_principal",
                "ID": 3,
                "texto": "\n        Desde 2016 o grupo Manxs vem despertando alegria e reflexão em seu público através da arte\n        Drag Queen, disseminando cultura, informação e arte com profissionalismo. O grupo é composto pelas\n        artistas Drags Queens\n        Ashilleyy Extravaganzza, Vikky e LuisAfF que são conhecidas por seus shows, sempre performáticos,\n        repletos de humor, dança, música e reflexões sociais. Iniciou seu trabalho cultural na cidade de Rio\n        Claro (interior do Estado de São Paulo) e hoje galga fronteiras compartilhando seu discurso artístico.\n        Já realizou apresentações em programas e atividades da Secretaria Municipal de Cultura de Rio Claro-SP,\n        UNESP campus de Rio Claro-SP, Sistema de Ensino COC e ETEC Armando Bayeux da Silva (Centro Paula Souza),\n        tendo como suas realizações mais simbólicas a abertura do show da Lia Clark em Rio Claro-SP no ano de\n        2018,\n        apresentação na posse de Iris Nogueira, coordenadora da Secretaria da Juventude de São Paulo no ano de\n        2018, o show principal de uma das noites do Festival Nacional INTERBio em 2019 e o Show (DVD Comentado)\n        intitulado Monta(Ação) em 2021. Recentemente, o grupo\n        Manxs vem investindo em seu trabalho autoral transpassando pelo gênero musical do Rock, lançando músicas\n        nas principais plataformas online de streaming e estão produzindo o seu primeiro álbum musical autoral.\n        Possui realizações notórias por meio de\n        editais contemplados, sendo elas:\n    ",
                "html_template": '<div class="row featurette bg-azul-branco"><div class="text-white bio-text fs-6 py-1 "><p class="" >{{texto}} </p>{{feitos}}{{texto_historico}}{{musicas}}{{texto_final}}</div></div>                ',
                "feitos": {
                    "component_name": "feitos",
                    "ID": 4,
                    "html_template": "<ul {{editor_macro(feitos_data,render_id)}}>{{li1}}{{li2}}{{li3}}{{li4}}{{li5}}{{li6}}{{li7}}</ul>",
                    "li1": {
                        "feito": "POIESIS (Programa de Qualificação em Arte - Dança) em 2019, que resultou no primeiro espetáculo de teatro musical LGBTQIA+ Drag Queen da cidade de Rio Claro-SP intitulado “O FIM”;",
                        "html_template": '<li class="list_triang"><p class="" {{editor_macro({\'ID\':loop.index},render_id)}}>{{feito}} </p></li>',
                    },
                    "li2": {
                        "feito": "Edital Nº1/2019 “Apoio a Projetos de Circulação de Espetáculos e Realização de Eventos Culturais no Município de Rio Claro - SP” em 2019, que resultou na elaboração do primeiro documento de registro histórico cultural da comunidade LGBTQIA+ de Rio Claro-SP;",
                        "html_template": '<li class="list_triang"><p class="" {{editor_macro({\'ID\':loop.index},render_id)}}>{{feito}} </p></li>',
                    },
                    "li3": {
                        "feito": 'Edital ProAC Nº14/2019 “Incentivo ao Desenvolvimento da Cultura Popular, Tradicional, Urbana, Negra, Indígena e Plural no Estado de São Paulo” em 2019, que resultou na circulação online e gratuito de oficinas de aprimoramento artístico de nível iniciante e do show (DVD) comentado intitulado "Monta(Ação)" ;',
                        "html_template": '<li class="list_triang"><p class="" {{editor_macro({\'ID\':loop.index},render_id)}}>{{feito}} </p></li>',
                    },
                    "li4": {
                        "feito": "POIESIS (Programa de Qualificação em Arte - Dança) em 2020, que resultou no espetáculo em videodança intitulado “Bem vindo ao Bailim” apresentado em evento online transmitido pelo Oficinas Culturais de São Paulo;",
                        "html_template": '<li class="list_triang"><p class="" {{editor_macro({\'ID\':loop.index},render_id)}}>{{feito}} </p></li>',
                    },
                    "li5": {
                        "feito": 'Edital ProAC Nº 04/2020 "Registro e licenciamento de espetáculos inéditos de Dança para difusão online - #CulturaEmCasa" em 2020. (NÃO REALIZADO DEVIDO ADVERSIDADES DA PANDEMIA);',
                        "html_template": '<li class="list_triang"><p class="" {{editor_macro({\'ID\':loop.index},render_id)}}>{{feito}} </p></li>',
                    },
                    "li6": {
                        "feito": "Lei Aldir Blanc em 2020, que possibilitou a apresentação parcial do repertório musical Monta(Ação) para a cidade de Rio Claro-SP, compondo o cronograma de atividades da Secretaria Municipal de Cultura;",
                        "html_template": '<li class="list_triang"><p class="" {{editor_macro({\'ID\':loop.index},render_id)}}>{{feito}} </p></li>',
                    },
                    "li7": {
                        "feito": 'Edital Cultural da Secretaria Municipal de Cultura de Rio Claro-SP intitulado "Semana Cultural - Tributo à Saúde", que resultou no show intitulado "Bem Me Quer, Mal Não Quero" em paralelo e apoio a campanha #SetembroAmarelo (Prevenção ao Suicídio) em 2021.',
                        "html_template": '<li class="list_triang"><p class="" {{editor_macro({\'ID\':loop.index},render_id)}}>{{feito}} </p></li>',
                    },
                },
                "texto_historico": {
                    "component_name": "texto_historico",
                    "ID": 5,
                    "texto": "HISTÓRICO: Manxs nasce de dentro do grupo de artes A'morasDance em Rio Claro-SP em 2016, idealizado por Luis Henrique (LuisAfF) e a Nina Rodrigues (Nina Poulain), sendo essa a primeira formação do grupo que até então performavam com Dança e Lip Sync. Em 2017, com a chegada de Pedro Marques (Ashilleyy Extravaganzza) em Rio Claro-SP, as Manxs decidem compor então um trio, passando a incluir o Canto como mais uma linguagem artística ao grupo, que seguiu com tal formação até março de 2018. Nina Poulain anuncia seu desligamento do grupo Manxs no final de 2017 e por meio de um acordo mutuo amigável, convida Leonardo Fonseca (Vikky) para ser a nova integrante. Vikky aceita o convite, decide deixar toda sua rotina e emprego em Valinhos-SP, se muda para Rio Claro-SP e dessa forma desde 2018, o trio oficial que compõe o título de Manxs é formado por: LuisAfF, Ashilleyy Extravaganzza e Vikky. À partir de 2019 o grupo Manxs passa a produzir um material musical autoral, visando a total independencia artística, para trabalhar com um conteúdo 100% original, condizendo assim com o discurso atrelado a missão do grupo. Como resultado desse empenho, hoje as Manxs possuem 4 músicas autorais e originais em todas as plataformas de streaming, sendo elas:",
                    "html_template": '<p class="" {{editor_macro(texto_historico_data,render_id)}}>{{texto_historico_data.texto}}</p>',
                },
                "musicas": {
                    "component_name": "musicas",
                    "ID": 6,
                    "html_template": "<ul {{editor_macro(musicas_data,render_id)}}>{{li1}}{{li2}}{{li3}}{{li4}}</ul>",
                    "li1": {
                        "link": "https://youtu.be/hlP-lESKS44",
                        "nome": "VELHA AMIGA",
                        "texto": " - Interprete: Manxs | Compositor: LuisAfF | Co-compositor: Davi Selingardi | Produção: Movie Mint. (2019) ONErpm Studios",
                        "html_template": '<li class="list_triang" {{editor_macro({\'ID\':loop.index},render_id)}}><a href="{{link}}"  style="color:#f69df1" target="_blank">{{nome}}</a>{{texto}}</li>',
                    },
                    "li2": {
                        "link": "https://youtu.be/5T0qEn23HYE",
                        "nome": "TÔ PLENA",
                        "texto": " - Interprete: Manxs | Compositor: Vikky e LuisAfF | Co-compositor: Chassi | Produção: Chassi. (2019) ONErpm Studios",
                        "html_template": '<li class="list_triang" {{editor_macro({\'ID\':loop.index},render_id)}}><a href="{{link}}"  style="color:#f69df1" target="_blank">{{nome}}</a>{{texto}}</li>',
                    },
                    "li3": {
                        "link": "https://youtu.be/OLs93xT5FEU",
                        "nome": "GOY",
                        "texto": " - Interprete: Manxs | Compositor: Vinicius Marques da Silva | Co-compositor: Nina Poulain e LuisAfF | Produção: Movie Mint. (2019) ONErpm Studios",
                        "html_template": '<li class="list_triang" {{editor_macro({\'ID\':loop.index},render_id)}}><a href="{{link}}"  style="color:#f69df1" target="_blank">{{nome}}</a>{{texto}}</li>',
                    },
                    "li4": {
                        "link": "https://youtu.be/b-_m3nnaESs",
                        "nome": "VISTA O CLOSE",
                        "texto": " - Interprete: Manxs | Compositor: LuisAfF | Co-compositor: Vikky e Ashilleyy Extravaganzza | Produção: Movie Mint. (2020) ONErpm Studios",
                        "html_template": '<li class="list_triang" {{editor_macro({\'ID\':loop.index},render_id)}}><a href="{{link}}"  style="color:#f69df1" target="_blank">{{nome}}</a>{{texto}}</li>',
                    },
                },
                "texto_final": {
                    "component_name": "texto_final",
                    "ID": 7,
                    "texto": 'O que era apenas um trio composto por três artistas Drag Queens, hoje é uma empresa independente, consistente e resistente, que vai além das ações das três integrantes que são porta vozes e a identidade visual do grupo. O grupo Manxs hoje conta com uma <a class="text-info" href="/servicos">equipe qualificada</a> e compromissada com o objetivo e missão da empresa.',
                    "html_template": "<p {{editor_macro(texto_final_data,render_id)}}>{{texto_final_data.texto|safe}}</p>",
                },
            },
            "card_missao": {
                "component_name": "card_missao",
                "ID": 8,
                "nome": "MISSÃO",
                "parte1": '"FAZER DO FERVO',
                "parte2": 'UM ATO POLÍTICO"',
                "img_link": "MISSÃO.jpeg",
                "alt": "",
                "html_template": '<div class="row bg-azul-branco py-2" style="border: 5px;border-radius: 0px 40px 0px 30px;"{{editor_macro(card_missao_data,render_id)}}>div class="col-md-7 order-md-2 text-white ">span class="d-block mx-auto text-center missao-titulo fs-3 mt-3">{{nome}} </span>span class="d-block mt-5 mx-auto col-9 missao-conteudo fs-1"><!-- TODO ASPAS GIGANTES -->p class="text-start">{{parte1}}</p>p class="text-end">{{parte2}}</p></span></div>div class="col-md-5 order-md-1">img loading=\'lazy\' src="{{url_for (\'static\', filename=\'imgs/\'+{{img_link}})}}" alt="" srcset=""class="bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="500"height="500"></div</div>',
            },
            "card_objetivo": {
                "component_name": "card_objetivo",
                "ID": 9,
                "nome": "OBJETIVO DO GRUPO",
                "parte1": '"FAZER DA ARTE UMA FERRAMENTA PARA VISIBILIDADE E O EMPODERAMENTO DA COMUNIDADE LGBTQIA+"',
                "img_link": "OBJETIVO.jpeg",
                "alt": "",
                "html_template": '<div class="row featurette bg-azul-branco py-2" {{editor_macro(card_objetivo_data,render_id)}}><div class="col-md-7 text-white"><span class="d-block mx-auto text-center missao-titulo fs-3 mt-3">{{nome}}</span><span class="d-block mt-5 mx-auto col-9 missao-conteudo fs-1"><p class="text-center">{{parte1}}</p></span></div><div class="col-md-5"><img loading=\'lazy\' src="{{url_for (\'static\', filename=\'imgs/\'+{{img_link}})}}"alt="{{alt}}" srcset=""class="mt-5 bd-placeholder-img bd-placeholder-img-lg featurette-image img-fluid mx-auto" width="500"height="500"></div></div>',
            },
            "instagrams": {
                "component_name": "instagrams",
                "ID": 10,
                "luisaff": {
                    "link": "https://www.instagram.com/oluisaff/",
                    "img": "luisaff.jpg",
                    "html_template": '<div class="d-flex-block col-sm-3 col-9 mb-1 rounded bg-azul-branco px-1 mx-auto py-3"{{editor_macro(instagrams_data,render_id)}}>><img loading=\'lazy\'src="{{url_for(\'static\', filename=\'imgs/\'+{{img}})}}" class="" alt="" width="140" height="140"><h2>LuisAfF</h2><a class="btn btn-redes btn-insta fs-5" href="{{link}}" target="_blank"role="button"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class=""viewBox="0 0 16 16"><pathd="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.9273.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.0483.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.3331.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.9160 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 168s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 00 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 02.389.007 3.232.046.78.035 1.204.1661.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.0473.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 01-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.4782.478 0 0 1-.92-.598 2.48 2.48 0 01-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.2330-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.241.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 00-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 05.334 2.667 2.667 0 0 1 0-5.334z" />            </svg></a>    </div>',
                },
                "ashilleyy": {
                    "link": "https://www.instagram.com/ash.extrava/",
                    "img": "ashilleyy.jpg",
                    "html_template": '<div class="d-flex-block col-sm-3 col-9 mb-1 rounded bg-azul-branco px-1 mx-auto py-3"{{editor_macro(instagrams_data,render_id)}}>><img loading=\'lazy\' src="{{url_for(\'static\', filename=\'imgs/\'+img)}}" class="" alt=""width="140" height="140"><h2>Ashilleyy</h2><a class="btn btn-redes btn-insta fs-5" href="{{link}}" target="_blank"role="button"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class=""viewBox="0 0 16 16"><pathd="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z" /></svg></a></div>',
                },
                "vikky": {
                    "link": "https://www.instagram.com/vikky_a_princesinha/",
                    "img": "vikky.jpg",
                    "html_template": '<div class="d-flex-block col-sm-3 col-9 mb-1 rounded bg-azul-branco px-1 mx-auto py-3"{{editor_macro(instagrams_data,render_id)}}>><img loading=\'lazy\' src="{{url_for(\'static\', filename=\'imgs/\'+img)}}" class="" alt=""width="140" height="140"><h2>Vikky</h2><a class="btn btn-redes btn-insta fs-5" href="{{link}}" target="_blank" role="button"><svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" fill="currentColor" class=""viewBox="0 0 16 16"><pathd="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z" /></svg></a></div>',
                },
                "html_template": '<div class="row text-center text-light">{{luisaff}}{{ashilleyy}}{{vikky}}',
            },
        }
    }
]

import re
from typing import Any


def create_html_from_component(component: dict):
    conteudo = component
    try:
        template_html: str = conteudo["html_template"]
    except TypeError as te:
        if isinstance(conteudo, str):
            return conteudo
        raise

    finds: list = re.findall(r"\{\{[a-z1-9]*[_]{0,1}[a-z1-9]*\}\}", template_html)
    # html = ""
    if conteudo.get("type", False) == "ul":
        ul_inner_html = ""
        for e in conteudo["li"]["items"]:
            ul_inner_html += create_html_from_component(
                {
                    "html_template": conteudo["li"]["html_template"],
                    re.findall(
                        r"\{\{[a-z1-9]*[_]{0,1}[a-z1-9]*\}\}",
                        conteudo["li"]["html_template"],
                    )
                    .pop()
                    .replace("{{", "")
                    .replace("}}", ""): e,
                }
            )

            print("asdf")
        return template_html.replace("{{items}}", ul_inner_html)

    for e in finds:
        nome_componente = e.replace("{{", "").replace("}}", "")
        try:
            componente: dict = conteudo[nome_componente]
        except KeyError as ke:
            breakpoint()
        else:
            template_html = template_html.replace(
                e, create_html_from_component(componente)
            )
            # html
    return template_html
    print()
    # if "{{" in html:


for item in json:
    result = create_html_from_component(item.popitem()[1])
    print(result)
