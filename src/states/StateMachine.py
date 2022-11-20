from states import IState


class StateMachine:

    def __init__(self) -> None:
        self._stateDict = {}
        self._current = IState

    def add(self, key: str, state: IState):
        self._stateDict[key] = state

    def remove(self, key: str):
        self._stateDict.pop(key)

    def clear(self):
        self._stateDict.clear()

    def change(self, key: str):
        self._current = self._stateDict[key]

    def update(self):
        self._current.update()

    def handleInput(self, event):
        self._current.handleInput(event)

    def render(self):
        self._current.render()
