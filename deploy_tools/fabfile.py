from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run, sudo
import random

REPO_URL = 'https://github.com/atala15/learning_log.git'
# NOTE: fab deploy:host=root@46.101.242.181 --sudo-password=PASSWORD  
# NOTE : ssh root@46.101.242.181
DEBUG = True

def deploy():
    site_folder=f'/{env.user}/sites/{env.host}'
    
    source_folder = site_folder + '/source'
    env['SITENAME'] = env.host

    _install_requred_applications(site_folder)
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_virtualenv(source_folder)
    _update_static_files(source_folder)
    _update_database(source_folder)
    _configure_nginx_and_gunicorn(source_folder)
    _start_up(source_folder)

def _install_requred_applications(site_folder):
    sudo('apt-get update --assume-yes')
    sudo('apt-get install git --assume-yes')
    # sudo('apt-get --assume-yes install nginx')
    # sudo('systemctl start nginx')
    sudo('apt-get install python3-venv --assume-yes')

def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run(f'mkdir -p {site_folder}/{subfolder}')

def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):  
        run(f'cd {source_folder} && git fetch') 
    else:
        run(f'git clone {REPO_URL} {source_folder}') 
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run(f'cd {source_folder} && git reset --hard {current_commit}') 

def _update_settings(source_folder, site_name):
    # settings_path = source_folder + '/learning_log/settings.py'
    # sed(settings_path, "DEBUG = .+$", f"DEBUG = {DEBUG}")
    # sed(settings_path,
    #     'ALLOWED_HOSTS = .+$',
    #     f'ALLOWED_HOSTS = ["{site_name}"]'
    # )
    # secret_key_file = source_folder + '/learning_log/secret_key.py'
    # if not exists(secret_key_file):
    #     chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    #     key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
    #     append(secret_key_file, f'SECRET_KEY = "{key}"')
    #     env['DJANGO_SECRET_KEY'] = key
    # append(settings_path, '\nfrom .secret_key import SECRET_KEY')
    pass

def _update_virtualenv(source_folder):
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirements.txt')

def _update_static_files(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../virtualenv/bin/python manage.py collectstatic --noinput'
    )

def _update_database(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../virtualenv/bin/python manage.py migrate --noinput'
    )

def _configure_nginx_and_gunicorn(source_folder):
    # sudo('rm -f /etc/nginx/sites-available/*')
    # sudo('rm -f /etc/nginx/sites-enabled/*')
    # sudo('rm -f /etc/systemd/system/gunicorn*')
    # sudo(f'sed s/SITENAME/{env.host}/g '
    #     f' {source_folder}/deploy_tools/nginx.template.conf '
    #     f' | tee /etc/nginx/sites-available/{env.host} '
    # )
    # sudo(f' ln -sfn /etc/nginx/sites-available/{env.host} '
    #     f' /etc/nginx/sites-enabled/{env.host} ',
    # )
    # sudo(f'sed s/SITENAME/{env.host}/g '
    #     f' {source_folder}/deploy_tools/gunicorn-systemd.template.service '
    #     f' |  tee /etc/systemd/system/gunicorn-{env.host}.service '
    # )
    # sudo(' systemctl daemon-reload && '
    #     ' systemctl reload nginx && '
    #     f' systemctl enable gunicorn-{env.host} &&'
    #     f' systemctl start gunicorn-{env.host}',
    # )
    pass
    # def _configure_email_server(source_folder):

def _start_up(source_folder):
    run(
        f'cd {source_folder}'
        ' && ../virtualenv/bin/python manage.py runserver'
    )



