runlocal:
	clear && python manage.py runserver

deploy:
	clear && cd deploy_tools && fab deploy:host=root@46.101.242.181 --sudo-password=$(passwd)
