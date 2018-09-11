from flask_assets import Environment, Bundle
from ..config.settings import STATIC_FOLDER, DEBUG
from os.path import join


# consolidated css bundle
css_bundle = Bundle('css/jquery*.css',
                    # 'css/font-awesome.min.css',
                    'css/bootstrap*.css',
                    'css/dataTables.min.css',
                    'css/style.css',
                    filters='cssmin', output='css/main.min.css')

# Compile CoffeeScript to JS.
# coffee_bundle = Bundle('coffee/init.js.coffee',
#                  filters='coffeescript', output='js/coffee.js')

# consolidated JavaScript bundle
js_bundle = Bundle('js/jquery.min.js',
                   'js/jquery-ui.min.js',
                   'js/lib/jquery.dataTables.min.js',
                   'js/bootstrap.min.js',
                   # coffee_bundle,
                   filters='rjsmin', output='js/main.min.js')


def init_assets(app):
    app.config['ASSETS_DEBUG'] = DEBUG
    webassets = Environment(app)
    webassets.config['PYSCSS_STATIC_ROOT'] = join(STATIC_FOLDER, 'scss')
    webassets.config['PYSCSS_STATIC_URL'] = join(STATIC_FOLDER, 'css/main.css')
    webassets.register('css', css_bundle)
    # webassets.register('coffee', coffee_bundle)
    webassets.register('js', js_bundle)
    # webassets.manifest = 'cache' if not app.debug else False
    # webassets.cache = not app.debug
    # webassets.debug = app.debug
