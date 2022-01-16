from abc import ABC, abstractmethod

class AudioPlayer:

    _state = None

    def __init__(self, state: State, UI, volume, playlist, currentSong):
        self.changeState = state
        self.UI = UI
        self.volume = volume
        self.playlist = playlist
        self.currentSong = currentSong

    def changeState(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    def clickLock(self):
        return self._state.clickLock()

    def clickPlay(self):
        return self._state.clickPlay()

    def clickNext(self):
        return self._state.clickNext()

    def clickPrevious(self):
        return self._state.clickPrevious()

    def startPlayback(self):
        return "Playing lovely music"

    def stopPlayback(self):
        return "Stopping the playing of songs"

    def nextSong(self):
        return "Playing the next song"

    def previousSong(self):
        return "Playing the previous song"

    def fastForward(self, time):
        pass

    def rewind(self, time):
        pass


class State(ABC):
    
    @property
    def audioplayer(self) -> AudioPlayer:
        return self._audioplayer

    @audioplayer.setter
    def audioplayer(self, audioplayer: AudioPlayer) -> AudioPlayer:
        self._audioplayer = AudioPlayer 

    @abstractmethod
    def clickLock(self):
        pass

    @abstractmethod
    def clickPlay(self):
        pass

    @abstractmethod
    def clickNext(self):
        pass

    @abstractmethod
    def clickPrevious(self):
        pass
    

class LockedState(State):
    def clickLock(self) -> None:
        pass   
        # if self._state == ReadyState():

        # else:
        #     self._state == LockedState():

    def clickPlay(self) -> None:
        return "Locked and do nothing!"

    def clickNext(self) -> None:
        return "Locked and do nothing"

    def clickPrevious(self) -> None:
        return "Locked and do nothing"

class ReadyState(State):
    def clickLock(self) -> None:
        self.changeState(LockedState())

    def clickPlay(self) -> None:
        self.