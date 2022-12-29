import os
from dynaconf import Dynaconf

current_directory = os.path.dirname(os.path.realpath(__file__))

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[f"{current_directory}/settings.toml", f"{current_directory}/.secrets.toml"],
    environments=True,
    ENV_FOR_DYNACONF="development",
    # ENV_FOR_DYNACONF="production",
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

# with settings.using_env('settings.ENV_FOR_DYNACONF'):
#     print(settings.message)
#
# print(settings.ENV_FOR_DYNACONF)
# V = vars(settings)['_kwargs']
# print(V)
# for key, value in vars(settings)['_kwargs'].items():
#     print(f'{key} = {value}')
#
# for key, value in settings.items():
#     print(f'{key} = {value}')
