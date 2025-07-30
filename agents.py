from strands import Agent
from tools import query_knowledge_base
from tools import get_ticket_status
import re


def clean_strands_response(question):
    """
    Extracts only the final answer, removing <thinking> tags and tool thoughts.
    """
    support_agent = Agent(
    name="SupportDeskAgent",
    model="us.amazon.nova-premier-v1:0",
    system_prompt=(
        """You are a smart electronic support desk agent. "
        Answer queries using the knowledge base and check ticket status from the database. 
        If a user asks about an issue with a device, use the knowledge base. 
        If they ask about their ticket status, use the DynamoDB tool.
        Please do not provide any 'thinking' or process you are following just only return the final answer"""
    ),
    tools=[query_knowledge_base, get_ticket_status]
    )
    agent_response = support_agent(question,stream=False)
    content = agent_response.message['content'][0]['text']
    # Remove <thinking>...</thinking>
    cleaned = re.sub(r"<thinking>.*?</thinking>", "", content, flags=re.DOTALL).strip()
    return cleaned
    
