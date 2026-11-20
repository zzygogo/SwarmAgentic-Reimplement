class Team():
    """
    一个team，包括多个agents和一个工作流（彼此之间怎么交互的）。
    一个粒子包括一个team，由多个通过工作流定义的agents组成，可执行代码由LLM_write_forward生成。
    Attributes :
        llm : LLM model to be used
        roles : List of agents in the team
        workflow : Workflow of the team
        task : Task to be solved by the team
        message_pool : Message pool for the team
    """

    def __init__(self, llm, logger) -> None:
        """
        初始化一个 Team 实例。
        Args :
            llm : LLM model to be used
            logger : Logger for logging messages
        """
        self.llm = llm
        self.roles = []
        self.workflow = None
        self.task = None
        self.message_pool = []
        self.logger = logger


    def call(self, required_role: str, inputs: List = [], output: str="") :
        """
        调用该角色时需要提供所需的agent名称。输入是来自其他agent的输出。
        Args :
            required_role ( str ) : name of the required agent .
            inputs ( List , optional ) : inputs for the agent . Defaults to [].
            output ( str , optional ) : output requirements for the agent . Defaults to "".
        Returns :
            response: response of the role.
        """
        return responses
                                    