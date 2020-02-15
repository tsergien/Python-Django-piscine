python3 -m venv my_env
source my_env/bin/activate
echo "Pip version: "
pip3 -V
# mkdir -p local_lib
pip3 install --quiet --upgrade --disable-pip-version-check  --target=local_lib --ignore-installed git+https://github.com/jaraco/path.git --log installing_logs.log

python3 my_program.py
deactivate
