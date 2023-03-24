# TextShare

### Working on python version 3.11


### Run:
```bash
docker build -t textshare .

docker run -v /home/user/textshare/posts:/home/textshare/posts -v /home/user/textshare/posts.old:/home/textshare/posts.old -v /home/user/textshare/logs:/home/textshare/logs --net=network --ip 172.18.0.113 textshare
```
