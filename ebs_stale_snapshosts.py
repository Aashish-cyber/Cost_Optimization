import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')

    # Fetch all EBS snapshots
    snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])['Snapshots']
    
    # Fetch all active EC2 instances (running or stopped)
    instances = ec2_client.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running', 'stopped']
            }
        ]
    )['Reservations']
    
    # Extract list of active volumes
    active_volumes = set()
    for reservation in instances:
        for instance in reservation['Instances']:
            for block_device in instance['BlockDeviceMappings']:
                active_volumes.add(block_device['Ebs']['VolumeId'])

    # Find and delete stale snapshots
    for snapshot in snapshots:
        volume_id = snapshot.get('VolumeId')
        if volume_id and volume_id not in active_volumes:
            print(f"Deleting snapshot {snapshot['SnapshotId']} for volume {volume_id}")
            ec2_client.delete_snapshot(SnapshotId=snapshot['SnapshotId'])

    return {
        'statusCode': 200,
        'body': f"Checked {len(snapshots)} snapshots. Deleted stale ones."
    }
