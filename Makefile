ENV = env
LINUX_ACTIVATE_PATH = $(ENV)/bin/activate

.PHONY: build_environment
build_environment: clean_linux
	virtualenv $(ENV)
	sh -c '. $(LINUX_ACTIVATE_PATH); pip install -r requirements.txt'
	echo "initialization complete"

.PHONY: clean_linux
clean_linux:
	if [ -d "$(ENV)" ]; then rm -rf $(ENV); fi
	if [ -f .coverage ]; then rm .coverage; fi
	if [ -d "./htmlcov" ]; then rm -rf ./htmlcov; fi
	if [ -d "./.tox" ]; then rm -rf ./.tox; fi

