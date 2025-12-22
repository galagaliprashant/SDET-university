#Class to define the browsers
#open the browser
# get the details of browser's link

class Browser:
  def __init__(self,browser_name,browser_version):
   self.browser_name = browser_name
   self.browser_version = browser_version

  def open_browser(self):
   print(f"The browser opened name is {self.browser_name}")

  def display_browser_version(self):
   print(f"The browser version is {self.browser_version}")


browser_1 = Browser("chrome", "4.5.1") # Changed version to a string for typical browser versions

browser_1.open_browser()
browser_1.display_browser_version()

browser_2 = Browser("safari", "4.5.1") # Changed version to a string for typical browser versions
browser_2.open_browser()
browser_2.display_browser_version()