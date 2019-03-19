run_prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

build_prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build

build_run_prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build

up:
	docker-compose up

up_build:
	docker-compose up --build