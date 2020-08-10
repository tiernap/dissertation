# jupyter server configurations

c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root=True
c.NotebookApp.port = {{ jupyter_port }}
c.NotebookApp.password = '{{ jupyter_pass }}'
c.NotebookApp.token = '{{ jupyter_token }}'
