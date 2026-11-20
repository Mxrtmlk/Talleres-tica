# Taller sumativo 4 (ETI195) — qué falta y con qué

Viernes 20-11-2026. Entrega en Canvas hoy a las 23:59.
Repo: https://github.com/Mxrtmlk/Talleres-tica

## 1. Dónde estamos (comprobado el 20-11)

| Cosa | Estado | Cómo se comprobó |
|---|---|---|
| Notebook con P1, P2 y P3, ejecutado | Listo y subido (`Taller_sumativo_4.ipynb`) | Se abrió el JSON: 20 celdas, 3 celdas de código con salida, 0 errores |
| Página (`docs/index.html`) | Lista y subida, con el texto de Vicente en «Qué muestra el gráfico» | Cifras recalculadas sobre `casen.csv`: 23,8 % (7.060 de 29.645), 16,6 % (30.432 de 182.826), diferencia 7,17 puntos |
| GitHub Pages | **No activado**. Sin eso la página no existe en internet | Quien subió los archivos tiene permiso de escritura, no de administrador |
| URL esperada | https://mxrtmlk.github.io/Talleres-tica/ | **No verificada**: solo se sabrá cuando se active |

## 2. Qué falta, por persona

### Martín (dueño del repo): activar GitHub Pages

1. Repo → **Settings** → **Pages**.
2. En *Build and deployment*: **Deploy from a branch**.
3. Rama `main`, carpeta `/docs`, **Save**.
4. Esperar uno o dos minutos y abrir https://mxrtmlk.github.io/Talleres-tica/.
5. Comprobar que se ven el texto y los dos gráficos, y avisar.

### Vicente

- Releer P1 y P3 en el notebook, que son lo evaluado. Tres cosas que mirar:
  1. P1, párrafo 3: «es plausible que se priorizara el objetivo de medir la pobreza multidimensional…» es una hipótesis y está dicha como tal. Si no quiere arriesgarla, se borra esa oración.
  2. P3, la propuesta (mesas de codiseño, k-anonimato, acceso diferenciado): confirmar que es lo que quiere defender.
  3. Los veredictos de la tabla de P3: No / A medias / A medias / Sí / A medias / A medias.

### Martín y Fernando (no se tocó)

- P4 a P7 del notebook.
- Declaración de uso de IA.
- Re-ejecutar todas las celdas, exportar a PDF y revisar.
- Entregar en Canvas, antes de las 23:59: `.ipynb`, PDF y link al repo (el de la página solo si ya la abrió alguien).

## 3. Archivos

```
Taller_sumativo_4.ipynb     notebook con P1, P2, P3 (ejecutado)
docs/index.html             la página (es lo que publica Pages)
docs/style.css              estilos (claro y oscuro, sirve en teléfono)
docs/img/                   los dos gráficos
scripts/grafico_prop.py     genera el gráfico de porcentajes
LEEME-taller4.md            este documento
```

`casen.csv` (73 MB) no está en el repo. Está en el Drive del curso, id `1DQsXd6hThmoROcqSqVlBPEO-jb0joKj9`, y el notebook lo descarga solo.

Para volver a generar el gráfico de porcentajes (necesita `pandas` y `matplotlib`):

```powershell
python scripts/grafico_prop.py ruta\a\casen.csv docs/img/pobreza-porcentaje-pueblo-indigena.png
```

## 4. Lo que NO se pudo comprobar (declarado)

- **Pages:** no está activo, así que la URL de la página no se ha abierto nunca.
- **Enlace de OHCHR:** ohchr.org responde 403 a las herramientas usadas. El año (2018) se confirmó en el PDF («© United Nations 2018»), pero el enlace tal como está escrito no se abrió.
- **Cuestionario y libros de códigos de Casen:** no se revisaron. P1 y P3 se basan en tres documentos (documento metodológico, ficha técnica y nota de uso) y en el dataset; el texto lo dice.
- **Criterio de las 42 variables** del dataset del curso (la base pública tiene 877): no está documentado en el material revisado. Queda como hipótesis, escrita así.
- **Formativo del curso:** trae mal los editores de Milan (2017). En el notebook se usaron los de la editorial (Pickard y Yang).
- **Porcentajes de la página:** son sobre los registros del dataset del curso, sin factor de expansión; no son estimaciones de la población.
