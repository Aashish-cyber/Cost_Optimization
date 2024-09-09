## AWS EBS Snapshot Cleaner

This project contains an AWS Lambda function that identifies and deletes stale EBS snapshots that are no longer associated with any active EC2 instance, effectively optimizing AWS storage costs.

## Overview

Over time, unused or "stale" EBS snapshots can accumulate and result in unnecessary storage costs. This Lambda function automatically checks all EBS snapshots owned by the account and verifies if the associated EBS volume is still attached to an active EC2 instance. If it finds that the snapshot’s volume is no longer associated with any instance, the function deletes the snapshot to free up storage space.

## Features


Identifies EBS snapshots not linked to any active EC2 instance.

Automatically deletes stale EBS snapshots to reduce storage costs.

Periodic cleanup using AWS CloudWatch Events to automate cost optimization.

Easy-to-deploy Lambda function using AWS SDK (boto3).

## Prerequisites


AWS account with necessary permissions.

AWS Lambda.

IAM Role with the following policies:

AmazonEC2ReadOnlyAccess (for reading EC2 instances and volumes)

AmazonEC2FullAccess (for managing EBS snapshots)

AWSLambdaBasicExecutionRole (for Lambda logging)

## Setup

## Step 1: Deploy Lambda Function

Log into your AWS Management Console.

Navigate to AWS Lambda and create a new function:

Function name: DeleteStaleSnapshots

Runtime: Python 3.9 (or your preferred version)

Assign the function the IAM Role mentioned in the prerequisites.

Copy and paste the Python code into the function editor.

## Step 2: Configure CloudWatch Event Rule

Go to AWS CloudWatch → Rules → Create rule.

Select Event Source as Schedule.

Choose a period (e.g., daily) to trigger the Lambda function.

Set the target as your newly created Lambda function (DeleteStaleSnapshots).

## Step 3: Test the Function

Manually invoke the Lambda function by selecting Test in the Lambda console.

Review logs in CloudWatch to confirm the snapshots have been deleted.

## Step 4: Automate the Process

Ensure that CloudWatch is triggering the function on a schedule (daily or weekly) to regularly clean up stale snapshots and optimize costs.
