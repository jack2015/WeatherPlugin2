from distutils.core import setup
import setup_translate

pkg = 'Extensions.WeatherPlugin2'
setup (name = 'enigma2-plugin-extensions-weatherplugin2',
       version = '2.1',
       description = 'Weather Plugin 2',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['weather.png', '*/*.png', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
