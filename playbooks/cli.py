import click
import subprocess
import os
from pathlib import Path
import colorama as c
from simple_term_menu import TerminalMenu

@click.group()
def vd():
    """vps deployer"""


@vd.command('deploy')
@click.argument('app', required=False)
@click.option('--ssh-key', '-k', help='SSH key to use for deployment')
def deploy(app : str, ssh_key : str):
    """Deploy an app."""
    click.echo()
    if not app:
        apps = _list_apps()
        terminal_menu = TerminalMenu(
            apps,
            title="Select an app to deploy",
            menu_cursor_style=("fg_blue", "bold"),
            menu_highlight_style=("bg_red", "fg_yellow")
        )
        selected_index = terminal_menu.show()
        app = apps[selected_index]
        click.echo(f"{c.Fore.BLUE}Selected app: {c.Style.BRIGHT}{app}{c.Style.RESET_ALL}{c.Fore.RESET}")
    elif app not in _list_apps():
        click.echo(c.Fore.RED + 'App not found.' + c.Fore.RESET)
        click.echo(c.Fore.RED + 'Run "vd apps" to see available apps.' + c.Fore.RESET)
        return
    click.echo()
    click.echo(c.Fore.BLUE + "Deploying " + c.Style.BRIGHT + app + c.Style.RESET_ALL + c.Fore.BLUE + '...' + c.Fore.RESET)
    cmd = ['ansible-playbook', f'playbooks/apps/{app}.yml']
    if ssh_key:
        cmd += ['--private-key', ssh_key]
    click.echo()
    click.echo(c.Style.DIM + '  > ' + ' '.join(cmd) + c.Style.RESET_ALL)
    rc = subprocess.call(cmd)
    click.echo()
    exit(rc)


def _list_apps():
    apps = []
    for app in os.scandir(Path(__file__).parent / 'apps'):
        if app.name.endswith('.yml'):
            apps.append(app.name[:-4])
    return apps

@vd.command('apps')
def list_apps():
    """List available apps."""
    # available apps are in the apps directory
    click.echo()
    click.echo(c.Style.BRIGHT + 'Available apps:' + c.Style.RESET_ALL)
    click.echo()
    for app in _list_apps():
            click.echo(c.Fore.CYAN + "- " + app + c.Fore.RESET)
    
    click.echo()

@vd.command('init')
def init():
    """Initilize vps server."""
    click.echo()
    click.echo(c.Fore.BLUE + "Initializing server..." + c.Fore.RESET)
    click.echo()
    click.echo(c.Style.DIM + '  > ' + 'ansible-playbook playbooks/init_vps.yml' + c.Style.RESET_ALL)
    rc = subprocess.call(['ansible-playbook', 'playbooks/init_vps.yml'])
    click.echo()
    exit(rc)