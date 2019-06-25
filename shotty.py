import boto3
import click
sesssion = boto3.Session (profile_name ="shotty")
ec2= session.resource("ec2")
@click.command()
@click.option('--project',default=None, help ="Only instances for project(tag Project:<name>)")
def list_instances(project):
	"list ec2 instances "
	instances=[]
	if project:
		filters = [{'Name':'tag:Project','Values':[project]}]
		instances = ce2.instances.filter(Filter = filters)
	else:
		instances = ec2.instances.all()
	for i in ec2.instances.all():
	print(i)
	
	
	for i in instances:
		tags ={t['Key']:t['Value'] for t in i.tag or []}
		print(','.join((
			i.id,
			i.instance_type,
			i.placement['Availability Zone'],
			i.state['Name']
			i.public_dns_name
			tags.get('Project','<no project>')))
		      
		      
	return
		      
if __name__ = ='__main__':
		      list_instances()
