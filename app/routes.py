from flask import Flask, render_template, url_for, Response, request, redirect
from app import app
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from app.models import webscrapping, afd


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/intro')
def intro():
  return render_template('intro.html')
@app.route('/de')
def de():
  return render_template('de.html')
@app.route('/automato', methods = ['POST', 'GET'])
def automatofinito():
  if request.method == 'GET':
    return render_template('automato.html')
  else:
    out = afd.automato(request.form['fSequencia'])
    return render_template('automato.html', resultado = out)
@app.route('/Final')
def final():
  return render_template('Final.html')
@app.route('/Webscrapping')
def webs():
  return render_template('Webscrapping.html')
@app.route('/imgPlot')
def plot_png():
  fig = webscrapping.create_figure()
  output = io.BytesIO()
  FigureCanvas(fig).print_png(output)
  return Response(output.getvalue(), mimetype='image/png')

if __name__ == '__main__':
  app.run(debug=True)
 