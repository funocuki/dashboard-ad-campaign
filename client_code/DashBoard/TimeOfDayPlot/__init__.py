from ._anvil_designer import TimeOfDayPlotTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

import plotly.graph_objects as go

class TimeOfDayPlot(TimeOfDayPlotTemplate):
  def __init__(self,data=None, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    times = data['time of day']
    data = data['clicks']
    
    bar = go.Bar(y=data, x=times, text=data, textposition='inside')
    bar.insidetextfont.color = 'white'
    
    self.plot.data = bar
    self.plot.layout.colorway = ['#00BCD4', '#8BC34A']
    
    from ..._plotly_templates import simple_white as template
    self.plot.layout.template = template

    self.plot.layout.margin = dict(t=10, b=10, l=0,r=0)
    self.plot.layout.yaxis.ticklen = 0
    self.plot.layout.yaxis.showline = False
    self.plot.layout.yaxis.showticklabels = False
    self.plot.layout.xaxis.ticklen = 0
