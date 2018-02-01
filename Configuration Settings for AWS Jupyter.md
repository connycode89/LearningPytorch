Guide to setting up Jupyter on AWS
https://kenophobio.github.io/2017-01-10/deep-learning-jupyter-ec2/

# Launching AWS instance
# create security group 
aws ec2 create-security-group --group-name JupyterSecurityGroup --description "My Jupyter security group"

# add security group rules 
aws ec2 authorize-security-group-ingress --group-name JupyterSecurityGroup --protocol tcp --port 8888 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name JupyterSecurityGroup --protocol tcp --port 22 --cidr 0.0.0.0/0
aws ec2 authorize-security-group-ingress --group-name JupyterSecurityGroup --protocol tcp --port 443 --cidr 0.0.0.0/0

# launch instance 
aws ec2 run-instances --image-id ami-41570b32 --count 1 --instance-type p2.xlarge --key-name <YOUR_KEY_NAME> --security-groups JupyterSecurityGroup

# Running Jupyter on localhost, port 8888
# SSH
ssh -i "your_pem_file.pem" ec2-user@ec2*.compute.amazonaws.com -L 8888:127.0.0.1:8888

# Configure Jupyter Server
jupyter notebook --generate-config
key=$(python -c "from notebook.auth import passwd; print(passwd())")

# Make sure to answer all questions:
cd ~
mkdir certs
cd certs
certdir=$(pwd)
openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout mycert.key -out mycert.pem

cd ~
sed -i "1 a\
c = get_config()\\
c.NotebookApp.certfile = u'$certdir/mycert.pem'\\
c.NotebookApp.keyfile = u'$certdir/mycert.key'\\
c.NotebookApp.ip = '*'\\
c.NotebookApp.open_browser = False\\
c.NotebookApp.password = u'$key'\\
c.NotebookApp.port = 8888" .jupyter/jupyter_notebook_config.py

# Create notebooks directory and run Jupyter
mkdir notebooks
cd notebooks
jupyter notebook