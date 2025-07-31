import boto3

def lambda_handler(event, context):
    eks=boto3.client('eks')
    cluster_name = event['cluster_name']
    nodegroup_name = event['nodegroup_name']
    if event['action'] == 'scale_up':
        scale_up_nodegroup(eks,cluster_name,nodegroup_name)
    elif event['action'] == 'scale_down':
        scale_down_nodegroup(eks,cluster_name,nodegroup_name)

def scale_up_nodegroup(eks,cluster_name,nodegroup_name):
    try:
        if cluster_name == 'my-eks':
            scaling_response = eks.update_nodegroup_config(
            clusterName = cluster_name,
            nodegroupName = nodegroup_name,
            scalingConfig = {
                'minSize': 1,
                'maxSize': 3,
                'desiredSize': 2
            })
            print(scaling_response)
        else:
            print(f"Cluster name '{cluster_name}' does not match 'my-eks'. Skipping scaling.")
    except Exception as e:
        print(e)

def scale_down_nodegroup(eks, cluster_name, nodegroup_name):
    try:
        if cluster_name == 'my-eks':
            scaling_response = eks.update_nodegroup_config(
            clusterName = cluster_name,
            nodegroupName = nodegroup_name,
            scalingConfig = {
                'minSize': 0,
                'maxSize': 1,
                'desiredSize': 0
            })
            print(scaling_response)
        else:
            print(f"Cluster name '{cluster_name}' does not match 'my-eks'. Skipping scaling.")
    except Exception as e:
        print(e)

