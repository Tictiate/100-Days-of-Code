from data_gathering import souping_data
from data_entering import FormFiller

site = souping_data()
links, addresses, prices = site.collect_data()

form = FormFiller()
# form.fill_form(links, addresses, prices)
