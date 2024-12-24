from ._anvil_designer import CountryPlotTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class CountryPlot(CountryPlotTemplate):
  def __init__(self, data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    
    countries = data['region']
    clicks = data['clicks']
    
    pie = go.Pie(values=clicks, names=countries, text=countries, textposition='auto',
                 marker=dict(line=dict(width=3, color='white')),
                 textinfo='text+value'
                )
    pie.insidetextfont.color = 'white'
    pie.hole = .2
    pie.pull = [0, 0, .1, .1]
    self.plot.data = pie
    
    self.plot.layout.colorway = ['#8BC34A', '#00BCD4']
    
    from ..._plotly_templates import simple_white as template
    self.plot.layout.template = template
    self.plot.layout.margin = dict(t=10, b=10, l=0,r=0)
    self.plot.layout.showlegend = False

