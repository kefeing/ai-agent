from .base import BaseAnthropicTool, ToolError, ToolResult
from anthropic.types.beta import BetaToolUnionParam


class TaskManagementTool(BaseAnthropicTool):
    """
    A task management tool dedicated to manage overdue asana tasks
    """
    name: str = "task_management"

    def __init__(self):
        super().__init__()

    def to_params(self) -> BetaToolUnionParam:
        return {
            "name": self.name,
            "description": '''
                  A tool which is used to manage Asana tasks like handling updating task priorities 
                  for overdue tasks''',
            "input_schema": {
                "type": "object",
                "properties": {
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
                "required": ["due_date", "priority"]
            }
        }

    async def __call__(self, due_date='', priority='P2'):
        return ToolResult(
            output=f'''
            Go to firefox and open asana if not open, otherwise go to the opened asana tab
            Click 'My tasks' on the left panel if you are not there, and go to task list if not there,
            find tasks whose due date is past {due_date}, then scroll the bar to find the priority column and then
            select the priority to {priority}
            '''
        )


