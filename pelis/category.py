from . import db
from flask import Blueprint, render_template

bp= Blueprint('category', __name__,url_prefix="/lenguaje")


@bp.route('/')
def category():
   consulta = """SELECT name FROM language ORDER BY name;
   """
   con = db.get_db()
   res = con.execute(consulta)
   lista_categorys = res.fetchall()
   pagina = render_template('category.html', categorys=lista_categorys)

   return pagina