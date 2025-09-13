from App.Utilities.Url import Url


route = Url.current_route()


if route == '/colors/blue':
    'template/colors/blue.html'

if route == '/colors/green':
    'template/colors/green.html'

if route == '/colors/red':
    'template/colors/red.html'

