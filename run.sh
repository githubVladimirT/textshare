export DOMAIN="0.0.0.0"
export PORT=7443
export CERT="./certs/cert.pem"
export KEY="./certs/key.pem"

hypercorn -b $DOMAIN:$PORT --certfile $CERT --keyfile $KEY server:app 