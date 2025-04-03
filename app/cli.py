import os
import click
from flask import Blueprint

bp = Blueprint('cli', __name__, cli_group=None)

@bp.cli.group()
def translate():
    """Translation and localization commands."""
    pass

@translate.command()
@click.argument('lang')
def init(lang):
    """Init a new language"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract command failed')

    if os.system(
            'pybabel init -i messages.pot -d app/translations -l ' + lang):
        raise RuntimeError('init command failed')
    
    os.remove('messages.pot')

@translate.command()
def update():
    """Update all langs"""
    if os.system('pybabel extract -F babel.cfg -k _l -o messages.pot .'):
        raise RuntimeError('extract cmd failed')

    if os.system('pybabel update -i messages.pot -d app/translations'):
        raise RuntimeError('update cmd failed')

    os.remove('messages.pot')

@translate.command()
def compile():
    """Compile all langs"""
    if os.system('pybabel compile -d app/translations'):
        raise RuntimeError('compile cmd failed')

