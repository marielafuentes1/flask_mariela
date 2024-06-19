from . import db
from flask import Blueprint, render_template



bp = Blueprint('category',__name__,url_prefix="/categorys")

@bp.route("/")
def category():
   consulta = """
       SELECT name FROM category
       ORDER BY name;
     """
   con = db.get_db()
   res = con.execute(consulta)
   lista_category = res.fetchall()
   pagina = render_template("category.html", categorias = lista_category)
   return pagina