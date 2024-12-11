import boto3

# Initialize a session using Amazon CloudWatch
session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY',
    aws_secret_access_key='YOUR_SECRET_KEY',
    region_name='YOUR_REGION'
)

cloudwatch = session.client('cloudwatch')

# Function to get CloudWatch metrics
def get_metrics(namespace, metric_name, dimensions):
    response = cloudwatch.get_metric_statistics(
        Namespace=namespace,
        MetricName=metric_name,
        Dimensions=dimensions,
        StartTime=datetime.utcnow() - timedelta(minutes=10),
        EndTime=datetime.utcnow(),
        Period=60,
        Statistics=['Average']
    )
    return response['Datapoints']

# Example usage
metrics = get_metrics(
    namespace='AWS/EC2',
    metric_name='CPUUtilization',
    dimensions=[{'Name': 'InstanceId', 'Value': 'YOUR_INSTANCE_ID'}]
)
print(metrics)
