from sys import prefix
from flask import Blueprint, render_template, request
# from mongo import configure_app as mongo_config, find_all,update
from conteudo import ( historia, aulas, oficinas, videos_lista, cursos,
    redes_sociais_componente,
)

RENDER_ID = True

editor_bp = Blueprint("editor",__name__,url_prefix='/editor')


# @editor_bp.get('/')
# def biografia():

#     biografia_data:dict = find_all("biografia")

#     return render_template(
#         "biografia.html",
#         redes_sociais_componente=redes_sociais_componente,
#         biografia_data=biografia_data,
#         render_id=RENDER_ID
#     )


# @editor_bp.patch('/edit/<int:pk>')
# def edit(pk):
#     data:dict = request.get_json() or {}
#     text:str = data.get('data',"")
#     if text :
#         update("biografia",pk,)
#     breakpoint()
#     return "",200