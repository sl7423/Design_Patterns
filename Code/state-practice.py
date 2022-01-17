from __future__ import annotations
from abc import ABC, abstractmethod

class AudioPlayer:

    _state = None

    #def __init__(self, UI, volume, playlist, currentSong, state: State):
    def __init__(self, state: State) -> None:
        self.changeState(state)
        # self.UI = UI
        # self.volume = volume
        # self.playlist = playlist
        # self.currentSong = currentSong

    def changeState(self, state: State):
        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.audioplayer = self

    def clickLock(self):
        self._state.clickLock()

    def clickPlay(self):
        self._state.clickPlay()

    def clickNext(self):
        self._state.clickNext()

    def clickPrevious(self):
        self._state.clickPrevious()

    def startPlayback(self) -> str:
        return f"Playing lovely music"

    def stopPlayback(self) -> str:
        return f"Stopping the playing of songs"

    def nextSong(self) -> str:
        return f"Playing the next song"

    def previousSong(self) -> str:
        return f"Playing the previous song"

    def fastForward(self, time) -> str:
        return f"fast Forward a song by {time}"

    def rewind(self, time) -> str:
        return f"Rewind a song by {time}"


class State(ABC):
    
    @property
    def audioplayer(self) -> AudioPlayer:
        return self._audioplayer

    @audioplayer.setter
    def audioplayer(self, audioplayer: AudioPlayer) -> AudioPlayer:
        self._audioplayer = audioplayer

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
    def clickLock(self, playing='yes') -> None:
        if playing == 'yes':
            self.changeState(PlayingState())
        else:
            self.changeState(ReadyState())

    def clickPlay(self) -> str:
        return "Locked and do nothing!"

    def clickNext(self) -> str:
        return "Locked and do nothing"

    def clickPrevious(self) -> str:
        return "Locked and do nothing"

class ReadyState(State):
    def clickLock(self) -> None:
        self.changeState(LockedState())

    def clickPlay(self) -> None:
        self.audioplayer.startPlayback()
        self.audioplayer.changeState(PlayingState())

    def clickNext(self) -> None:
        self.nextSong()

    def clickPrevious(self):
        self.previousSong()

class PlayingState(State):
    def clickLock(self) -> None:
        self.changeState(LockedState())

    def clickPlay(self):
        self.stopPlayback()
        self.changeState(ReadyState())

    def clickNext(self, doubleclick='Yes'):
        if doubleclick == 'Yes':
            self.nextSong()
        else:
            self.fastForward(5)
    

    def clickPrevious(self, doubleclick="Yes"):
        if doubleclick == 'Yes':
            self.previousSong()
        else:
            self.rewind(5)

if __name__ == '__main__':
    #context = AudioPlayer('GUI', 50, "EDM", "Don't you worry child", ReadyState())
    context = AudioPlayer(ReadyState())
    context.clickPlay()


