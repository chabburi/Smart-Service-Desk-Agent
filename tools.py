from strands import tool
import boto3
import json
from datetime import datetime

# Tool 1: Query Bedrock Knowledge Base using AWS Bedrock Runtime
@tool
def query_knowledge_base(query: str) -> str:
    """
    Answers a user's device support query using the Bedrock Knowledge Base.
    """
    bedrock_agent_runtime = boto3.client("bedrock-agent-runtime", region_name="us-east-1")
    response = bedrock_agent_runtime.retrieve_and_generate(
    input= {
        "text": query
    },
    retrieveAndGenerateConfiguration= {
        "knowledgeBaseConfiguration": {
            "knowledgeBaseId": "TCWAN43E6O",
            "modelArn": "us.amazon.nova-premier-v1:0"
        },
        "type": "KNOWLEDGE_BASE"
    }
    )
    return response["output"]["text"]

# Tool 2: Fetch ticket status from DynamoDB
@tool
def get_ticket_status(user_id: str) -> str:
    """
    Fetches the ticket status of a user from DynamoDB based on user_id.
    """
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table("Ticket_Status")  # replace with actual table name

    response = table.get_item(Key={"user_id": user_id})
    item = response.get("Item")

    if not item:
        return "No ticket found for the given user ID."

    return (
        f"Hi {item['name']}, your ticket status is '{item['ticket_status']}' "
        f"for the issue '{item['issue']}' on your {item['device']}. "
        f"ETA: {item['eta']}. Last Updated: {item['LastUpdated']}."
    )
