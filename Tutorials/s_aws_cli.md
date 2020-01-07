
# AWS Cli

## AWS Console

Link: https://693837262434.signin.aws.amazon.com/console
AccountID: 693837262434 
IAM user: alex
Password: standard

## Configure AWS accounts 
```
# for default user
aws configure
# for special user
aws configure --profile user2name
```

## CLI commands for S3

#### ls
```
# show content of bucket or bucket/prefix

aws s3 ls s3://conti-test
aws s3 ls s3://conti-test/audio

```
#### cp
```
# copy from s3 to local
aws s3 cp s3://conti-test/audio/fileOnBucket.csv LocalFile.csv

# copy from local to s3
aws s3 cp /Users/LocalFile.csv s3://conti-test/audio/fileOnBucket.csv 

```
#### rm
```

# delete file explicite
aws s3 rm s3://conti-test/audio/audio_test_file.csv

# delete all files in bucket or bucket/prefix 
aws s3 rm s3://conti-test/audio/ --recursive

# delete all but exclude some files
aws s3 rm s3://conti-test/audio/ --recursive --exclude "newAudio_*"
```

## CLI for EC2

#### EC2 Status
```
aws ec2 describe-instances --instance-ids $(IID) --output json  

# or drill down  into one JSON object
aws ec2 describe-instances --output json  | jq '.Reservations[0].Instances[0].State.Name'

# or get public dns name for ssh connection
aws ec2 describe-instances --instance-ids $(IID) --output json | jq '.Reservations[0].Instances[0].PublicDnsName' -r
```

#### Create and termiante instance
```
aws ec2 run-instances \
	--image-id ami-0cc293023f983ed53 \
	--count 1 \
	--instance-type r5.2xlarge \
	--key-name alex_aws_keys \
	--subnet-id subnet-54e36d2e \
	--security-group-ids sg-17469e7c \
	--user-data file://ec2_setup.sh  # contains setup instructions like apt-get and pip install commands


aws ec2 terminate-instances --instance-ids $(IID)

```


#### Start and Stop instance 
```
aws ec2 start-instances --instance-ids $(IID)

aws ec2 stop-instances --instance-ids $(IID)
```

#### SSH and SCP into instance
``` 
SSH_KEY=~/.ssh/my-ssh-key

# connect to server
ssh -i $(SSH_KEY) ec2-user@$(PUBLIC_DNS

# send script for execution to server
ssh -i $(SSH_KEY) ec2-user@$(PUBLIC_DNS) 'jupyter notebook --no-browser'

# forward port from server to local host
ssh -NfL 9999:localhost:8888 -i $(SSH_KEY) ec2-user@$(PUBLIC_DNS)

# copy file to server
	scp -i ~/.ssh/mykey $(HOME)/$(FILE) ec2-user@$(PUBLIC_DNS):/home/ec2-user/$(FILE)
``` 


## CLI for EMR

#### EMR Status
```
emr list-clusters --active --output json 
```
#### Create and termiante cluster
```
aws s3 cp emr_ec2_install.sh s3://conti-traceability/config/emr_ec2_install.sh
aws s3 cp /Users/aortner/git/Conti_traceability/python/pyspark  s3://conti-traceability/scripts/ --recursive
#aws s3 ls s3://conti-traceability/config/

# setup to create constantly running cluster !!!! expensive 
aws emr create-cluster  \
	--applications Name=Hadoop Name=Spark \
	--release-label emr-5.26.0  \
	--name "Spark4Conti_"${USER}  \
	--log-uri s3://conti-traceability/logs/install_log.log \
	--service-role EMR_DefaultRole \
	--instance-groups '[{"InstanceCount":2,"InstanceGroupType":"CORE","InstanceType":"r3.xlarge","Name":"Core Instance Group"},{"InstanceCount":1,"InstanceGroupType":"MASTER","InstanceType":"r3.xlarge","Name":"Master Instance Group"}]' \
	--ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetId":"subnet-54e36d2e","EmrManagedSlaveSecurityGroup":"sg-ba459dd1","EmrManagedMasterSecurityGroup":"sg-42469e29","KeyName":"alex_aws_keys"}'  \
	--configurations '[{"Classification":"spark","Properties":{"maximizeResourceAllocation":"true"}}]' \
	--bootstrap-actions Path=s3://conti-traceability/config/emr_ec2_install.sh,Name="Install python modules"  \
	--region eu-central-1 \
	--enable-debugging 
```

```
aws emr terminate-clusters --cluster-ids $(EMR_ID)
``` 
#### SSH and SCP into cluster
```
ssh -i $(SSH_KEY) hadoop@$(EMR_SSH_HOST)
```

## CLI for RDS

## CLI for Redshift
