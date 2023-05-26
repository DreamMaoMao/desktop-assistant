# desktop-assistant
桌面辅助工具

hotarea 鼠标移动到右上角出发win键，可以全屏触发
mouse_vlc vlc播放器左键单击暂停/播放

#放在supervisor上
/etc/supervisor/supervisord.conf
```
[unix_http_server]
file=/tmp/supervisor.sock

[supervisord]
logfile=/var/log/supervisor/supervisord.log
logfile_maxbytes=50MB
logfile_backups=10
loglevel=info
pidfile=/var/log/supervisor/supervisord.pid
nodaemon=false
minfds=1024
minprocs=200

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock

[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[include]
files = /etc/supervisor/conf.d/*.conf

[inet_http_server]
port=127.0.0.1:9001

```

/etc/supervisor/conf.d/hotarea.conf
```
[program:hotarea]
directory=~/project/desktop-assistant
command=python3 ~/project/desktop-assistant/hotarea.py
priority=100
autostart=true
autorestart=true
startsecs=5
startretries=3
stopwaitsecs=10
redirect_stderr=true
stdout_logfile=/var/log/hotarea.log
stdout_logfile_maxbytes=50MB
stdout_logfile_backups=10
stdout_capture_maxbytes=1MB

```