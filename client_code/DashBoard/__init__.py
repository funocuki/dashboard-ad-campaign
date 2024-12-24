from ._anvil_designer import DashBoardTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class DashBoard(DashBoardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    summary, age_gender, by_country, time_of_day = anvil.server.call('get_data')
    
    self.small_card_1.heading = f"£{summary['amount spent (gbp)']} spent"
    self.small_card_1.subheading = f"£{summary['cpc (cost per link click)']:.2f} cost per click"
    self.small_card_2.heading = f"{summary['clicks']:,} total clicks"
    self.small_card_2.subheading = f"{summary['ctr (link click-through rate)']:.2f}% click through rate"
    self.small_card_3.heading = f"{summary['reach']:,} reach"
    self.small_card_3.subheading = f"{summary['frequency']:.2f} frequency per person"
    self.small_card_4.heading = f"{summary['page likes']} page likes"
    self.small_card_4.subheading = f"{summary['page engagements']:,} page engagements"
    
    
    
    from .GenderAgePlot import GenderAgePlot
    from .CountryPlot import CountryPlot
    from .TimeOfDayPlot import TimeOfDayPlot
       
    
    self.gender_card.add_component(GenderAgePlot(data=age_gender))
    self.location_card.add_component(CountryPlot(data=by_country))
    self.time_card.add_component(TimeOfDayPlot(data=time_of_day))