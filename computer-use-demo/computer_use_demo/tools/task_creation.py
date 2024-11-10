from .base import BaseAnthropicTool, ToolError, ToolResult
from anthropic.types.beta import BetaToolUnionParam


class TaskCreationTool(BaseAnthropicTool):
    name: str = "task_creation"

    def __init__(self):
        super().__init__()

    def to_params(self) -> BetaToolUnionParam:
        return {
            "name": self.name,
            "description": '''
                      A tool which is used to summarize actions from Slack conversations and create
                      Asana tasks based on the summarized actions''',
            "input_schema": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "The message received date"
                    },
                    "due_date": {
                        "type": "string",
                        "description": "The task's due date"
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["P0", "P1", "P2"],
                        "description": "The priority which the task should be updated to"
                    }
                },
                "required": ["date", "due_date"]
            }
        }

    async def __call__(self, date='', due_date='', priority='P1'):
        return ToolResult(
            output=f"""
                Open a browser if not opened.
                If browser is opened, check each tab to find slack tab. 
                If slack tab is there, Go to 'DMs'.
                If slack tab is not there, open slack 
                Make sure the slack is loaded, you may click
                'launch slack' or 'Use slack in' link. Once the slack is loaded, go to "DM", and check 
                messages I received after {date}, summarize these messages to action items. Then
                Open asana tab if not opened, go to 'My tasks' and create tasks from the summarization,
                and set task due date to {due_date} and priority to {priority}
            """
        )