"""
This is a nice way to make imports user friendly. If this init py file was empty, which it could be, 
the StatsHelper import would look like this:
`from WenntechTutorialPackage.stats.stats import StatsHelper`
However, since we told python how to handle this import it will now look like:
`from WenntechTutorialPackage.stats import StatsHelper`. Just simplifies usability!
"""
from WenntechTutorialPackage.stats.stats import StatsHelper