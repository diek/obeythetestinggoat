from selenium import webdriver

browser = webdriver.Firefox()

# Justin needs to keep track of stuff, he checks out the homepage
browser.get('http://localhost:8080')

# he notices the page title and header mention to-do lists
assert 'To-Do' in browser.title
print("complete")
# He is invited to enter a to-do item straight away

# He types "Buy peacock feathers" into a text box (Edith's hobby
# is tying fly-fishing lures)

# When He hits enter, the page updates, and now the page lists
# "1: Buy peacock feathers" as an item in a to-do list

# There is still a text box inviting her to add another item. He
# enters "Use peacock feathers to make a fly" (Edith is very methodical)

# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then He sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# He visits that URL - her to-do list is still there.

# Satisfied, He goes back to sleep
browser.quit()
