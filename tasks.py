import os
import glob

from invoke import task


current_path = os.getcwd()
path_migrate_test = '/app/test/migration/versions/'
files_migrate = glob.glob(current_path + path_migrate_test + '*.py')


@task
def run_coverage_test(c):
    c.run('rm -rf app/test/migration/database.db')
    if not files_migrate:
        c.run('alembic -n dev revision --autogenerate -m "migrate by invoke"')

    c.run('alembic -n dev upgrade head')
    c.run('coverage run --source=app -m unittest discover -s app/test/test_controllers/ -v')
    # c.run('coverage run --source=app -m unittest discover app/test/ -v')
