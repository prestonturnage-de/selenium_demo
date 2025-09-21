build:
	docker compose build

test: build
	docker compose up tests

start:
	docker compose up -d selenium_chrome

stop:
	docker compose down selenium_chrome
