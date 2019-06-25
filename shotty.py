import boto3
import click
sesssion = boto3.Session (profile_name ="shotty")
ec2= session.resource("ec2")
@click.command()
for i in ec2.instances.all():
	print(i)
	print(','.join((
		i.id,
		i.instance_type,
		i.placement['Availability Zone'],
		i.state['Name']
		i.public_dns_name)))
