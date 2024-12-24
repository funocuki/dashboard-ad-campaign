from ._anvil_designer import GenderAgePlotTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import plotly.graph_objects as go


class GenderAgePlot(GenderAgePlotTemplate):
  def __init__(self, data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    men, women = data
    
    age = men['age']
    men = men['clicks']
    women = women['clicks']
    
    men_text = [f'age {a}: {click}' for a,click in zip(age, men)]
    wom_text = [f'age {a}: {click}' for a,click in zip(age, women)]
    
    men_bar = go.Bar(x=men, y=age, orientation='h',name='Men',text=age,textposition='auto')
    wom_bar = go.Bar(x=women, y=age, orientation='h',name='Women',text=age,textposition='auto')
    men_bar.insidetextfont.color = 'white'
    wom_bar.insidetextfont.color = 'white'
    
    self.plot_m.data = men_bar
    self.plot_m.layout.title.text = "Men"

    self.plot_w.data = wom_bar
    self.plot_w.layout.title.text = 'Women'
    self.plot_w.layout.xaxis.autorange = 'reversed'
    
    colorway = ['#00BCD4', '#8BC34A']
    from ..._plotly_templates import simple_white as template
    
    for i, plot in enumerate([self.plot_m, self.plot_w]):
      plot.layout.margin = dict(t=10, b=10, l=0,r=0)
      plot.layout.colorway = [colorway[i]]
      plot.layout.template = template
      plot.layout.yaxis.ticklen = 0
      plot.layout.yaxis.showline = False
      plot.layout.yaxis.showticklabels = False
      plot.layout.xaxis.ticklen = 0
      plot.layout.xaxis.showline = False
      plot.layout.xaxis.showticklabels = False
      plot.layout.title.xanchor = 'center'
      plot.layout.title.yanchor = 'top'
      plot.layout.title.x = 0.5

